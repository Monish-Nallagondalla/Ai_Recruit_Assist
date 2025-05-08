# Ai_Recruit_Assist

**Ai_Recruit_Assist** is a Streamlit-based web application designed to streamline the candidate screening process for recruiters. It extracts candidate information (name and email) from resumes (PDFs), screens candidates using AI (via Groq API), and generates interview invitation emails. The app leverages large language models (LLMs) to evaluate resumes against job descriptions, assign scores, and provide detailed feedback.

---

## Features

- **Resume Parsing**: Extract candidate names and emails from PDF resumes using LLMs and regex.
- **Candidate Screening**: Evaluate candidates based on resume content and job descriptions using Groq's `llama3-8b-8192` model.
- **Scoring and Feedback**: Assign scores (0–10) and provide feedback on candidate suitability.
- **Interview Scheduling**: Automatically schedule mock interviews for candidates meeting score thresholds.
- **Email Generation**: Draft professional interview invitation emails with editable recipient addresses.
- **User-Friendly Interface**: Built with Streamlit for an intuitive and seamless user experience.

---

## Prerequisites

- Python 3.8 or higher  
- A Groq API key (sign up at [Groq Console](https://groq.io) to obtain one)  
- Git (for cloning the repository)  

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Monish-Nallagondalla/Ai_Recruit_Assist.git
   cd Ai_Recruit_Assist

2. **Set Up a Virtual Environment** (optional but recommended):

   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment**:
   Create a `config.yaml` file in the `config` directory or a `.env` file in the project root. Add your Groq API key and other configurations:

   * `config/config.yaml`:

     ```yaml
     groq_api_key: "your-groq-api-key"
     from_email: "recruiter@ai-recruit-assist.com"
     timezone: "Asia/Kolkata"
     ```
   * OR `.env`:

     ```env
     GROQ_API_KEY=your-groq-api-key
     FROM_EMAIL=recruiter@ai-recruit-assist.com
     TIMEZONE=Asia/Kolkata
     ```

---

## Usage

1. **Run the Application**:

   ```bash
   streamlit run app.py
   ```

2. **Access the App**:
   Open your browser and navigate to [http://localhost:8501](http://localhost:8501).

3. **Steps to Use**:

   * Upload a resume PDF (e.g., `Monish_2025_2.pdf`).
   * Enter a job description (e.g., “We are hiring a Data Scientist! Requirements: Proficiency in Python, experience with ML frameworks, strong statistical skills, etc.”).
   * Click **Screen Candidate**.

4. **Review Results**:

   * View extracted candidate name and email (with editable options).
   * Check the candidate’s score and feedback.
   * For candidates scoring above the threshold (e.g., 7.0), the app schedules a mock interview and drafts an email.
   * Review and send the email (output displayed in the console).

---

## Project Structure

```
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
│       │   └── email_handler.py        # Email generation and mock sending
│       ├── constants/
│       │   └── constants.py           # Constants (e.g., score threshold)
│       └── utils/
│           ├── groq_client.py         # Groq API client
│           └── pdf_processor.py       # PDF parsing and info extraction
├── tests/                     # Unit tests (optional, not fully implemented)
└── README.md                  # Project documentation
```

---

## Dependencies

* `streamlit`: For the web interface
* `pypdf`: For PDF parsing
* `groq`: For interacting with the Groq API
* `pydantic`: For data validation and modeling
* `python-dotenv`: For managing environment variables

See `requirements.txt` for the complete list.

---

## Troubleshooting

### Groq API Errors:

* Ensure your API key is valid and has sufficient quota. Check usage at [Groq Console](https://groq.io).
* For rate limits, wait a few seconds and retry or reduce `max_tokens` in `groq_client.py`.

### PDF Parsing Issues:

* Ensure the resume PDF contains extractable text and a valid email format (e.g., `user@domain.com`).
* Adjust the LLM prompt in `pdf_processor.py` for specific resume formats.

### JSON Parsing Errors:

* Check console logs for `Raw Groq response: ...` to debug.
* Modify prompts in `candidate_screening.py` or `email_handler.py` if needed.

---

## Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:

   ```bash
   git commit -m "Add your feature"
   ```
4. Push to your branch:

   ```bash
   git push origin feature/your-feature
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

For issues or inquiries, open an issue on GitHub or contact the maintainer:
📧 **[nsmonish@gmail.com](mailto:nsmonish@gmail.com)**

---

**Built with ❤️ by Monish Nallagondalla**
