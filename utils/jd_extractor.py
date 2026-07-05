import re
from utils.extractor import SKILLS

def extract_jd_data(job_title, job_description):

    # Company Name
    company_match = re.search(
        r'Company\s*:\s*(.+)',
        job_description,
        re.IGNORECASE
    )

    company = (
        company_match.group(1).strip()
        if company_match
        else "Not Found"
    )

    # Location

    location_match = re.search(
        r'Location\s*:\s*(.+)',
        job_description,
        re.IGNORECASE
    )

    location = (
        location_match.group(1).strip()
        if location_match
        else "Not Found"
    )

    # Employment Type

    employment_match = re.search(
        r'Employment\s*Type\s*:\s*(.+)',
        job_description,
        re.IGNORECASE
    )

    employment_type = (
        employment_match.group(1).strip()
        if employment_match
        else "Not Found"
    )

    # Education Requirement

    education = "Not Mentioned"

    education_keywords = [
        "bachelor",
        "master",
        "b.tech",
        "m.tech",
        "bfa",
        "b.e",
        "bachelor's degree",
        "master's degree",
        "mba",
        "mca"
    ]

    for keyword in education_keywords:
        if keyword.lower() in job_description.lower():
            education = keyword.title()
            break

    # Mandatory Skills

    mandatory_skills = []
    jd_lower = job_description.lower()
    for skill in SKILLS:
        if skill.lower() in jd_lower:
            mandatory_skills.append(skill.title())

    mandatory_skills = sorted(list(set(mandatory_skills)))


    # JD Dictionary

    jd_data = {
        "job_title": job_title,
        "company": company,
        "location": location,
        "employment_type": employment_type,
        "education": education,
        "mandatory_skills": mandatory_skills
    }

    return jd_data



    
    