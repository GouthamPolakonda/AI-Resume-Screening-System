import os

from flask import Blueprint
from flask import request
from werkzeug.utils import secure_filename

from utils.parser import extract_text
from utils.preprocess import preprocess_text
from utils.extractor import extract_skills
from utils.matcher import calculate_similarity

upload_bp = Blueprint("upload", __name__)

@upload_bp.route("/upload", methods=["POST"])
def upload():

    # Get Form Data
    job_title = request.form["job_title"]
    job_description = request.form["job_description"]
    resume = request.files["resume"]

    # Save Uploaded Resume
    filename = secure_filename(resume.filename)
    upload_folder = "uploads"
    file_path = os.path.join(upload_folder, filename)
    resume.save(file_path)

     # Extract Resume Text
    resume_text = extract_text(file_path)

     # Preprocess Text
    clean_text = preprocess_text(resume_text)
    clean_job_description = preprocess_text(job_description)

     # Extract Skills
    skills = extract_skills(clean_text)

    # Calculate Match Score
    match_score = calculate_similarity(
        clean_job_description,
        clean_text
    )

    print("\n JOB TITLE : ")
    print(job_title)

    print("\n JOB DESCRIPTION : ")
    print(job_description)

    print("\n FILE : ")
    print(resume.filename)

    print("\n RAW RESUME TEXT : \n")
    print(resume_text)

    print("\n CLEAN TEXT : \n")
    print(clean_text)

    print("\n EXTRACTED SKILLS : \n")
    print(skills)

    print("\n MATCH SCORE : \n")
    print(f"{match_score}%")
   
    return "Resume uploaded and parsed successfully"