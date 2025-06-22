# ----------------------------
# 📦 requirements.txt
# ----------------------------
openai
python-dotenv
requests
imaplib2
email-validator
smtplib

# ----------------------------
# 📘 README.md
# ----------------------------
# Solution Center Agent

An intelligent email-based assistant that reads user queries and interacts with enterprise systems like Concur, Corporate Card, and Invoice Processing.

## 🚀 Features
- Email reader and responder
- LLM-based intent detection
- Modular routing to backend systems
- API-based integration

## 🧰 Technologies Used
- Python
- OpenAI GPT-4
- IMAP/SMTP
- REST API clients

## 📁 Project Structure
```
project_root/
├── config.py
├── main.py
├── requirements.txt
├── .env
├── email_reader.py
├── email_sender.py
├── intent_classifier.py
├── response_generator.py
├── router.py
├── systems/
└── utils/
```

## 🔧 Setup Instructions
1. Clone the repo:
```bash
git clone https://github.com/your_org/solution-center-agent.git
cd solution-center-agent
```

2. Create a `.env` file:
```
OPENAI_API_KEY=your_openai_key
EMAIL_USER=solution@yourcompany.com
EMAIL_PASS=your_password
SMTP_SERVER=smtp.yourcompany.com
IMAP_SERVER=imap.yourcompany.com
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the agent:
```bash
python main.py
