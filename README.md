# 🛡️ PhishScope

**PhishScope** is a Flask-based phishing email analysis platform designed to help identify suspicious emails through automated threat analysis. It parses email files (`.eml`), extracts Indicators of Compromise (IOCs), analyzes multiple phishing indicators, assigns a threat score, and generates a professional PDF security report.

Built as a cybersecurity portfolio project to demonstrate practical skills in Python, Flask, phishing detection, threat analysis, and reporting.

---

## 📌 Features

- 📧 Parse `.eml` email files
- 👤 Analyze sender information
- 🔗 Detect and inspect URLs
- 🧠 Identify phishing keywords
- 📨 Analyze email headers
- 📎 Inspect attachments
- 🎯 Extract Indicators of Compromise (IOCs)
- 📊 Calculate an overall threat score
- 📈 Interactive dashboard with charts
- 📄 Generate professional PDF security reports
- 🎨 Modern cybersecurity-themed UI

---

## 📷 Screenshots

### Home Page

> Add your screenshot here

```
screenshots/Home.png
```

---

### Analysis Dashboard

> Add your screenshot here

```
screenshots/Analysis.png
screenshots/Main Dashboard.png
screenshots/Ioc Dashboard.png
screenshots/Threat Score Dashboard.png
```

---

### Generated PDF Report

> Add your screenshot here

```
screenshots/Report.png
screenshots/Report2.png
```

---

## 🏗️ Project Structure

```
PhishScope/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── modules/
│   ├── parser.py
│   ├── sender_analysis.py
│   ├── url_analysis.py
│   ├── keyword_analysis.py
│   ├── header_analysis.py
│   ├── attachment_analysis.py
│   ├── ioc_extractor.py
│   ├── risk_engine.py
│   └── report_generator.py
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── dashboard.html
│
├── uploads/
├── reports/
├── screenshots/
└── samples/
```

---

## ⚙️ Technologies Used

### Backend

- Python
- Flask

### Frontend

- HTML5
- CSS3
- JavaScript
- Chart.js

### Cybersecurity

- Email Parsing
- IOC Extraction
- Threat Scoring
- Phishing Detection

### Reporting

- ReportLab
- Matplotlib

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/prathameshk-programmer/PhishScope.git
```

Move into the project directory

```bash
cd PhishScope
```

Create a virtual environment (optional)

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 🔍 How It Works

1. Upload a `.eml` email file.
2. PhishScope parses the email contents.
3. Sender reputation, URLs, keywords, headers, and attachments are analyzed.
4. Indicators of Compromise (IOCs) are extracted.
5. A weighted threat score is calculated.
6. A SOC-style dashboard displays the results.
7. A PDF security assessment report is generated.

---

## 📊 Current Analysis Modules

- Sender Analysis
- URL Analysis
- Keyword Detection
- Header Analysis
- Attachment Analysis
- IOC Extraction
- Risk Scoring
- PDF Report Generation

---

## 🔮 Future Improvements

- VirusTotal API integration
- URL reputation checking
- WHOIS lookup
- Machine Learning phishing detection
- Email authentication (SPF, DKIM, DMARC)
- MITRE ATT&CK technique mapping
- User authentication
- Scan history database
- Dark mode/light mode toggle
- Docker deployment

---

## 🎯 Learning Outcomes

This project helped me strengthen my understanding of:

- Python development
- Flask web applications
- Email parsing
- Cybersecurity fundamentals
- Phishing analysis
- Threat intelligence concepts
- IOC identification
- Report automation
- Git and GitHub workflows

---

## ⚠️ Disclaimer

This project is intended for educational purposes only.

It is designed to help users understand phishing analysis techniques and should not be used to process confidential or sensitive emails without appropriate authorization.

---

## 📄 License

This project is licensed under the MIT License.

See the **LICENSE** file for details.

---

## 👨‍💻 Author

**prathameshk-programmer**

B.Sc. Information Technology (Hons. with Research)

Cybersecurity Enthusiast | Python Developer | Aspiring Cybersecurity Analyst

GitHub:
https://github.com/prathameshk-programmer

---

⭐ If you found this project interesting, consider giving it a star!
