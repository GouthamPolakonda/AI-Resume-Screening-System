SKILLS = [
    # Programming Languages
    "python", "java", "c", "c++", "c#", ".net", "golang", "rust",
    "swift", "kotlin", "r", "matlab", "perl", "php", "typescript",
    "scala", "ruby",

    # Web Development
    "html", "css", "javascript", "react", "angular", "vue.js",
    "node.js", "express.js", "bootstrap", "tailwind css", "jquery",
    "rest api", "graphql", "flask", "django", "spring", "spring boot",

    # Databases
    "sql", "mysql", "postgresql", "mongodb", "oracle", "sqlite",
    "firebase", "redis", "cassandra", "dynamodb",

    # Version Control & DevOps
    "git", "github", "github actions", "gitlab ci", "docker",
    "kubernetes", "jenkins", "terraform", "ansible", "helm",

    # Cloud Platforms
    "aws", "azure",

    # Operating Systems & Servers
    "linux", "unix", "nginx", "apache",

    # AI / Machine Learning / Data Science
    "machine learning", "deep learning", "nlp", "computer vision",
    "tensorflow", "keras", "pytorch", "opencv", "scikit learn",
    "pandas", "numpy", "scipy", "matplotlib", "seaborn",
    "xgboost", "lightgbm", "langchain", "hugging face",
    "openai", "llm", "generative ai",

    # Big Data
    "hadoop", "spark", "hive", "airflow",

    # Testing
    "selenium", "junit", "testng", "pytest",
    "postman", "cypress", "playwright",

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
    "system design", "microservices",
    "design patterns", "agile", "scrum",

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

def extract_skills(clean_text):
    found_skills = []

    for skill in SKILLS:
        if skill in clean_text:
            found_skills.append(skill.title())
    
    found_skills = list(set(found_skills))
    found_skills.sort()
    return found_skills
