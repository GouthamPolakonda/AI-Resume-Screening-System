import re

def extract_certifications(resume_text):
    certifications = []
    certification_pattern = re.search(
        r'certifications?(.*?)(projects|education|experience|skills|languages|achievements|$)',
        resume_text,
        re.IGNORECASE | re.DOTALL
    )
    if not certification_pattern:
        return []

    certification_text = certification_pattern.group(1)
    lines = certification_text.split("\n")

    for line in lines:
        line = line.strip()
        if len(line) == 0:
            continue
        line = line.lstrip("-•*").strip()
        if "-" in line:
            parts = line.split("-", 1)
            certifications.append({
                "name": parts[0].strip(),
                "provider": parts[1].strip()
            })
        else:
            certifications.append({
                "name": line,
                "provider": "Unknown"
            })
    return certifications