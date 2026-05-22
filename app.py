import streamlit as st
import matplotlib.pyplot as plt
from PyPDF2 import PdfReader

# PAGE CONFIG
st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="wide"
)

# TITLE
st.markdown("""
# 💬 AI Resume Analyzer
### NLP-Based Resume Skill Scanner
Upload a resume and receive AI-style feedback.
""")

st.markdown("---")

# REQUIRED SKILLS
required_skills = [
    "python",
    "machine learning",
    "data analysis",
    "streamlit",
    "pandas",
    "scikit-learn",
    "sql",
    "deep learning"
]

# FILE UPLOAD
uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["txt", "pdf"]
)

resume_text = ""

# READ TXT
if uploaded_file is not None:

    if uploaded_file.type == "text/plain":
        resume_text = uploaded_file.read().decode("utf-8")

    # READ PDF
    elif uploaded_file.type == "application/pdf":

        pdf_reader = PdfReader(uploaded_file)

        for page in pdf_reader.pages:
            resume_text += page.extract_text()

    resume_text = resume_text.lower()

    # DISPLAY TEXT
    st.subheader("📄 Resume Content")

    st.text_area(
        "Resume Text",
        resume_text,
        height=250
    )

    st.markdown("---")

    # SKILL ANALYSIS
    matched_skills = []
    missing_skills = []

    for skill in required_skills:

        if skill in resume_text:
            matched_skills.append(skill)

        else:
            missing_skills.append(skill)

    # SCORE
    score = int(
        (len(matched_skills) / len(required_skills)) * 100
    )

    st.subheader("📊 Resume Match Score")

    st.metric(
        "ATS Match Score",
        f"{score}%"
    )

    st.progress(score / 100)

    st.markdown("---")

    # SKILLS
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✅ Matched Skills")

        for skill in matched_skills:
            st.success(skill)

    with col2:
        st.subheader("❌ Missing Skills")

        for skill in missing_skills:
            st.error(skill)

    st.markdown("---")

    # CHART
    st.subheader("📈 Skill Analysis")

    labels = ["Matched", "Missing"]

    values = [
        len(matched_skills),
        len(missing_skills)
    ]

    fig, ax = plt.subplots()

    ax.bar(labels, values)

    st.pyplot(fig)

    st.markdown("---")

    # AI FEEDBACK
    st.subheader("🤖 AI Career Feedback")

    if score >= 80:

        st.success("""
Strong technical profile detected.

Your resume demonstrates a solid alignment with
modern AI and data-focused roles.
Continue building deployed portfolio projects
and emphasize measurable achievements.
""")

    elif score >= 50:

        st.warning("""
Your resume shows promising technical skills,
but additional optimization is recommended.

Consider improving:
- SQL
- deployment experience
- machine learning projects
- business impact descriptions
""")

    else:

        st.error("""
Your resume currently lacks several important
technical keywords used in AI/ML hiring.

Recommended next steps:
- add Python projects
- include deployed applications
- strengthen machine learning skills
- add GitHub portfolio links
""")

else:
    st.info("👆 Upload a TXT or PDF resume to begin analysis")
