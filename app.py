# Intent-Based Lead Scoring Tool (Streamlit)
import streamlit as st
import pandas as pd
import random
import time

st.set_page_config(page_title="Intent-Based Lead Scoring", layout="wide")
st.title("🔍 Intent-Based Lead Prioritization Tool")

st.markdown("""
Upload a list of company domains or names, and we'll simulate real-time analysis:
- Job Postings
- Blog/News Content
- Intent Signals
""")

uploaded_file = st.file_uploader("Upload a CSV with a column named 'company'", type="csv")

intent_keywords = ["scaling", "automation", "growth", "AI tools", "customer acquisition", "CRM"]

def simulate_job_postings(company):
    # Randomly simulate hiring intent
    hiring = random.choice([True, False])
    role = random.choice(["Data Scientist", "Marketing Manager", "Sales Ops", "None"])
    return hiring, role if hiring else "-"

def simulate_blog_mentions(company):
    # Simulate finding blog keywords
    mentioned_keywords = random.sample(intent_keywords, k=random.randint(0, 3))
    return mentioned_keywords

def compute_intent_score(hiring, keywords):
    score = 0
    if hiring:
        score += 4
    score += len(keywords) * 2
    return min(score, 10.0)

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    if "company" not in df.columns:
        st.error("CSV must have a 'company' column.")
    else:
        st.success("Analyzing leads for buying intent...")
        results = []

        for company in df["company"]:
            time.sleep(0.2)  # simulate delay
            hiring, role = simulate_job_postings(company)
            keywords = simulate_blog_mentions(company)
            score = compute_intent_score(hiring, keywords)

            results.append({
                "Company": company,
                "Hiring": "Yes" if hiring else "No",
                "Role Posted": role,
                "Intent Keywords": ", ".join(keywords) if keywords else "-",
                "Intent Score": score
            })

        result_df = pd.DataFrame(results)
        st.dataframe(result_df)

        csv = result_df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Scored Leads", csv, "intent_scored_leads.csv", "text/csv")
else:
    st.info("Awaiting CSV upload...")
