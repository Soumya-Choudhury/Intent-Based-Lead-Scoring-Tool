# Intent-Based-Lead-Scoring-Tool

A lightweight, real-time, AI-enhanced Streamlit app that simulates lead scoring based on hiring activity and content intent signals.

---

## 🚀 Overview

This tool allows Go-To-Market (GTM) teams to upload a list of company leads and receive a prioritized output based on simulated indicators of buying intent:
- Active hiring in relevant roles
- Presence of growth/automation-related keywords in company content

It’s designed as a **prototype** to showcase how real-time external signals can be used for smarter lead targeting and sales prioritization.

---

## 🧠 How It Works

1. Upload a `.csv` file with a column named `company`.
2. The app simulates:
   - **Job Posting Signals** – randomly assigns hiring activity and roles.
   - **Content Mining** – randomly assigns blog/news keywords linked to buying intent.
3. A **rule-based scoring model** assigns an `Intent Score` out of 10 for each company.

---

## 🛠️ Scoring Logic

| Signal              | Points           |
|---------------------|------------------|
| Hiring Active       | +4               |
| Each Intent Keyword | +2 (max up to 10)|

Intent keywords include:
`"scaling", "automation", "growth", "AI tools", "customer acquisition", "CRM"`

---

## 🧪 Dataset (Why Dummy?)

Due to privacy and time constraints, the dataset uses **dummy company names and simulated data**.  
This mimics public signal-based scoring without violating terms of service or data sharing policies.

✅ In real-time deployment:
- Hiring data could be fetched from LinkedIn Jobs or Greenhouse APIs.
- Content signals could be scraped from blogs, RSS feeds, or APIs like BuiltWith / Clearbit.

---

## 📂 Files

- `app.py` – Main Streamlit app
- `sample_leads.csv` – Sample input format
- `Intent_Based_Lead_Prioritization_Report_OnePage.docx` – 1-pager technical report
- `README.md` – GitHub project overview

---

## 📈 Business Value

This tool helps:
- GTM/Sales teams focus on **high-intent accounts**
- Reduce **wasted outreach** to cold leads
- Lay foundation for **real-time, API-integrated scoring engines**

---

## 🔧 How to Run

Install the required libraries:

```bash
pip install streamlit pandas
```

Launch the Streamlit app:
```bash
streamlit run app.py
```
## ✍️ Author

**Soumya Choudhury**  
---

## 🏁 Future Work

- Integrate live job scraping via LinkedIn/Indeed APIs  
- Real-time blog/news scraping  
- Deploy as a hosted Streamlit app  
- CRM integration with HubSpot or Salesforce

---
