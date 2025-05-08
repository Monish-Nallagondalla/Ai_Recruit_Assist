"""PDF processing utilities"""
from io import BytesIO
from pypdf import PdfReader
from streamlit.runtime.uploaded_file_manager import UploadedFile
import re
from groq import Groq
import json

def extract_text_from_pdf(uploaded_file: UploadedFile, groq_api_key: str) -> tuple[str, str, str]:
    """Extract text content, candidate name, and email from an uploaded PDF file using Groq API for name extraction"""
    try:
        # Verify file type
        if uploaded_file.type != 'application/pdf':
            raise ValueError(f"Uploaded file is not a PDF. File type: {uploaded_file.type}")

        # Read uploaded file content
        pdf_file = BytesIO(uploaded_file.read())
        pdf_reader = PdfReader(pdf_file)

        # Extract text from all pages
        text_content = ""
        for page in pdf_reader.pages:
            text = page.extract_text()
            if text:
                text_content += text

        if not text_content:
            raise ValueError("No text could be extracted from the PDF")

        # Extract email using regex
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        email_match = re.search(email_pattern, text_content)
        candidate_email = email_match.group(0) if email_match else ""

        if not candidate_email:
            raise ValueError("Could not extract candidate email from the PDF")

        # Use Groq API to extract the candidate name
        groq_client = Groq(api_key=groq_api_key)
        prompt = (
            "You are an expert at extracting information from resumes. "
            "Given the following resume text, identify the candidate's full name (first and last name if available). "
            "Return the name in a JSON object with a single field 'name' (string). "
            "Example response: {\"name\": \"John Doe\"}. "
            "Ensure the response is valid JSON, enclosed in curly braces, and contains only the specified field. "
            "Do not include any additional text, code blocks, or explanations outside the JSON object.\n\n"
            f"Resume text: {text_content[:2000]}"  # Limit to 2000 chars to avoid token limits
        )

        response = groq_client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100,
        )
        content = response.choices[0].message.content

        # Parse the JSON response
        try:
            parsed_response = json.loads(content)
            candidate_name = parsed_response.get("name", "")
        except json.JSONDecodeError:
            raise ValueError(f"Failed to parse Groq API response for name extraction: {content}")

        if not candidate_name:
            raise ValueError("Could not extract candidate name from the PDF using Groq API")

        return text_content, candidate_name, candidate_email

    except ValueError as e:
        print(f"Error processing PDF: {str(e)}")
        return "", "", ""
    except Exception as e:
        print(f"Unexpected error processing PDF: {str(e)}")
        return "", "", ""