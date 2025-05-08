Ai_Recruit_Assist

Ai_Recruit_Assist is a Streamlit-based web application designed to streamline the candidate screening process for recruiters. It extracts candidate information (name and email) from a resume PDF, screens candidates using AI (via Groq API), and generates interview invitation emails. The app leverages large language models (LLMs) to evaluate resumes against job descriptions, assign scores, and provide feedback.

Features





Resume Parsing: Extracts candidate name and email from a PDF resume using LLMs and regex.



Candidate Screening: Evaluates candidates based on resume content and job description using Groq's llama3-8b-8192 model.



Scoring and Feedback: Assigns a score (0-10) and provides detailed feedback on candidate suitability.



Interview Scheduling: Automatically schedules a mock interview for candidates above a score threshold.



Email Generation: Drafts professional interview invitation emails with editable email addresses.



User-Friendly UI: Built with Streamlit for an intuitive interface.

Prerequisites





Python 3.8 or higher



A Groq API key (sign up at Groq Console to obtain one)



Git (for cloning the repository)

Installation





Clone the Repository:

git clone https://github.com/Monish-Nallagondalla/Ai_Recruit_Assist.git
cd Ai_Recruit_Assist



Set Up a Virtual Environment (optional but recommended):

python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate



Install Dependencies:

pip install -r requirements.txt



Configure Environment:





Create a config.yaml file in the config directory or a .env file in the project root.



Add your Groq API key and other configurations:

# config/config.yaml
groq_api_key: "your-groq-api-key"
from_email: "recruiter@ai-recruit-assist.com"
timezone: "Asia/Kolkata"

Or:

# .env
GROQ_API_KEY=your-groq-api-key
FROM_EMAIL=recruiter@ai-recruit-assist.com
TIMEZONE=Asia/Kolkata

Usage





Run the Application:

streamlit run app.py



Access the App:





Open your browser and go to http://localhost:8501.



Upload a resume PDF (e.g., Monish_2025_2.pdf).



Enter a job description (e.g., "We are hiring a Data Scientist! Requirements: Proficiency in Python, R, or similar languages. Experience with machine learning frameworks (e.g., TensorFlow, PyTorch). Strong statistical analysis skills. Bonus: Experience with big data tools (e.g., Hadoop, Spark).").



Click "Screen Candidate".



Review Results:





The app will display the extracted candidate name and email (with an option to edit the email).



It will show the candidate's score and feedback.



If the score is above the threshold (7.0), it schedules a mock interview and drafts an email.



You can review the email and click "Send Email" to mock-send it (output will be printed to the console).

Project Structure

Ai_Recruit_Assist/
│
├── app.py                     # Main Streamlit app
├── requirements.txt           # Project dependencies
├── config/
│   ├── config.yaml            # Configuration file (template)
│   └── configuration.py       # Config loading logic
├── src/
│   └── Ai_Recruit_Assist/
│       ├── components/
│       │   ├── candidate_screening.py  # Screening logic using Groq API
│       │   └── email_handler.py       # Email generation and mock sending
│       ├── constants/
│       │   └── constants.py           # Constants (e.g., score threshold)
│       └── utils/
│           ├── groq_client.py         # Groq API client
│           └── pdf_processor.py       # PDF parsing and info extraction
├── tests/                     # Unit tests (optional, not fully implemented)
└── README.md                  # Project documentation

Dependencies





streamlit: For the web interface



pypdf: For PDF parsing



groq: For interacting with the Groq API



pydantic: For data validation and modeling



python-dotenv: For environment variable management

See requirements.txt for the full list.

Troubleshooting





Groq API Errors:





Ensure your API key is valid and has sufficient quota. Check usage at Groq Console.



If you hit rate limits, wait a few seconds and retry, or reduce max_tokens in groq_client.py.



PDF Parsing Issues:





Ensure the resume PDF contains extractable text and a standard email format (e.g., user@domain.com).



If name extraction fails, the LLM prompt in pdf_processor.py may need adjustment based on your resume format.



JSON Parsing Errors:





Check the console for Raw Groq response: ... logs to debug invalid JSON responses.



Adjust prompts in candidate_screening.py or email_handler.py if needed.

Contributing

Contributions are welcome! Please follow these steps:





Fork the repository.



Create a new branch (git checkout -b feature/your-feature).



Make your changes and commit (git commit -m "Add your feature").



Push to your branch (git push origin feature/your-feature).



Open a pull request.

Please ensure your code follows the existing style and includes appropriate tests.

License

This project is licensed under the MIT License. See the LICENSE file for details (if added).

Contact

For issues or inquiries, please open an issue on GitHub or contact the maintainer at nsmonish@gmail.com.



Built with ❤️ by Monish Nallagondalla