import re
from utils.extractor import SKILLS

def extract_projects(resume_text):
    projects = []
    
    # Find the Projects section
    project_pattern = re.search(
        r'projects?(.*?)(education|certifications|experience|skills|languages|achievements|$)',         
        resume_text, re.IGNORECASE | re.DOTALL
    )
    if not project_pattern:
        return []
    
    project_text = project_pattern.group(1)
    lines = project_text.split("\n")
    current_project = None
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            continue

        # Ignore headings
        if line.lower().startswith("technologies"):
            continue

        # Detect a new project title
        if (
            not line.startswith("-")
            and not line.startswith("•")
            and len(line) > 3
        ):
            # Save previous project
            if current_project:
                current_project["technologies"] = sorted(
                    list(set(current_project["technologies"]))
                )
                projects.append(current_project)

            current_project = {
                "title": line,
                "technologies": []
            }
            continue

        # Extract technologies used in the project
        if current_project:
            for skill in SKILLS:
                if skill.lower() in line.lower():
                    current_project["technologies"].append(
                        skill.title()
                    )
    
    # Save the last project
    if current_project:
        current_project["technologies"] = sorted(
            list(set(current_project["technologies"]))
        )
        projects.append(current_project)
    return projects
