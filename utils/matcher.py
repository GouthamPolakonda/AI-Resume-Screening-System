from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Calculate Cosine Similarity Score

def calculate_similarity(job_description, resume_text):
    documents = [job_description, resume_text]
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]
    score = round(similarity * 100, 2)
    return score

# Calculating Resume Score

def calculate_resume_score(resume_data, jd_data, tfidf_score):
    
    # Resume skills
    resume_skills = set(
        skill.lower()
        for skill in resume_data["skills"]
    )

    # Job Description Skills
    jd_skills = set(
        skill.lower()
        for skill in jd_data["mandatory_skills"]
    )

    matched_skills = resume_skills.intersection(jd_skills)
    missing_skills = jd_skills.difference(resume_skills)

    # Skill score
    if len(jd_skills) > 0:
        skill_score = (
            len(matched_skills)
            /
            len(jd_skills)
        ) * 100
    else:
        skill_score = 0

    # Education Score
    education_score = 100
    resume_degree = resume_data["education"]["degree"]
    jd_degree = jd_data["education"]
    if jd_degree != "Not Mentioned":
        if resume_degree == "Not Found":
            education_score = 0

    # Final ATS Score
    final_score = (
        (skill_score * 0.70) + (education_score * 0.10) + (tfidf_score * 0.20)
    )

    return {
        "overall_score": round(final_score,2),
        "skill_score": round(skill_score,2),
        "education_score": education_score,
        "matched_skills": sorted(matched_skills),
        "missing_skills": sorted(missing_skills),
    }
