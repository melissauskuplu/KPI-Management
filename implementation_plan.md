# Autonomous Reporting System Implementation Plan

This plan outlines the creation of a Python-based reporting system that fetches live CSV data, processes it using Gemini AI for insights, and sends a professional HTML dashboard via email. It also includes setting up a monthly schedule.

## User Review Required

> [!IMPORTANT]
> - **API Key & Credentials**: I will use the provided Gemini API key and SMTP app password. Please ensure these are correct and active.
> - **Email Recipient**: The report will be sent to `recipient mail` from `sender mail`.
> - **Scheduling**: I will use the Windows `schtasks` command to schedule the script for the 1st of every month at 09:00 AM.

## Proposed Changes

### Reporting Script

#### [NEW] [test_run.py]

The script will contain:
1.  **Data Fetching**: A function using `requests` with a professional User-Agent header to download the CSV from the provided Google Sheets link.
2.  **Gemini AI Analysis**:
    *   Integration with `google-generativeai`.
    *   Logic to convert CSV data to a JSON format for the AI.
    *   A prompt specifically instructed to return a 3-paragraph executive summary in raw HTML format with a professional dashboard design (dark navy header, white rounded cards, blue highlights).
3.  **Secure Delivery**:
    *   Use `smtplib` and `email.mime` to send the generated HTML content.
    *   Configuration for Gmail's SMTP server using the provided app password.

## Verification Plan

### Automated Tests
1.  **Execution**: Run `python test_run.py` manually to verify the entire flow from fetching to sending.
2.  **Output Verification**: Check logs for successful CSV download, Gemini response parsing, and SMTP delivery.

### Manual Verification
1.  **Email Receipt**: Ask the user (or check logs) to verify that the email was received and the HTML dashboard rendered correctly.
2.  **Scheduling Verification**: Run `schtasks /query /tn "MonthlyReport"` to ensure the task is correctly registered.

## Execution Steps

1.  **Draft Script**: Write the complete `test_run.py`.
2.  **Execution**: Run the script once immediately to perform the test run.
3.  **Scheduling**: Register the task with Windows Task Scheduler.
4.  **Confirm**: Report the results of the test run and parsing of 'Stanford Balbaners' data.
