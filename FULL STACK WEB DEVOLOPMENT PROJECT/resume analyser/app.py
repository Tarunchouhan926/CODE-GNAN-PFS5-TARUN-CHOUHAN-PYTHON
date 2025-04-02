from flask import Flask, request, jsonify, render_template
import pdfplumber
import docx
import spacy
import re
import mysql.connector

app = Flask(__name__, static_folder="static")

nlp = spacy.load("en_core_web_sm")

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="resume_analyzer"
)
cursor = db_connection.cursor()

SKILLS_LIST = set([
    # Programming Languages
    "Python", "Java", "C++", "JavaScript", "TypeScript", "C#", "Swift", "Go", "Rust",
    "Ruby", "PHP", "Kotlin", "Dart", "Scala", "Perl", "R", "Objective-C", "Haskell", "Lua", "Shell Scripting",
    
    # Frontend Development
    "HTML", "CSS", "Sass", "Less", "JavaScript", "TypeScript", "React", "Vue.js", "Angular", "Svelte",
    "Next.js", "Nuxt.js", "Gatsby", "Bootstrap", "Tailwind CSS", "Material UI", "Chakra UI", "jQuery",
    
    # Backend Development
    "Node.js", "Express.js", "NestJS", "Django", "Flask", "FastAPI", "Spring Boot", "Ruby on Rails",
    "ASP.NET Core", "Laravel", "Phoenix (Elixir)", "Go Fiber", "Koa.js", "Actix (Rust)",
    
    # Databases (SQL & NoSQL)
    "MySQL", "PostgreSQL", "SQLite", "MariaDB", "Microsoft SQL Server", "Oracle Database",
    "MongoDB", "Firebase Firestore", "Cassandra", "CouchDB", "DynamoDB", "Redis", "Neo4j", "InfluxDB",
    
    # DevOps & Cloud
    "Docker", "Kubernetes", "Terraform", "Ansible", "Jenkins", "GitHub Actions", "CircleCI",
    "AWS", "Azure", "Google Cloud Platform", "Heroku", "Vercel", "Netlify", "DigitalOcean", "Cloudflare",
    
    # API & Microservices
    "GraphQL", "REST API", "gRPC", "WebSockets", "Kafka", "RabbitMQ", "NATS Streaming", "Redis Streams",
    
    # Data Science & AI
    "Machine Learning", "Data Science", "Deep Learning", "TensorFlow", "Keras", "PyTorch", "OpenCV",
    "Pandas", "NumPy", "Scikit-Learn", "Matplotlib", "Seaborn", "Hugging Face Transformers",
    
    # Big Data & Analytics
    "Apache Hadoop", "Apache Spark", "Apache Flink", "Apache Kafka", "Snowflake", "Google BigQuery",
    "ClickHouse", "Dask", "Presto", "Redshift", "Elasticsearch", "Grafana", "Tableau", "Power BI",
    
    # Mobile Development
    "React Native", "Flutter", "Swift", "Kotlin", "Xamarin", "Ionic", "Cordova", "Unity", "Unreal Engine",
    
    # Blockchain & Web3
    "Solidity", "Ethereum", "Web3.js", "Hardhat", "Truffle", "IPFS", "Polkadot", "Rust (Solana)",
    
    # Cybersecurity
    "OWASP", "Burp Suite", "Metasploit", "Wireshark", "Snort", "Suricata", "Nmap", "Splunk", "SIEM",
    
    # Testing & Automation
    "Selenium", "Cypress", "Playwright", "Jest", "Mocha", "Chai", "PyTest", "JUnit", "TestNG", "Cucumber",
    
    # Miscellaneous
    "Git", "GitHub", "GitLab", "Bitbucket", "Linux", "Bash", "PowerShell", "WebAssembly (WASM)",
    "Figma", "Adobe XD", "Postman", "Swagger", "Insomnia", "Vim", "Emacs", "VS Code", "JetBrains IntelliJ"
])
len(SKILLS_LIST)  


def extract_text(file):
    text = ""
    if file.filename.endswith('.pdf'):
        with pdfplumber.open(file) as pdf:
            text = "\n".join([page.extract_text() or "" for page in pdf.pages])
    elif file.filename.endswith('.docx'):
        doc = docx.Document(file)
        text = "\n".join([para.text for para in doc.paragraphs])
    return text.strip()


def extract_skills(text):
    return list(set(token.text for token in nlp(text) if token.text in SKILLS_LIST))


def extract_personal_details(text):
    cgpa = re.search(r"CGPA:?[\s:]*(\d+\.\d+)", text)
    education = re.search(r"(?:Education|Degree):?\s*([A-Za-z\s,]+)", text)
    
    return {
        "cgpa": float(cgpa.group(1)) if cgpa else 0.0,
        "education_details": education.group(1).strip() if education else "Not Found"
    }


def calculate_ats_score(job_skills, resume_skills):
    matched_skills = set(job_skills) & set(resume_skills)
    score = (len(matched_skills) / len(job_skills)) * 100 if job_skills else 0
    return round(score, 2), matched_skills


def store_candidate_info(cgpa, education_details, ats_score):
    query = """
    INSERT INTO candidates (cgpa, education_details, ats_score)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (cgpa, education_details, ats_score))
    db_connection.commit()



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_resume():
    if 'resume' not in request.files or 'job_description' not in request.form:
        return jsonify({'error': 'Missing file or job description'})

    file = request.files['resume']
    job_description = request.form['job_description']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    resume_text = extract_text(file)
    job_skills = extract_skills(job_description)
    resume_skills = extract_skills(resume_text)
    personal_details = extract_personal_details(resume_text)

    ats_score, matched_skills = calculate_ats_score(job_skills, resume_skills)
    missing_skills = set(job_skills) - set(resume_skills)

    store_candidate_info(
        personal_details["cgpa"], personal_details["education_details"], ats_score
    )

    return jsonify({
        "ats_score": ats_score,
        "matched_skills": list(matched_skills),
        "missing_skills": list(missing_skills),
        "job_fit": "Good fit!" if ats_score > 70 else "Needs improvement.",
        **personal_details
    })


if __name__ == '__main__':
    app.run(debug=True)
