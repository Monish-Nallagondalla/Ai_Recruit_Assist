"""Streamlit app for Ai_Recruit_Assist"""
import streamlit as st
from src.Ai_Recruit_Assist.config.configuration import Config
from src.Ai_Recruit_Assist.utils.groq_client import GroqClient
from src.Ai_Recruit_Assist.utils.pdf_processor import extract_text_from_pdf
from src.Ai_Recruit_Assist.components.candidate_screening import CandidateScreening
from src.Ai_Recruit_Assist.components.email_handler import EmailHandler
from src.Ai_Recruit_Assist.constants.constants import MIN_SCORE_THRESHOLD
from datetime import datetime, timedelta
import pytz
from groq import BadRequestError

def main():
    """Main Streamlit app"""
    st.title("AI Recruit Assist")
    config = Config()
    groq_client = GroqClient(config.groq_api_key)
    screening = CandidateScreening(groq_client)
    email_handler = EmailHandler(groq_client, config.from_email)

    # Input form
    with st.form("candidate_form"):
        resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
        job_description = st.text_area("Job Description")
        submit = st.form_submit_button("Screen Candidate")

    if submit and resume_file and job_description:
        with st.spinner("Processing..."):
            # Extract resume content, name, and email
            resume_content, extracted_name, extracted_email = extract_text_from_pdf(resume_file, config.groq_api_key)
            if not resume_content or not extracted_name or not extracted_email:
                st.error("Failed to process the uploaded resume or extract name and email. Please ensure it is a valid PDF file with extractable text, name, and email.")
                return

            # Display extracted name and email, allow email to be edited
            st.subheader("Extracted Candidate Information")
            st.write(f"**Name**: {extracted_name}")
            candidate_email = st.text_input("**Email** (edit if needed)", value=extracted_email)
            candidate_name = extracted_name  # Name is not editable

            # Screen candidate
            try:
                result = screening.screen(candidate_name, candidate_email, resume_content, job_description)
                st.write(f"Score: {result.score}")
                st.write(f"Feedback: {result.feedback}")

                if result.score > MIN_SCORE_THRESHOLD:
                    # Schedule interview (mock scheduling)
                    tz = pytz.timezone(config.timezone)
                    call_time = (datetime.now(tz) + timedelta(days=1)).replace(hour=10, minute=0, second=0)
                    call_url = "https://mock-zoom.us/j/123456789"  # Mock Zoom URL
                    st.success(f"Interview scheduled for {call_time} at {call_url}")

                    # Generate email
                    email = email_handler.write_email(candidate_name, candidate_email, str(call_time), call_url)
                    st.subheader("Drafted Email")
                    st.write(f"**Subject**: {email.subject}")
                    st.write(f"**Body**:")
                    st.text_area("Email Body", email.body, height=200, disabled=True)

                    # Button to confirm sending
                    if st.button("Send Email"):
                        email_handler.send_email(candidate_email, email.subject, email.body)
                        st.success("Email sent to candidate")
                else:
                    st.warning("Candidate did not meet the score threshold")
            except ValueError as e:
                st.error(f"Failed to screen candidate: {str(e)}. Raw response may be malformed. Please try again or check the Groq API configuration.")
                return
            except BadRequestError as e:
                st.error(f"Groq API error: {str(e)}. Please check if the model is supported or if rate limits are exceeded. See https://console.groq.com/docs/deprecations for supported models.")
                return

if __name__ == "__main__":
    main()