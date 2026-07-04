import os
from werkzeug.utils import secure_filename
from utils.parser import extract_text
from flask import Blueprint
from flask import request

upload_bp = Blueprint("upload", __name__)

@upload_bp.route("/upload", methods=["POST"])
def upload():

    job_title = request.form["job_title"]
    job_description = request.form["job_description"]
    resume = request.files["resume"]

    filename = secure_filename(resume.filename)
    upload_folder = "uploads"
    file_path = os.path.join(upload_folder, filename)
    resume.save(file_path)
    
    print("\n========== JOB TITLE ==========")
    print(job_title)
    print("\n========== JOB DESCRIPTION ==========")
    print(job_description)
    print("\n========== FILE ==========")
    print(resume.filename)

    resume_text = extract_text(file_path)
    print("\n========== RESUME TEXT ==========\n")
    print(resume_text)


    return "Resume uploaded and parsed successfully"