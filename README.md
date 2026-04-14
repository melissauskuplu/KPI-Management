# 📊 Autonomous KPI Reporting System

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![AI](https://img.shields.io/badge/AI-Gemini%201.5%20Flash-orange.svg)](https://aistudio.google.com/)
[![Automation](https://img.shields.io/badge/Automation-Scheduled-green.svg)](https://github.com/)

A fully autonomous data pipeline that fetches live operational metrics, performs advanced analytics using the **Gemini AI API**, and dispatches a professional **HTML Executive Dashboard** via email.

## 🚀 Key Features

- **Live Data Ingestion:** Automated fetching of real-time CSV data from cloud sources using secure request headers.
- **Generative AI Intelligence:** Leverages **Gemini Flash** to act as a Senior Data Analyst, providing deep insights into sales performance and operational trends.
- **Modern Dashboard UI:** Generates a visually rich HTML email body featuring:
  - **Dark Navy (#1e293b) Header** for a sleek corporate identity.
  - **KPI Cards:** White rounded containers with drop shadows for clear metric presentation.
  - **Professional Accents:** Strategic use of blue (#3b82f6) for key financial figures.
- **Autonomous Scheduling:** Native integration for monthly execution (1st of every month at 09:00 AM) without manual intervention.

## 🏗️ System Architecture

1.  **Ingestion:** The system connects to the live data source and parses raw CSV into a structured format.
2.  **Analysis:** Data is processed by Gemini AI to generate a 3-paragraph executive summary focusing on efficiency and variance diagnostics.
3.  **Rendering:** The AI constructs the dashboard using inline CSS and raw HTML strings.
4.  **Delivery:** The final report is transmitted through a secure SMTP gateway with HTML rendering support.

## 🛠️ Technical Stack

- **Language:** Python 3.x
- **AI Engine:** `google-generativeai` (Gemini Flash Latest)
- **Networking:** `requests` with Professional User-Agent spoofing.
- **Communication:** `smtplib` & `email.mime` for high-fidelity HTML emails.

## 📂 Project Structure

* `test_run.py`: The core automation engine and logic.
* `README.md`: Technical documentation and project overview.

## 🔧 Setup & Configuration

1.  **Install Dependencies:**
    ```bash
    pip install google-generativeai requests
    ```

2.  **Environment Variables:**
    Configure the following credentials within the script:
    - Gemini API Key
    - SMTP App Password
    - Target CSV URL

3.  **Deployment:**
    Execute a test run to verify the pipeline:
    ```bash
    python test_run.py
    ```

## 📈 Executive Summary Focus

The automated reports prioritize three critical areas:
- **Sales Performance:** Revenue tracking vs. targets.
- **Operational Efficiency:** Process optimization and steady-state metrics.
- **Variance Analysis:** Identification and diagnosis of critical data deviations (e.g., October variance).

---
*Professional Data Automation & Analytics Project*
