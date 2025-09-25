import streamlit as st
import os
import PyPDF2
import docx2txt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ========= Helper functions =========
def extract_text_from_pdf(file):
    text = ""
    reader = PyPDF2.PdfReader(file)
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    return text

def extract_text_from_docx(file):
    return docx2txt.process(file)

def extract_text_from_txt(file):
    return file.read().decode("utf-8")

def extract_text(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        return extract_text_from_pdf(uploaded_file)
    elif uploaded_file.name.endswith(".docx"):
        return extract_text_from_docx(uploaded_file)
    elif uploaded_file.name.endswith(".txt"):
        return extract_text_from_txt(uploaded_file)
    return ""

# ========= Streamlit UI ==============
st.set_page_config(page_title="Resume Matcher", layout="centered")

st.title("📄 Job Description and Resume Matcher")

job_description = st.text_area("Enter Job Description:", height=200)

uploaded_resumes = st.file_uploader(
    "Upload Resumes (PDF, DOCX, TXT). Upload more than 5 for better results:",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

if st.button("Match Resumes"):
    if not job_description or not uploaded_resumes:
        st.warning("⚠️ Please provide both Job Description and Resumes.")
    else:
        # Extract text from resumes
        resumes_text = []
        resume_names = []
        for resume in uploaded_resumes:
            text = extract_text(resume)
            if text.strip():
                resumes_text.append(text)
                resume_names.append(resume.name)

        if not resumes_text:
            st.error("No valid resume text could be extracted.")
        else:
            # Vectorize JD + resumes
            vectorizer = TfidfVectorizer().fit_transform([job_description] + resumes_text)
            vectors = vectorizer.toarray()
            job_vector = vectors[0]
            resumes_vectors = vectors[1:]

            # Similarity
            similarities = cosine_similarity([job_vector], resumes_vectors)[0]

            # Top 5 matches
            top_indices = similarities.argsort()[-5:][::-1]
            top_resumes = [resume_names[i] for i in top_indices]
            similarity_scores = [round(similarities[i] * 100, 2) for i in top_indices]

            st.success("✅ Top Matching Resumes:")

            for i, (name, score) in enumerate(zip(top_resumes, similarity_scores), 1):
                st.write(f"**{i}. {name}** - Similarity Score: `{score}%`")
