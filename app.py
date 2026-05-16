import streamlit as st
import pdfplumber
import boto3
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os
from io import BytesIO

# -----------------------------
# AWS S3 Configuration
# -----------------------------
s3 = boto3.client(
    "s3",
   s3 = boto3.client("s3")
)

BUCKET_NAME = "ai-resume-screening-swathi"

# -----------------------------
# Database Connection
# -----------------------------
conn = sqlite3.connect(
    "candidates.db",
    check_same_thread=False
)

cursor = conn.cursor()

# -----------------------------
# Create Table
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS candidates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    matched_skills TEXT,
    missing_skills TEXT,
    score REAL,
    recommendation TEXT
)
""")

conn.commit()

# -----------------------------
# Streamlit App Title
# -----------------------------
st.title("AI Resume Screening System")

# -----------------------------
# Upload Resume
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

# -----------------------------
# Main Logic
# -----------------------------
if uploaded_file is not None:

    st.success("Resume Uploaded Successfully")

    # Read File Bytes
    file_bytes = uploaded_file.read()

    # -----------------------------
    # Upload Resume to AWS S3
    # -----------------------------
    s3.upload_fileobj(
        BytesIO(file_bytes),
        BUCKET_NAME,
        uploaded_file.name
    )

    st.success("Resume Uploaded to AWS S3")

    # -----------------------------
    # Download Resume from AWS S3
    # -----------------------------
    download_path = f"downloaded_{uploaded_file.name}"

    s3.download_file(
        BUCKET_NAME,
        uploaded_file.name,
        download_path
    )

    st.success("Resume Downloaded from AWS S3")

    # -----------------------------
    # Extract Text from PDF
    # -----------------------------
    text = ""

    with pdfplumber.open(BytesIO(file_bytes)) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

    # -----------------------------
    # Display Resume Text
    # -----------------------------
    st.subheader("Extracted Resume Text")
    st.write(text)

    # -----------------------------
    # Convert Text to Lowercase
    # -----------------------------
    resume_text = text.lower()

    # -----------------------------
    # Required Skills
    # -----------------------------
    required_skills = [
        "python",
        "aws",
        "sql",
        "machine learning",
        "java",
        "communication"
    ]

    # -----------------------------
    # Match Skills
    # -----------------------------
    matched_skills = []
    missing_skills = []

    for skill in required_skills:

        if skill in resume_text:
            matched_skills.append(skill)

        else:
            missing_skills.append(skill)

    # -----------------------------
    # Candidate Score
    # -----------------------------
    score = (
        len(matched_skills)
        / len(required_skills)
    ) * 100

    # -----------------------------
    # Display Skills
    # -----------------------------
    st.subheader("Matched Skills")
    st.write(matched_skills)

    st.subheader("Missing Skills")
    st.write(missing_skills)

    # -----------------------------
    # Display Candidate Score
    # -----------------------------
    st.subheader("Candidate Score")
    st.write(f"{score:.2f}%")

    # -----------------------------
    # AI Resume Analysis
    # -----------------------------
    st.subheader("AI Resume Analysis")

    strengths = f"""
    Candidate has knowledge in:
    {', '.join(matched_skills)}
    """

    # Recommendation
    if score >= 70:
        recommendation = "Strong Candidate"

    elif score >= 40:
        recommendation = "Average Candidate"

    else:
        recommendation = "Needs Improvement"

    # -----------------------------
    # Interview Questions
    # -----------------------------
    interview_questions = []

    for skill in matched_skills[:3]:

        interview_questions.append(
            f"Explain your experience with {skill}."
        )

    # -----------------------------
    # Display Analysis
    # -----------------------------
    st.write("### Strengths")
    st.write(strengths)

    st.write("### Hiring Recommendation")
    st.write(recommendation)

    st.write("### Suggested Interview Questions")

    for question in interview_questions:

        st.write("-", question)

    # -----------------------------
    # Store Candidate Data
    # -----------------------------
    cursor.execute("""
    INSERT INTO candidates (
        filename,
        matched_skills,
        missing_skills,
        score,
        recommendation
    )
    VALUES (?, ?, ?, ?, ?)
    """, (
        uploaded_file.name,
        ", ".join(matched_skills),
        ", ".join(missing_skills),
        score,
        recommendation
    ))

    conn.commit()

    st.success("Candidate Data Stored in Database")
    # -----------------------------
# Candidate Dashboard
# -----------------------------
st.subheader("Candidate Dashboard")

query = """
SELECT * FROM candidates
"""

df = pd.read_sql_query(
    query,
    conn
)

st.dataframe(df)
# -----------------------------
# Score Bar Chart
# -----------------------------
st.subheader("Candidate Scores")

fig, ax = plt.subplots()

ax.bar(
    df["filename"],
    df["score"]
)

plt.xticks(rotation=45)

st.pyplot(fig)

# -----------------------------
# Recommendation Pie Chart
# -----------------------------
st.subheader("Hiring Recommendations")

recommendation_counts = df["recommendation"].value_counts()

fig2, ax2 = plt.subplots()

ax2.pie(
    recommendation_counts,
    labels=recommendation_counts.index,
    autopct="%1.1f%%"
)

st.pyplot(fig2)