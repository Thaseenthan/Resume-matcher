# Resume Matcher Web App

This is a **Resume Matcher** web application built using **Streamlit**. The app allows you to upload multiple resumes and a job description, then ranks the resumes based on how closely they match the job description using **TF-IDF** and **cosine similarity**.

---

## Features

- Upload **multiple resumes** (PDF, DOCX, TXT).  
- Paste or type a **Job Description**.  
- Automatically **extracts text** from uploaded resumes.  
- Converts text into **numerical vectors** using **TF-IDF**.  
- Measures **similarity** between Job Description and resumes.  
- Displays **top 5 matching resumes** with similarity scores as **percentages**.

---

## Requirements

Make sure you have **Python 3.7+** installed.  

Install dependencies:

```bash
pip install streamlit scikit-learn PyPDF2 python-docx docx2txt
```
## How to Run

1. Save the main code as resume_matcher.py.

2. Open a terminal and run:
```
streamlit run app.py
```

3. The app will open in your browser.

4. Enter the job description in the text area.

5. Upload resumes (PDF, DOCX, TXT).

6. Click Match Resumes to see the top matching resumes with similarity percentages.

## How It Works

1. Text Extraction

  PDF → PyPDF2

  DOCX → docx2txt

  TXT → standard file reading

2. Vectorization

  Uses TfidfVectorizer to convert the job description and resumes into numerical vectors.

3. Similarity Calculation

  Uses cosine_similarity to compare the job description vector with each resume vector.

  Similarity score is converted into percentage for easy understanding.

4. Ranking

   The top 5 resumes with the highest similarity scores are displayed.

## File Structure
```
resume-matcher/
│
├─ app.py       # Main Streamlit app
├─ README.md              # Project documentation

```

