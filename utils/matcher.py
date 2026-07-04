from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(job_description, resume_text):
    documents = [job_description, resume_text]
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]
    score = round(similarity * 100, 2)
    return score