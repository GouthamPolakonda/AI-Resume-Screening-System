from spacy.matcher import PhraseMatcher
import spacy
import re

nlp = spacy.load("en_core_web_sm")

SKILLS = [
    # Programming Languages
    "python", "java", "c", "c++", "c#", ".net", "golang", "rust",
    "swift", "kotlin", "r", "matlab", "perl", "php", "typescript",
    "scala", "ruby","core java", "advanced java", "exception handling", 
    "multithreading", "jdbc", "collections framework", "generics", "java streams", "lambda expressions",

    # Web Development
    "html", "css", "javascript", "react", "angular", "vue.js",
    "node.js", "express.js", "bootstrap", "tailwind css", "jquery",
    "rest api", "graphql", "flask", "django", "spring", "spring boot","spring mvc",
    "spring security", "spring data jpa", "hibernate", "jpa",

    # Databases
    "sql", "mysql", "postgresql", "mongodb", "oracle", "sqlite",
    "firebase", "redis", "cassandra", "dynamodb", "pl/sql", "sql server",


    # Version Control & DevOps
    "git", "github", "github actions", "gitlab ci", "docker",
    "kubernetes", "jenkins", "terraform", "ansible", "helm", "intellij",
    "intellij idea", "eclipse", "vs code", "visual studio code", "jupyter notebook", 
    "mysql workbench", "maven", "gradle",

    # Cloud Platforms
    "aws", "azure",

    # Operating Systems & Servers
    "linux", "unix", "nginx", "apache",

    # AI / Machine Learning / Data Science
    "machine learning", "deep learning", "nlp", "computer vision",
    "tensorflow", "keras", "pytorch", "opencv", "scikit learn",
    "pandas", "numpy", "scipy", "matplotlib", "seaborn",
    "xgboost", "lightgbm", "langchain", "hugging face",
    "openai", "llm", "generative ai", "feature engineering", "data preprocessing",

    # Big Data
    "hadoop", "spark", "hive", "airflow",

    # Testing
    "selenium", "junit", "testng", "pytest",
    "postman", "cypress", "playwright", "mockito",

    # Mobile Development
    "android", "ios", "flutter", "react native", "xamarin",

    # Cybersecurity
    "ethical hacking", "penetration testing", "wireshark",
    "metasploit", "burp suite", "network security",
    "cryptography", "firewall",

    # Networking
    "tcp/ip", "dns", "http", "https", "vpn",
    "routing", "switching",

    # Data Analytics & BI
    "data analysis", "data visualization", "statistics",
    "power bi", "tableau", "excel", "dax",
    "power query", "etl", "ssis",

    # Computer Science Fundamentals
    "data structures", "algorithms", "oop",
    "operating systems", "computer networks", "dbms",
    "system design", "microservices", "design patterns", 
    "agile", "scrum", "software engineering",
    "computer organization", "compiler design", "distributed systems",

    # Soft Skills
    "communication", "verbal communication",
    "written communication", "presentation skills",
    "teamwork", "leadership", "problem solving",
    "critical thinking", "analytical thinking",
    "time management", "adaptability", "creativity",
    "decision making", "negotiation",
    "customer service", "customer relationship management",
    "attention to detail", "organizational skills",
    "multitasking", "conflict resolution",
    "interpersonal skills", "active listening",
    "public speaking", "project management",
    "stakeholder management",

    # Human Resources
    "recruitment", "talent acquisition",
    "employee engagement", "payroll",
    "performance management", "hr analytics",
    "onboarding", "employee relations",
    "training and development",

    # Sales
    "sales", "business development",
    "lead generation", "cold calling",
    "crm", "salesforce",
    "account management", "inside sales",
    "outside sales", "upselling", "cross selling",

    # Marketing
    "digital marketing", "seo", "sem",
    "social media marketing", "content marketing",
    "email marketing", "google analytics",
    "google ads", "facebook ads",
    "branding", "market research",

    # Finance & Accounting
    "financial analysis", "bookkeeping",
    "taxation", "tally", "sap fico",
    "quickbooks", "budgeting",
    "forecasting", "accounts payable",
    "accounts receivable",

    # Customer Support
    "technical support", "customer support",
    "help desk", "ticketing",
    "service now", "zendesk", "freshdesk",

    # Productivity Tools
    "microsoft office", "word",
    "powerpoint", "outlook",
    "google workspace", "google sheets",
    "google docs"
]

SKILL_ALIASES = {
    "core java": "Java",
    "advanced java": "Java",
    "java se": "Java",
    "oops": "OOP",
    "object oriented programming": "OOP",
    "mysql database": "MySQL",
    "js": "JavaScript",
    "ml": "Machine Learning",
    "ai": "Artificial Intelligence"
}

matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
patterns = [nlp.make_doc(skill) for skill in SKILLS]
matcher.add("SKILLS", patterns)

# Extract Skills

def extract_skills(clean_text):
    doc = nlp(clean_text)
    matches = matcher(doc)
    skills = set()

    for match_id, start, end in matches:
        skill = doc[start:end].text
        normalized = SKILL_ALIASES.get(
            skill.lower(),
            skill.title()
        )
        skills.add(normalized)
    return sorted(skills)

def categorize_skills(skills):
    categories = {
        "Programming": [],
        "Web": [],
        "Database": [],
        "AI": [],
        "Tools": [],
        "Soft Skills": []
    }
    return categories

# Extract Text

def extract_email(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(pattern, text)
    if emails:
        return emails[0]
    return "Not Found"

# Extract Phone Number

def extract_phone(text):
    pattern = r'(?:\+91[\-\s]?)?[6-9]\d{9}'
    match = re.search(pattern, text)
    if match:
        return match.group()
    return "Not Found"

# Extract Names

def extract_name(text):
    lines = text.split("\n")
    for line in lines:
        line = line.strip()
        if len(line) > 2:
            return line
    return "Not Found"

# Extract Education

def extract_education(text):
    education = {
        "degree": "Not Found",
        "cgpa": None
    }
    degree_patterns = [
        "Bachelor of Technology",
        "Bachelor of Engineering",
        "B.Tech",
        "B.E",
        "Bachelor",
        "Master of Technology",
        "Master of Engineering",
        "M.Tech",
        "M.E",
        "Master"
    ]
    text_lower = text.lower()
    for degree in degree_patterns:
        if degree.lower() in text_lower:
            education["degree"] = degree
            break
    
    cgpa_match = re.search(
        r'(?:cgpa|gpa)\s*[:\-]?\s*(\d+(\.\d+)?)',
        text,
        re.IGNORECASE
    )

    if cgpa_match:
        education["cgpa"] = float(cgpa_match.group(1))
    return education

# Extract Resume Data

def extract_resume_data(resume_text, clean_text):
    resume_data = {
        "name": extract_name(resume_text),
        "email": extract_email(resume_text),
        "phone": extract_phone(resume_text),
        "skills": extract_skills(clean_text),
        "education": extract_education(resume_text),
         "categorized_skills": categorize_skills(extract_skills(clean_text))
    }
    return resume_data
