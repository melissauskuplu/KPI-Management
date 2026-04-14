import requests
import pandas as pd
import google.generativeai as genai
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import io
import sys

# Configuration
CSV_URL = ""
GEMINI_API_KEY = ""
MODEL_NAME = "gemini-flash-latest"

SMTP_SENDER = ""
SMTP_PASSWORD = ""
SMTP_RECIPIENT = ""
EMAIL_SUBJECT = "Monthly Performance and KPI Analysis Report"

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

def fetch_csv_data(url):
    print(f"Fetching data from {url}...")
    headers = {"User-Agent": USER_AGENT}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    print("Data fetched successfully.")
    return response.content

def analyze_with_gemini(csv_content):
    print("Analyzing data with Gemini AI...")
    # Read CSV into a JSON format for Gemini
    df = pd.read_csv(io.BytesIO(csv_content))
    json_data = df.to_json(orient='records')
    
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(MODEL_NAME)
    
    instruction = f"""
    Role: Professional Data Analyst.
    Analyze data: {json_data}. 
    Create a 3-paragraph executive summary (Sales, Efficiency, Error Rates) focusing on the October variance.
    
    Output Format: Return ONLY raw HTML (no markdown code blocks, no ```html wrappers, just the raw HTML). 
    Design Requirements:
    - Use a dark navy (#1e293b) header.
    - Three white rounded cards for main KPIs. 
    - Use blue (#3b82f6) for key numbers. 
    - Design must look like a professional modern dashboard.
    - Responsive layout.
    """
    
    response = model.generate_content(instruction)
    html_content = response.text.strip()
    
    # Remove markdown wrappers if any were returned despite instructions
    if html_content.startswith("```html"):
        html_content = html_content.replace("```html", "", 1)
    if html_content.endswith("```"):
        html_content = html_content.rsplit("```", 1)[0]
        
    print("Gemini analysis complete.")
    return html_content

def send_email(html_body):
    print(f"Sending email to {SMTP_RECIPIENT}...")
    msg = MIMEMultipart("alternative")
    msg["Subject"] = EMAIL_SUBJECT
    msg["From"] = SMTP_SENDER
    msg["To"] = SMTP_RECIPIENT
    
    part = MIMEText(html_body, "html")
    msg.attach(part)
    
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SMTP_SENDER, SMTP_PASSWORD)
            server.sendmail(SMTP_SENDER, SMTP_RECIPIENT, msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
        raise

def main():
    try:
        csv_content = fetch_csv_data(CSV_URL)
        html_report = analyze_with_gemini(csv_content)
        send_email(html_report)
        print("Report generation and delivery successful.")
        
        # Check for 'Stanford Balbaners' in the CSV data for confirmation logic
        df = pd.read_csv(io.BytesIO(csv_content))
        if any(df.astype(str).apply(lambda x: x.str.contains('Stanford Balbaners').any(), axis=1)):
            print("Confirmation: 'Stanford Balbaners' KPI data was found and parsed.")
        else:
            print("Note: 'Stanford Balbaners' KPI data was not found in the raw CSV content.")
            
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
