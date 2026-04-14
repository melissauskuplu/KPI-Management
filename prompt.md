I need you to build a fully autonomous reporting system using the Gemini AI API and Python. This setup will leverage external generative capabilities to ensure high-performance data analysis.

Stage 1: Data Fetching (Live Link)

Create a Python script test_run.py that downloads the live CSV data from: https://docs.google.com/spreadsheets/d/(your id)/export?format=csv

Use a professional User-Agent header to ensure Google doesn't block the request.

Stage 2: External AI Processing (Gemini API Integration)

The script must use the google-generativeai library with API Key: gemini-api-key.

Model: models/gemini-flash-latest.

Role: Professional Data Analyst.

Instruction: 'Analyze data: {{ $json }}. Create a 3-paragraph executive summary (Sales, Efficiency, Error Rates) focusing on the October variance.

Output Format: Return ONLY raw HTML (no markdown). Use a dark navy (#1e293b) header and three white rounded cards for main KPIs. Use blue (#3b82f6) for key numbers. Design must look like a professional modern dashboard.'

Stage 3: Secure Delivery (SMTP Gateway)

Sender: sender mail

App Password: Google app pasword

Recipient: recipient mail

Subject: 'Monthly Performance and KPI Analysis Report'

Technical Requirement: Ensure the MIMEText is set to html so the report is rendered visually.

Stage 4: Scheduling & Execution

Configure a schedule for the 1st of every month at 09:00 AM.

Immediate Action: Write the final version of test_run.py, install all necessary libraries (google-generativeai, requests), and execute a test run now.

Confirmation: Please verify once the email has been sent and let me know if the Gemini API successfully parsed the 'Stanford Balbaners' KPI data.