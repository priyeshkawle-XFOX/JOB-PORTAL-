import streamlit as st
import pandas as pd
import io
import re
import requests
import json
import docx2txt
import PyPDF2
import os
import base64
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np


def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def Hire_IQ_app():
    load_css("style.css")

# --- Authentication Functions ---

def init_user_db():
    """
    Initialize a mock database of users if it doesn't exist.
    In a real app, this would connect to SQL/Firebase.
    """
    if 'users_db' not in st.session_state:
        # Default admin user (Username: admin, Password: 123)
        st.session_state['users_db'] = {"admin": "123"}

def show_login_page():
    """Displays a Futuristic Cyberpunk-style Login Page"""
    
    # --- FUTURISTIC CSS STYLING ---
    st.markdown("""
    <style>
        /* 1. Futuristic Background */
        .stApp {
            background-color: #050505;
            background-image: 
                radial-gradient(circle at 50% 50%, #111827 0%, #000000 90%),
                linear-gradient(0deg, rgba(59,130,246,0.1) 1px, transparent 1px),
                linear-gradient(90deg, rgba(59,130,246,0.1) 1px, transparent 1px);
            background-size: 100% 100%, 40px 40px, 40px 40px;
        }

        /* 2. Neon Card Styling (Form) */
        [data-testid="stForm"] {
            background: rgba(20, 25, 40, 0.7);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(59, 130, 246, 0.3);
            border-radius: 15px;
            box-shadow: 0 0 20px rgba(59, 130, 246, 0.2), inset 0 0 10px rgba(59, 130, 246, 0.1);
            padding: 40px;
        }

        /* 3. Neon Title Text */
        .neon-title {
            font-family: 'Inter', sans-serif;
            font-weight: 800;
            font-size: 3.5rem !important;
            text-align: center;
            background: linear-gradient(90deg, #00c6ff, #0072ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 20px rgba(0, 198, 255, 0.5);
            margin-bottom: 0;
        }
        
        .neon-subtitle {
            color: #a1a1aa;
            text-align: center;
            letter-spacing: 2px;
            font-size: 0.9rem;
            margin-bottom: 30px;
            text-transform: uppercase;
        }

        /* 4. Input Fields (Dark Tech Look) */
        .stTextInput > div > div > input {
            background-color: #0a0a0c !important;
            color: #00f2ff !important;
            border: 1px solid #333;
            border-radius: 8px;
            height: 50px;
            transition: all 0.3s ease;
        }
        .stTextInput > div > div > input:focus {
            border-color: #00c6ff;
            box-shadow: 0 0 10px rgba(0, 198, 255, 0.5);
        }

        /* 5. Futuristic Button */
        div.stButton > button {
            background: linear-gradient(90deg, #00c6ff 0%, #0072ff 100%);
            color: white;
            font-weight: bold;
            border: none;
            border-radius: 8px;
            padding: 12px 0;
            width: 100%;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: all 0.3s ease;
            box-shadow: 0 0 15px rgba(0, 114, 255, 0.4);
        }
        div.stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 0 25px rgba(0, 114, 255, 0.7);
        }

        /* 6. Tabs Styling */
        button[data-baseweb="tab"] {
            color: #64748b;
            font-weight: 600;
        }
        button[data-baseweb="tab"][aria-selected="true"] {
            color: #00c6ff !important;
            background-color: transparent !important;
            border-bottom: 2px solid #00c6ff !important;
        }
    </style>
    """, unsafe_allow_html=True)

    # Layout: Center Column
    col1, col2, col3 = st.columns([1, 1.5, 1])

    with col2:
        st.markdown("<div style='margin-top: 80px;'></div>", unsafe_allow_html=True)
        st.markdown("<h1 class='neon-title'>HIRE IQ</h1>", unsafe_allow_html=True)
        st.markdown("<p class='neon-subtitle'>Next Gen Career Intelligence</p>", unsafe_allow_html=True)
        
        tab_login, tab_signup = st.tabs(["ACCESS PORTAL", "NEW USER"])

        # --- LOGIN LOGIC ---
        with tab_login:
            with st.form("login_form"):
                username = st.text_input("IDENTITY", placeholder="Username")
                password = st.text_input("ACCESS CODE", type="password", placeholder="Password")
                
                st.markdown("<br>", unsafe_allow_html=True)
                submit_login = st.form_submit_button("INITIALIZE SESSION")

                if submit_login:
                    if not username or not password:
                        st.warning("⚠️ Credentials Missing")
                    elif username in st.session_state['users_db']:
                        if st.session_state['users_db'][username] == password:
                            st.session_state['authenticated'] = True
                            st.session_state['username'] = username
                            st.success("✅ Access Granted")
                            st.rerun()
                        else:
                            st.error("❌ Access Denied: Invalid Code")
                    else:
                        st.error("❌ Identity Not Found")

        # --- SIGNUP LOGIC ---
        with tab_signup:
            with st.form("signup_form"):
                new_user = st.text_input("SET IDENTITY")
                new_pass = st.text_input("SET ACCESS CODE", type="password")
                confirm_pass = st.text_input("CONFIRM CODE", type="password")
                
                st.markdown("<br>", unsafe_allow_html=True)
                submit_signup = st.form_submit_button("CREATE IDENTITY")

                if submit_signup:
                    if not new_user or not new_pass:
                        st.error("⚠️ Fields Required")
                    elif new_pass != confirm_pass:
                        st.error("⚠️ Code Mismatch")
                    elif new_user in st.session_state['users_db']:
                        st.error("⚠️ Identity Already Exists")
                    else:
                        st.session_state['users_db'][new_user] = new_pass
                        st.success("✅ Identity Created. Proceed to Access.")

def Hire_IQ_app():
    """
    This function contains the entire HireIQ application.
    """
    # NOTE: set_page_config is called in main(), so we don't need it here again.
    # st.set_page_config(page_title="HireIQ", page_icon="💼", layout="wide")

    # Custom CSS for better styling
    st.markdown("""
    <style>
        .main {padding: 1rem;}
        .stTabs [data-baseweb="tab-list"] {gap: 10px;}
        .stTabs [data-baseweb="tab"] {height: 50px; white-space: pre-wrap; border-radius: 4px; padding: 10px 16px; background-color: #f0f2f6;}
        .stTabs [aria-selected="true"] {background-color: #4e89ae !important; color: white !important;}
        h1, h2, h3 {color: #1e3d59;}
        .stButton>button {background-color: #4e89ae; color: white; border-radius: 4px; padding: 10px 24px; border: none;}
        .stButton>button:hover {background-color: #1e3d59;}
        .card {background-color: white; border-radius: 8px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px;}
    </style>
    """, unsafe_allow_html=True)

    # Initialize session state variables
    if 'resume_data' not in st.session_state:
        st.session_state.resume_data = None
    if 'extracted_skills' not in st.session_state:
        st.session_state.extracted_skills = []
    if 'job_recommendations' not in st.session_state:
        st.session_state.job_recommendations = []
    if 'career_advice' not in st.session_state:
        st.session_state.career_advice = None

    # Function to extract text from PDF files
    def extract_text_from_pdf(pdf_file):
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text

    # Function to extract text from DOCX files
    def extract_text_from_docx(docx_file):
        text = docx2txt.process(docx_file)
        return text

    # Function to extract skills from resume text
    def extract_skills(resume_text):
        # Common skills to look for (this could be expanded)
        common_skills = [
            # Programming Languages
            "Python", "Java", "JavaScript", "C++", "C#", "Ruby", "PHP", "Swift", "Kotlin", "Go", "Rust",
            "TypeScript", "SQL", "HTML", "CSS", "R", "Scala", "Perl", "Shell", "Bash", "PowerShell",
            
            # Frameworks & Libraries
            "React", "Angular", "Vue", "Django", "Flask", "Spring", "ASP.NET", "Express", "Node.js",
            "TensorFlow", "PyTorch", "Keras", "Pandas", "NumPy", "Scikit-learn", "jQuery", "Bootstrap",
            
            # Cloud & DevOps
            "AWS", "Azure", "GCP", "Docker", "Kubernetes", "Jenkins", "Git", "CI/CD", "Terraform",
            "Ansible", "Puppet", "Chef", "Prometheus", "Grafana", "ELK Stack",
            
            # Databases
            "MySQL", "PostgreSQL", "MongoDB", "Oracle", "SQL Server", "SQLite", "Redis", "Cassandra",
            "DynamoDB", "Elasticsearch", "Neo4j", "Firebase",
            
            # Mobile Development
            "Android", "iOS", "React Native", "Flutter", "Xamarin", "Ionic", "SwiftUI", "Kotlin Multiplatform",
            
            # Web Development
            "RESTful API", "GraphQL", "WebSockets", "Progressive Web Apps", "SPA", "SSR", "JAMstack",
            "Webpack", "Babel", "Sass", "Less", "Tailwind CSS",
            
            # Data Science & AI
            "Machine Learning", "Deep Learning", "NLP", "Computer Vision", "Data Analysis", "Data Visualization",
            "Big Data", "Hadoop", "Spark", "Statistical Analysis", "A/B Testing", "Data Mining",
            
            # Project Management & Methodologies
            "Agile", "Scrum", "Kanban", "Waterfall", "Lean", "Six Sigma", "PRINCE2", "PMP", "JIRA",
            "Confluence", "Trello", "Asana", "MS Project",
            
            # Soft Skills
            "Communication", "Leadership", "Teamwork", "Problem Solving", "Critical Thinking", "Time Management",
            "Adaptability", "Creativity", "Emotional Intelligence", "Negotiation", "Conflict Resolution",
            
            # Design
            "UI/UX", "Figma", "Sketch", "Adobe XD", "Photoshop", "Illustrator", "InDesign", "After Effects",
            "Premiere Pro", "3D Modeling", "Animation",
            
            # Testing & QA
            "Unit Testing", "Integration Testing", "E2E Testing", "TDD", "BDD", "Selenium", "JUnit",
            "TestNG", "Mocha", "Jest", "Cypress", "Postman", "SoapUI",
            
            # Security
            "Cybersecurity", "Penetration Testing", "Ethical Hacking", "OWASP", "Encryption", "Authentication",
            "Authorization", "OAuth", "JWT", "SSO", "GDPR Compliance",
            
            # Business & Analytics
            "Business Intelligence", "Tableau", "Power BI", "Google Analytics", "SEO", "SEM", "CRM",
            "ERP", "Salesforce", "SAP", "Microsoft Dynamics", "Excel", "VBA",
            
            # Other Technical Skills
            "Microservices", "Serverless", "Blockchain", "IoT", "AR/VR", "Game Development", "Unity",
            "Unreal Engine", "Embedded Systems", "Networking", "Linux", "Windows Server"
        ]
        
        # Extract skills from resume text
        found_skills = []
        for skill in common_skills:
            # Use regex with word boundaries to find whole words only
            pattern = r'\b' + re.escape(skill) + r'\b'
            if re.search(pattern, resume_text, re.IGNORECASE):
                found_skills.append(skill)
        
        # Extract years of experience using regex patterns
        experience_patterns = [
            r'(\d+)\+?\s+years?\s+of\s+experience',
            r'experience\s+of\s+(\d+)\+?\s+years?',
            r'(\d+)\+?\s+years?\s+experience',
            r'experienced\s+(?:for|with)\s+(\d+)\+?\s+years?'
        ]
        
        years_of_experience = []
        for pattern in experience_patterns:
            matches = re.findall(pattern, resume_text, re.IGNORECASE)
            years_of_experience.extend([int(year) for year in matches])
        
        # Store years of experience in session state if found
        if years_of_experience:
            st.session_state.years_of_experience = max(years_of_experience)
        else:
            st.session_state.years_of_experience = None
        
        # Extract education information
        education_patterns = [
            r'(?:Bachelor|BS|B\.S\.|BA|B\.A\.)\s+(?:of|in)\s+([^,\.]+)',
            r'(?:Master|MS|M\.S\.|MA|M\.A\.|MBA|M\.B\.A\.)\s+(?:of|in)\s+([^,\.]+)',
            r'(?:Doctor|PhD|Ph\.D\.|Doctorate)\s+(?:of|in)\s+([^,\.]+)'
        ]
        
        education = []
        for pattern in education_patterns:
            matches = re.findall(pattern, resume_text, re.IGNORECASE)
            education.extend(matches)
        
        # Store education in session state if found
        if education:
            st.session_state.education = education
        else:
            st.session_state.education = []
        
        return found_skills

    # Function to analyze resume and provide feedback
    def analyze_resume(resume_text, skills):
        # Comprehensive resume analysis based on extracted skills and other information
        feedback = []
        strengths = []
        areas_for_improvement = []
        
        # Check the number of skills
        if len(skills) < 5:
            areas_for_improvement.append("Consider adding more skills to your resume to increase your chances of getting noticed.")
        elif len(skills) > 15:
            strengths.append("You have a good number of skills listed. Make sure they're all relevant to your target positions.")
        
        # Check for programming languages
        programming_languages = ["Python", "Java", "JavaScript", "C++", "C#", "Ruby", "PHP", "Swift", "Kotlin", "Go", "Rust", "TypeScript"]
        has_programming = any(lang in skills for lang in programming_languages)
        
        if not has_programming and "developer" in resume_text.lower():
            areas_for_improvement.append("Consider adding specific programming languages to your resume if you're targeting developer roles.")
        
        # Check for frameworks
        frameworks = ["React", "Angular", "Vue", "Django", "Flask", "Spring", "ASP.NET", "Express", "Node.js", "TensorFlow", "PyTorch"]
        has_frameworks = any(framework in skills for framework in frameworks)
        
        if has_programming and not has_frameworks:
            areas_for_improvement.append("Consider adding frameworks and libraries related to your programming languages.")
        elif has_programming and has_frameworks:
            strengths.append("Great job including both programming languages and frameworks in your resume.")
        
        # Check for soft skills
        soft_skills = ["Communication", "Leadership", "Teamwork", "Problem Solving", "Critical Thinking", "Time Management", "Adaptability"]
        has_soft_skills = any(skill in skills for skill in soft_skills)
        
        if not has_soft_skills:
            areas_for_improvement.append("Consider adding soft skills to your resume to showcase your well-roundedness.")
        else:
            strengths.append("Good inclusion of soft skills, which are highly valued by employers.")
        
        # Check resume length based on word count
        word_count = len(resume_text.split())
        if word_count < 300:
            areas_for_improvement.append("Your resume seems quite short. Consider adding more details about your experience and achievements.")
        elif word_count > 1000:
            areas_for_improvement.append("Your resume is quite lengthy. Consider condensing it to highlight the most relevant information.")
        else:
            strengths.append("Your resume has a good length, making it easy for recruiters to review.")
        
        # Check for years of experience
        if hasattr(st.session_state, 'years_of_experience') and st.session_state.years_of_experience:
            years = st.session_state.years_of_experience
            if years < 2:
                feedback.append(f"You have {years} year{'s' if years > 1 else ''} of experience. Consider highlighting internships or projects to strengthen your application.")
            elif years >= 2 and years < 5:
                strengths.append(f"You have {years} years of experience, which is valuable for mid-level positions.")
            else:
                strengths.append(f"Your {years} years of experience is a significant strength for senior-level positions.")
        else:
            areas_for_improvement.append("Consider clearly mentioning your years of experience in your resume.")
        
        # Check for education
        if hasattr(st.session_state, 'education') and st.session_state.education:
            degrees = st.session_state.education
            strengths.append(f"Your education in {', '.join(degrees)} is well highlighted.")
        else:
            areas_for_improvement.append("Consider clearly mentioning your educational background in your resume.")
        
        # Check for action verbs
        action_verbs = ["achieved", "improved", "led", "developed", "created", "implemented", "managed", "designed", "launched", "increased"]
        action_verb_count = sum(1 for verb in action_verbs if re.search(r'\b' + re.escape(verb) + r'\b', resume_text, re.IGNORECASE))
        
        if action_verb_count < 3:
            areas_for_improvement.append("Use more action verbs (like 'achieved', 'improved', 'developed') to describe your accomplishments.")
        else:
            strengths.append("Good use of action verbs to describe your accomplishments.")
        
        # Check for quantifiable achievements
        quantifiable_patterns = [r'\b\d+%\b', r'\bincreased\s+by\s+\d+\b', r'\bdecreased\s+by\s+\d+\b', r'\bimproved\s+by\s+\d+\b']
        has_quantifiable = any(re.search(pattern, resume_text, re.IGNORECASE) for pattern in quantifiable_patterns)
        
        if not has_quantifiable:
            areas_for_improvement.append("Consider adding quantifiable achievements (e.g., 'increased efficiency by 20%') to strengthen your resume.")
        else:
            strengths.append("Excellent use of quantifiable achievements to demonstrate your impact.")
        
        # Combine strengths and areas for improvement
        for strength in strengths:
            feedback.append(f"✅ Strength: {strength}")
        
        for area in areas_for_improvement:
            feedback.append(f"🔸 Improvement: {area}")
        
        # If no feedback generated, provide positive feedback
        if not feedback:
            feedback.append("Your resume looks good! It has a good balance of technical and soft skills.")
        
        # Add a summary score
        score = min(100, 50 + 10 * len(strengths) - 5 * len(areas_for_improvement))
        feedback.insert(0, f"📊 Resume Score: {score}/100")
        
        return feedback

    # Function to search for jobs based on skills
    def search_jobs(skills, location="", num_results=5, salary_range=None, date_filter="Any time", company_filter="Any size"):
        # This is a mock function that would normally call a job API like Adzuna
        # For demonstration purposes, we'll return mock data
        mock_jobs = [
            {
                "title": "Senior Python Developer",
                "company": "Tech Innovations Inc.",
                "location": "New York, NY",
                "description": "Looking for an experienced Python developer with knowledge of Django and Flask frameworks. You'll be working on our core product, building new features and maintaining existing ones. Ideal candidates have 5+ years of experience with Python and web development.",
                "skills_match": ["Python", "Django", "Flask", "SQL", "Git", "RESTful API"],
                "url": "https://example.com/job1",
                "salary": "$120,000 - $150,000",
                "date_posted": "2023-06-01",
                "job_type": "Full-time",
                "experience_level": "Senior"
            },
            {
                "title": "Frontend React Developer",
                "company": "WebSolutions Ltd.",
                "location": "Remote",
                "description": "Join our team to build responsive and interactive web applications using React and TypeScript. You'll collaborate with designers and backend developers to create seamless user experiences. We're looking for someone with a strong portfolio and attention to detail.",
                "skills_match": ["JavaScript", "React", "TypeScript", "HTML", "CSS", "Redux", "Webpack"],
                "url": "https://example.com/job2",
                "salary": "$90,000 - $120,000",
                "date_posted": "2023-06-05",
                "job_type": "Full-time",
                "experience_level": "Mid-level"
            },
            {
                "title": "Data Scientist",
                "company": "DataMinds Analytics",
                "location": "San Francisco, CA",
                "description": "Seeking a data scientist with strong skills in Python, machine learning, and data visualization. You'll work on projects involving predictive modeling, natural language processing, and recommendation systems. Experience with big data technologies is a plus.",
                "skills_match": ["Python", "Machine Learning", "Data Analysis", "Data Visualization", "SQL", "TensorFlow", "Pandas", "NumPy"],
                "url": "https://example.com/job3",
                "salary": "$130,000 - $160,000",
                "date_posted": "2023-06-10",
                "job_type": "Full-time",
                "experience_level": "Mid-level to Senior"
            },
            {
                "title": "DevOps Engineer",
                "company": "CloudNative Systems",
                "location": "Austin, TX",
                "description": "Join our team to build and maintain our cloud infrastructure using AWS, Docker, and Kubernetes. You'll be responsible for CI/CD pipelines, infrastructure as code, and ensuring high availability of our services. Experience with monitoring and security is highly valued.",
                "skills_match": ["AWS", "Docker", "Kubernetes", "CI/CD", "Terraform", "Linux", "Jenkins", "Prometheus"],
                "url": "https://example.com/job4",
                "salary": "$110,000 - $140,000",
                "date_posted": "2023-06-12",
                "job_type": "Full-time",
                "experience_level": "Mid-level"
            },
            {
                "title": "Full Stack Developer",
                "company": "Omnipresent Technologies",
                "location": "Chicago, IL",
                "description": "Looking for a full stack developer with experience in React, Node.js, and MongoDB. You'll work on all aspects of our web application, from database design to frontend implementation. We value problem-solving skills and the ability to learn quickly.",
                "skills_match": ["JavaScript", "React", "Node.js", "Express", "MongoDB", "HTML", "CSS", "RESTful API", "Git"],
                "url": "https://example.com/job5",
                "salary": "$100,000 - $130,000",
                "date_posted": "2023-06-15",
                "job_type": "Full-time",
                "experience_level": "Mid-level"
            },
            {
                "title": "Machine Learning Engineer",
                "company": "AI Innovations",
                "location": "Seattle, WA",
                "description": "Join our team to develop cutting-edge machine learning models for real-world applications. You'll work on computer vision, natural language processing, and reinforcement learning projects. Strong mathematical background and experience with deep learning frameworks required.",
                "skills_match": ["Python", "TensorFlow", "PyTorch", "Machine Learning", "Deep Learning", "NLP", "Computer Vision", "Data Analysis"],
                "url": "https://example.com/job6",
                "salary": "$140,000 - $170,000",
                "date_posted": "2023-06-18",
                "job_type": "Full-time",
                "experience_level": "Senior"
            },
            {
                "title": "UI/UX Designer",
                "company": "Creative Designs Inc.",
                "location": "Los Angeles, CA",
                "description": "Looking for a talented UI/UX designer with experience in Figma and Adobe Creative Suite. You'll create user-centered designs for web and mobile applications, conduct user research, and collaborate with developers to implement your designs.",
                "skills_match": ["UI/UX", "Figma", "Adobe XD", "Photoshop", "Illustrator", "User Research", "Wireframing", "Prototyping"],
                "url": "https://example.com/job7",
                "salary": "$90,000 - $120,000",
                "date_posted": "2023-06-20",
                "job_type": "Full-time",
                "experience_level": "Mid-level"
            },
            {
                "title": "Cybersecurity Analyst",
                "company": "SecureNet Solutions",
                "location": "Washington, DC",
                "description": "Join our team to protect our systems and data from cyber threats. You'll conduct security assessments, implement security measures, and respond to incidents. Knowledge of network security, encryption, and authentication protocols is essential.",
                "skills_match": ["Cybersecurity", "Penetration Testing", "OWASP", "Encryption", "Authentication", "Network Security", "Incident Response"],
                "url": "https://example.com/job8",
                "salary": "$110,000 - $140,000",
                "date_posted": "2023-06-22",
                "job_type": "Full-time",
                "experience_level": "Mid-level to Senior"
            },
            {
                "title": "Mobile App Developer",
                "company": "AppWorks Mobile",
                "location": "Boston, MA",
                "description": "Seeking a mobile app developer with experience in React Native or Flutter. You'll build cross-platform mobile applications with a focus on performance and user experience. Experience with native development (iOS/Android) is a plus.",
                "skills_match": ["React Native", "Flutter", "JavaScript", "Mobile Development", "iOS", "Android", "RESTful API", "Git"],
                "url": "https://example.com/job9",
                "salary": "$100,000 - $130,000",
                "date_posted": "2023-06-25",
                "job_type": "Full-time",
                "experience_level": "Mid-level"
            },
            {
                "title": "Database Administrator",
                "company": "DataSystems Corp",
                "location": "Denver, CO",
                "description": "Join our team to manage and optimize our database systems. You'll be responsible for database design, performance tuning, backup and recovery, and security. Experience with both SQL and NoSQL databases is preferred.",
                "skills_match": ["SQL", "MySQL", "PostgreSQL", "MongoDB", "Oracle", "Database", "Performance Tuning", "Data Modeling"],
                "url": "https://example.com/job10",
                "salary": "$95,000 - $125,000",
                "date_posted": "2023-06-28",
                "job_type": "Full-time",
                "experience_level": "Mid-level to Senior"
            },
            {
                "title": "Junior Python Developer",
                "company": "CodeCraft Solutions",
                "location": "Remote",
                "description": "Great opportunity for a junior developer to join our team and grow their skills. You'll work on web applications using Python and Django under the guidance of senior developers. Strong fundamentals and eagerness to learn are essential.",
                "skills_match": ["Python", "Django", "HTML", "CSS", "JavaScript", "Git"],
                "url": "https://example.com/job11",
                "salary": "$70,000 - $90,000",
                "date_posted": "2023-07-01",
                "job_type": "Full-time",
                "experience_level": "Junior"
            },
            {
                "title": "Data Engineer",
                "company": "BigData Solutions",
                "location": "Chicago, IL",
                "description": "Looking for a data engineer to build and maintain our data infrastructure. You'll work with ETL processes, data warehousing, and big data technologies to ensure data quality and accessibility for our data science team.",
                "skills_match": ["Python", "SQL", "ETL", "Spark", "Hadoop", "Data Warehousing", "AWS"],
                "url": "https://example.com/job12",
                "salary": "$110,000 - $140,000",
                "date_posted": "2023-07-05",
                "job_type": "Full-time",
                "experience_level": "Mid-level"
            },
            {
                "title": "Frontend Developer (Contract)",
                "company": "Digital Agency Inc.",
                "location": "Remote",
                "description": "6-month contract role for a frontend developer with strong React skills. You'll work on client projects, implementing responsive designs and interactive features. Possibility of extension or conversion to full-time for the right candidate.",
                "skills_match": ["JavaScript", "React", "HTML", "CSS", "Responsive Design", "Git"],
                "url": "https://example.com/job13",
                "salary": "$60-80/hour",
                "date_posted": "2023-07-10",
                "job_type": "Contract (6 months)",
                "experience_level": "Mid-level"
            },
            {
                "title": "Technical Project Manager",
                "company": "Enterprise Solutions",
                "location": "New York, NY",
                "description": "Seeking a technical project manager with software development background to lead our engineering teams. You'll coordinate project timelines, manage resources, and ensure successful delivery of our products.",
                "skills_match": ["Project Management", "Agile", "Scrum", "JIRA", "Software Development", "Communication", "Leadership"],
                "url": "https://example.com/job14",
                "salary": "$120,000 - $150,000",
                "date_posted": "2023-07-15",
                "job_type": "Full-time",
                "experience_level": "Senior"
            },
            {
                "title": "QA Engineer",
                "company": "Quality Software Inc.",
                "location": "Austin, TX",
                "description": "Join our QA team to ensure the quality of our software products. You'll design and execute test plans, automate testing processes, and collaborate with developers to fix issues. Experience with test automation frameworks is required.",
                "skills_match": ["Selenium", "Test Automation", "QA", "Python", "JavaScript", "CI/CD", "JIRA"],
                "url": "https://example.com/job15",
                "salary": "$85,000 - $110,000",
                "date_posted": "2023-07-20",
                "job_type": "Full-time",
                "experience_level": "Mid-level"
            }
        ]
        
        # Initial job list
        filtered_jobs = mock_jobs
        
        # Filter by location if provided
        if location:
            filtered_jobs = [job for job in filtered_jobs if location.lower() in job["location"].lower()]
        
        # Filter by salary range if provided
        if salary_range:
            min_salary, max_salary = salary_range
            
            def is_in_salary_range(job):
                salary = job.get('salary', '')
                # Handle hourly rates (convert to annual assuming 2000 hours/year)
                if '/hour' in salary or '/hr' in salary:
                    try:
                        # Extract hourly rate and convert to annual
                        rate = salary.replace('$', '').replace(',', '').split('/')[0]
                        if '-' in rate:
                            min_rate, max_rate = rate.split('-')
                            annual_min = float(min_rate.strip()) * 2000
                            annual_max = float(max_rate.strip()) * 2000
                        else:
                            annual_min = annual_max = float(rate.strip()) * 2000
                    except:
                        return True  # Include if parsing fails
                else:
                    try:
                        # Extract salary range for normal salaries
                        salary = salary.replace('$', '').replace(',', '').replace('k', '000')
                        if '-' in salary:
                            parts = salary.split('-')
                            annual_min = float(parts[0].strip())
                            annual_max = float(parts[1].strip().split('/')[0])
                        else:
                            annual_min = annual_max = float(salary.split('/')[0].strip())
                    except:
                        return True  # Include if parsing fails
                
                # Check if job salary range overlaps with desired range
                return (annual_max >= min_salary and annual_min <= max_salary)
            
            filtered_jobs = [job for job in filtered_jobs if is_in_salary_range(job)]
        
        # Filter by date posted
        if date_filter != "Any time":
            from datetime import datetime, timedelta
            today = datetime.now()
            
            if date_filter == "Past week":
                cutoff_date = today - timedelta(days=7)
            elif date_filter == "Past month":
                cutoff_date = today - timedelta(days=30)
            elif date_filter == "Past 3 months":
                cutoff_date = today - timedelta(days=90)
            
            def is_recent_enough(job):
                try:
                    post_date = datetime.strptime(job.get('date_posted', '2023-01-01'), '%Y-%m-%d')
                    return post_date >= cutoff_date
                except:
                    return True  # Include if parsing fails
            
            filtered_jobs = [job for job in filtered_jobs if is_recent_enough(job)]
        
        # Filter by company size
        if company_filter != "Any size":
            # Add company size to mock data (would normally come from API)
            company_sizes = {
                "TechCorp": "Large (1000+)",
                "StartupXYZ": "Startup",
                "WebDev Solutions": "Small (10-100)",
                "Data Insights Inc.": "Medium (100-1000)",
                "AI Research Lab": "Small (10-100)",
                "Cloud Systems": "Medium (100-1000)",
                "DevOps Experts": "Small (10-100)",
                "SecureNet Solutions": "Medium (100-1000)",
                "AppWorks Mobile": "Small (10-100)",
                "DataSystems Corp": "Medium (100-1000)",
                "CodeCraft Solutions": "Small (10-100)",
                "BigData Solutions": "Medium (100-1000)",
                "Digital Agency Inc.": "Small (10-100)",
                "Enterprise Solutions": "Large (1000+)",
                "Quality Software Inc.": "Medium (100-1000)"
            }
            
            filtered_jobs = [job for job in filtered_jobs if company_sizes.get(job['company'], 'Any size') == company_filter]
        
        # Filter and rank jobs based on skills match
        ranked_jobs = []
        for job in filtered_jobs:
            # Count how many skills match
            matching_skills = [skill for skill in job["skills_match"] if skill in skills]
            match_count = len(matching_skills)
            
            # Only include jobs with at least one matching skill
            if match_count > 0:
                # Calculate match percentage (weighted to favor jobs with more matching skills)
                match_percentage = (match_count / len(job["skills_match"])) * 100
                
                # Boost score for jobs with high percentage of matched skills from user's skill set
                user_skill_coverage = match_count / len(skills) if skills else 0
                weighted_score = match_percentage * 0.7 + (user_skill_coverage * 100) * 0.3
                
                # Add job to ranked list with match info
                ranked_job = job.copy()
                ranked_job["matching_skills"] = matching_skills
                ranked_job["match_count"] = match_count
                ranked_job["match_percentage"] = weighted_score
                ranked_jobs.append(ranked_job)
        
        # Sort by match percentage (highest first)
        ranked_jobs.sort(key=lambda x: x["match_percentage"], reverse=True)
        
        # Return top N results
        return ranked_jobs[:num_results]

    # Function to generate career advice based on skills and preferences
    def generate_career_advice(skills, career_goal="", work_preferences=None, skill_interests=None):
        # This is a simplified function that would normally use more sophisticated AI
        # For demonstration purposes, we'll return advice based on skill categories and user preferences
        
        # Set default values for optional parameters
        if work_preferences is None:
            work_preferences = {}
        
        if skill_interests is None:
            skill_interests = []
        
        # Define skill categories with expanded lists
        programming_languages = ["Python", "Java", "JavaScript", "C++", "C#", "Ruby", "PHP", "Swift", "Kotlin", "Go", "Rust", "TypeScript", "Scala", "Perl", "Shell", "Bash", "PowerShell"]
        web_dev = ["HTML", "CSS", "React", "Angular", "Vue", "Django", "Flask", "Express", "Node.js", "jQuery", "Bootstrap", "Webpack", "Babel", "Sass", "Less", "Tailwind CSS", "GraphQL", "RESTful API"]
        data_science = ["Python", "R", "Machine Learning", "Deep Learning", "NLP", "Data Analysis", "Data Visualization", "TensorFlow", "PyTorch", "Pandas", "NumPy", "Scikit-learn", "Spark", "Hadoop", "Big Data", "Statistics", "Data Mining"]
        devops = ["AWS", "Azure", "GCP", "Docker", "Kubernetes", "Jenkins", "Git", "CI/CD", "Terraform", "Ansible", "Puppet", "Chef", "Prometheus", "Grafana", "ELK Stack", "Linux", "Networking", "Security"]
        mobile_dev = ["Android", "iOS", "React Native", "Flutter", "Xamarin", "Ionic", "Swift", "Kotlin", "Mobile Development", "SwiftUI", "Jetpack Compose", "Mobile Security", "App Store Optimization"]
        design = ["UI/UX", "Figma", "Sketch", "Adobe XD", "Photoshop", "Illustrator", "InDesign", "User Research", "Wireframing", "Prototyping", "Design Systems", "Accessibility", "Motion Design"]
        soft_skills = ["Communication", "Leadership", "Teamwork", "Problem Solving", "Critical Thinking", "Time Management", "Adaptability", "Project Management", "Agile", "Scrum", "Negotiation", "Presentation", "Conflict Resolution"]
        business_skills = ["Marketing", "Sales", "Business Development", "Product Management", "Strategy", "Finance", "Accounting", "Operations", "Customer Service", "Consulting", "Entrepreneurship"]
        
        # Count skills in each category
        category_counts = {
            "Programming": sum(1 for skill in skills if skill in programming_languages),
            "Web Development": sum(1 for skill in skills if skill in web_dev),
            "Data Science": sum(1 for skill in skills if skill in data_science),
            "DevOps": sum(1 for skill in skills if skill in devops),
            "Mobile Development": sum(1 for skill in skills if skill in mobile_dev),
            "Design": sum(1 for skill in skills if skill in design),
            "Soft Skills": sum(1 for skill in skills if skill in soft_skills),
            "Business Skills": sum(1 for skill in skills if skill in business_skills)
        }
        
        # Find the top categories (up to 3)
        sorted_categories = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
        top_categories = [cat[0] for cat in sorted_categories[:3] if cat[1] > 0]
        
        # If no skills matched our categories, use a default
        if not top_categories:
            top_categories = ["General Technology"]
        
        # Get years of experience and education if available
        years_exp = st.session_state.get('years_of_experience', 0)
        education = st.session_state.get('education', [])
        
        # Determine experience level
        if years_exp is None or years_exp < 2:
            experience_level = "Entry-level"
        elif years_exp < 5:
            experience_level = "Mid-level"
        else:
            experience_level = "Senior-level"
        
        # Generate advice based on top categories and user inputs
        advice = {
            "top_field": top_categories[0],
            "secondary_fields": top_categories[1:] if len(top_categories) > 1 else [],
            "experience_level": experience_level,
            "career_paths": [],
            "skill_recommendations": [],
            "learning_resources": [],
            "industry_trends": "",
            "skill_categories": category_counts
        }
        
        # Career paths based on top field and experience level
        career_paths_by_field = {
            "Programming": {
                "Entry-level": ["Junior Software Developer", "Backend Developer", "API Developer", "QA Engineer"],
                "Mid-level": ["Software Engineer", "Full Stack Developer", "DevOps Engineer", "Technical Lead"],
                "Senior-level": ["Senior Software Engineer", "Software Architect", "Engineering Manager", "CTO"]
            },
            "Web Development": {
                "Entry-level": ["Junior Frontend Developer", "Junior Web Developer", "UI Developer", "WordPress Developer"],
                "Mid-level": ["Frontend Developer", "Full Stack Web Developer", "JavaScript Developer", "Web Application Developer"],
                "Senior-level": ["Senior Frontend Engineer", "Web Application Architect", "Technical Lead", "UI/UX Engineering Manager"]
            },
            "Data Science": {
                "Entry-level": ["Junior Data Analyst", "Data Engineer", "Business Intelligence Analyst", "Research Assistant"],
                "Mid-level": ["Data Scientist", "Machine Learning Engineer", "AI Developer", "BI Developer"],
                "Senior-level": ["Senior Data Scientist", "Lead ML Engineer", "AI Research Scientist", "Director of Data Science"]
            },
            "DevOps": {
                "Entry-level": ["Cloud Support Engineer", "Junior DevOps Engineer", "Systems Administrator", "IT Operations Analyst"],
                "Mid-level": ["DevOps Engineer", "Site Reliability Engineer", "Cloud Engineer", "Infrastructure Developer"],
                "Senior-level": ["Senior DevOps Engineer", "Cloud Architect", "Infrastructure Architect", "Head of DevOps"]
            },
            "Mobile Development": {
                "Entry-level": ["Junior Mobile Developer", "iOS/Android Developer", "Mobile QA Engineer", "App Support Specialist"],
                "Mid-level": ["Mobile App Developer", "Cross-platform Developer", "Mobile UI Developer", "App Performance Engineer"],
                "Senior-level": ["Senior Mobile Developer", "Mobile Architect", "Lead App Developer", "Mobile Development Manager"]
            },
            "Design": {
                "Entry-level": ["Junior UI Designer", "Visual Designer", "Design Assistant", "Web Designer"],
                "Mid-level": ["UI/UX Designer", "Product Designer", "Interaction Designer", "UX Researcher"],
                "Senior-level": ["Senior UX Designer", "Design Systems Specialist", "Creative Director", "Head of Design"]
            },
            "Soft Skills": {
                "Entry-level": ["Project Coordinator", "Team Lead", "Scrum Master", "Business Analyst"],
                "Mid-level": ["Project Manager", "Product Owner", "Agile Coach", "Operations Manager"],
                "Senior-level": ["Senior Project Manager", "Program Manager", "Director of Operations", "Chief of Staff"]
            },
            "Business Skills": {
                "Entry-level": ["Business Development Representative", "Marketing Specialist", "Sales Associate", "Product Analyst"],
                "Mid-level": ["Product Manager", "Marketing Manager", "Business Analyst", "Account Manager"],
                "Senior-level": ["Senior Product Manager", "Director of Marketing", "VP of Sales", "Chief Product Officer"]
            },
            "General Technology": {
                "Entry-level": ["IT Support Specialist", "Technical Support Engineer", "Junior Developer", "QA Tester"],
                "Mid-level": ["Systems Engineer", "Technical Consultant", "IT Project Manager", "Solutions Engineer"],
                "Senior-level": ["IT Manager", "Solutions Architect", "Technical Director", "CIO/CTO"]
            }
        }
        
        # Skill recommendations based on top field and career goals
        skill_recommendations_by_field = {
            "Programming": ["Cloud Services (AWS/Azure/GCP)", "Microservices Architecture", "Containerization (Docker)", "Version Control (Git)", "CI/CD Pipelines", "Test-Driven Development", "Design Patterns", "System Design"],
            "Web Development": ["TypeScript", "Next.js/Nuxt.js", "GraphQL", "Tailwind CSS", "Web Performance Optimization", "Progressive Web Apps", "Web Accessibility", "Responsive Design", "State Management"],
            "Data Science": ["Deep Learning", "Natural Language Processing", "Computer Vision", "Big Data Technologies (Spark)", "MLOps", "Feature Engineering", "A/B Testing", "Statistical Analysis", "Data Ethics"],
            "DevOps": ["Infrastructure as Code", "Kubernetes", "Monitoring and Observability", "Security Automation", "GitOps", "Cloud Cost Optimization", "Disaster Recovery", "Service Mesh", "Zero Trust Security"],
            "Mobile Development": ["SwiftUI/Jetpack Compose", "React Native/Flutter", "Mobile Performance Optimization", "Offline-first Design", "Mobile Security", "App Store Optimization", "Mobile Analytics", "Push Notifications", "Mobile Accessibility"],
            "Design": ["Design Systems", "Prototyping", "User Research", "Accessibility", "Motion Design", "Design Thinking", "Information Architecture", "Usability Testing", "Design Psychology"],
            "Soft Skills": ["Leadership", "Communication", "Conflict Resolution", "Negotiation", "Time Management", "Emotional Intelligence", "Public Speaking", "Team Building", "Strategic Thinking"],
            "Business Skills": ["Product Management", "Market Research", "Business Strategy", "Financial Analysis", "Customer Development", "Growth Hacking", "Stakeholder Management", "OKRs/KPIs", "Business Model Canvas"],
            "General Technology": ["Project Management", "Technical Writing", "Problem Solving", "System Architecture", "Data Analysis", "Security Fundamentals", "Networking Basics", "Agile Methodologies", "Cross-functional Collaboration"]
        }
        
        # Learning resources based on top field and skill interests
        learning_resources_by_field = {
            "Programming": ["LeetCode for algorithm practice", "GitHub repositories of open-source projects", "Coursera - Programming courses", "Udemy - Complete programming bootcamps", "Clean Code by Robert C. Martin", "Design Patterns: Elements of Reusable Object-Oriented Software", "The Pragmatic Programmer"],
            "Web Development": ["Frontend Masters", "CSS-Tricks", "JavaScript30 by Wes Bos", "Full Stack Open by University of Helsinki", "MDN Web Docs", "Smashing Magazine", "A List Apart", "Web.dev by Google"],
            "Data Science": ["Kaggle Competitions", "Fast.ai", "Coursera - Andrew Ng's Machine Learning Courses", "DataCamp", "Towards Data Science", "Elements of Statistical Learning", "Python for Data Analysis", "Deep Learning by Ian Goodfellow"],
            "DevOps": ["A Cloud Guru", "Linux Academy", "Kubernetes Documentation", "The DevOps Handbook", "Infrastructure as Code by Kief Morris", "Site Reliability Engineering (Google's SRE Book)", "The Phoenix Project"],
            "Mobile Development": ["Ray Wenderlich Tutorials", "Flutter Dev", "iOS Dev Weekly", "Android Developers Blog", "Mobile App Development & Swift by Apple", "Head First Android Development", "Flutter in Action"],
            "Design": ["Dribbble", "Behance", "Nielsen Norman Group Articles", "Interaction Design Foundation", "Don't Make Me Think by Steve Krug", "The Design of Everyday Things", "Refactoring UI", "Design Systems Handbook"],
            "Soft Skills": ["Toastmasters International", "Crucial Conversations", "LinkedIn Learning - Soft Skills courses", "How to Win Friends and Influence People", "Emotional Intelligence 2.0", "Radical Candor", "The 7 Habits of Highly Effective People"],
            "Business Skills": ["Harvard Business Review", "Product School", "Y Combinator Startup School", "The Lean Startup", "Zero to One", "Inspired: How to Create Products Customers Love", "Business Model Generation", "Strategyzer"],
            "General Technology": ["Pluralsight", "LinkedIn Learning", "MIT OpenCourseWare", "edX Technology Courses", "O'Reilly Learning Platform", "Stack Overflow", "Medium Technology Publications", "TED Talks on Technology"]
        }
        
        # Industry trends based on top field
        industry_trends_by_field = {
            "Programming": "The demand for skilled programmers continues to grow across industries. Focus on learning cloud-native development, microservices architecture, and AI integration. Low-code/no-code platforms are rising but creating more demand for complex programming skills.",
            "Web Development": "Web development is evolving with a focus on performance and user experience. JAMstack, headless CMS, progressive web apps, and WebAssembly are becoming increasingly important. Web3 technologies and decentralized applications are creating new opportunities.",
            "Data Science": "Data science is becoming more specialized. Consider focusing on a specific domain like NLP, computer vision, or time series analysis. MLOps and productionizing models are increasingly important skills. Ethical AI and explainable AI are growing concerns.",
            "DevOps": "DevOps is evolving towards GitOps, Infrastructure as Code, and Platform Engineering. Focus on security integration (DevSecOps), cloud-native technologies, and FinOps for cost optimization. Kubernetes and service mesh technologies continue to dominate the container orchestration space.",
            "Mobile Development": "Cross-platform development continues to gain popularity, but native expertise is still valuable. Focus on creating seamless user experiences, optimizing for performance and battery life. Super apps, AR/VR integration, and on-device AI are emerging trends.",
            "Design": "Design is becoming more integrated with development through design systems and tools like Figma. Focus on accessibility, inclusive design, and creating cohesive experiences across platforms. Design ops and design at scale are becoming important for larger organizations.",
            "Soft Skills": "As automation increases, soft skills become more valuable. Remote and hybrid work models demand stronger communication, self-management, and digital collaboration skills. Emotional intelligence and adaptability are increasingly valued by employers across all industries.",
            "Business Skills": "Product-led growth, customer-centric approaches, and data-driven decision making are reshaping business strategies. Agile methodologies are expanding beyond software into general business operations. Sustainability and social responsibility are becoming key business considerations.",
            "General Technology": "Technology roles are becoming more hybrid, requiring both technical and business acumen. AI and automation are transforming all aspects of technology work. Continuous learning and adaptability are essential as technology cycles accelerate."
        }
        
        # Populate advice based on top field and user inputs
        primary_field = advice["top_field"]
        
        # Add career paths based on experience level and top fields
        for field in top_categories:
            if field in career_paths_by_field and experience_level in career_paths_by_field[field]:
                advice["career_paths"].extend(career_paths_by_field[field][experience_level])
        
        # Remove duplicates while preserving order
        advice["career_paths"] = list(dict.fromkeys(advice["career_paths"]))
        
        # Add skill recommendations based on top fields and skill interests
        for field in top_categories:
            if field in skill_recommendations_by_field:
                advice["skill_recommendations"].extend(skill_recommendations_by_field[field][:3])  # Top 3 from each field
        
        # Add additional skills based on user's skill interests
        if skill_interests:
            for interest in skill_interests:
                if interest == "Technical Skills":
                    # Add technical skills from fields not in top categories
                    for field in ["Programming", "Web Development", "Data Science", "DevOps"]:
                        if field not in top_categories and field in skill_recommendations_by_field:
                            advice["skill_recommendations"].extend(skill_recommendations_by_field[field][:2])  # Top 2 from each field
                elif interest == "Leadership":
                    advice["skill_recommendations"].extend(["Team Leadership", "Strategic Planning", "Mentoring", "Decision Making"])
                elif interest == "Project Management":
                    advice["skill_recommendations"].extend(["Agile/Scrum", "Risk Management", "Resource Planning", "Stakeholder Communication"])
                elif interest == "Communication":
                    advice["skill_recommendations"].extend(["Technical Writing", "Presentation Skills", "Client Communication", "Documentation"])
                elif interest == "Data Analysis":
                    advice["skill_recommendations"].extend(["SQL", "Data Visualization", "Statistical Analysis", "Excel/Spreadsheets"])
                elif interest == "Design":
                    advice["skill_recommendations"].extend(["UI/UX Fundamentals", "Color Theory", "Typography", "User-Centered Design"])
        
        # Remove duplicates while preserving order
        advice["skill_recommendations"] = list(dict.fromkeys(advice["skill_recommendations"]))
        
        # Add learning resources based on top fields
        for field in top_categories:
            if field in learning_resources_by_field:
                advice["learning_resources"].extend(learning_resources_by_field[field][:3])  # Top 3 from each field
        
        # Add industry trends based on primary field
        if primary_field in industry_trends_by_field:
            advice["industry_trends"] = industry_trends_by_field[primary_field]
        
        # Customize advice based on career goals if provided
        if career_goal:
            # Look for keywords in career goals
            career_goal_lower = career_goal.lower()
            
            if "transition" in career_goal_lower or "switch" in career_goal_lower or "change" in career_goal_lower:
                advice["career_transition"] = "Career transitions require highlighting transferable skills and filling skill gaps. Consider starting with hybrid roles that leverage your current expertise while building new skills."
            
            if "senior" in career_goal_lower or "lead" in career_goal_lower or "manager" in career_goal_lower:
                advice["leadership_path"] = "Moving into leadership requires demonstrating impact beyond individual contributions. Focus on mentoring others, leading projects, and developing a strategic perspective on your work."
            
            if "freelance" in career_goal_lower or "independent" in career_goal_lower or "consultant" in career_goal_lower:
                advice["freelance_path"] = "Building a successful freelance career requires both technical excellence and business acumen. Focus on developing a strong portfolio, client relationship skills, and basic business operations knowledge."
        
        # Customize advice based on work preferences if provided
        if work_preferences:
            work_env = work_preferences.get("environment", "")
            if work_env == "Remote":
                advice["remote_work_tips"] = "Success in remote work requires strong self-management, communication skills, and establishing clear boundaries between work and personal life."
            
            industries = work_preferences.get("industry", [])
            if industries:
                advice["industry_specific"] = f"To succeed in the {', '.join(industries)} {'industry' if len(industries) == 1 else 'industries'}, focus on understanding domain-specific knowledge and building a network of professionals in {'this field' if len(industries) == 1 else 'these fields'}."
        
        return advice

    # --- Main application ---
    
    # Header with Logout Button
    col1, col2 = st.columns([4, 1])
    with col1:
        st.title("🚀 HireIQ")
        st.markdown(f"Welcome, **{st.session_state.get('username', 'User')}**!")
    with col2:
        st.write("") # Spacer
        st.write("") # Spacer
        if st.button("Logout"):
            st.session_state['authenticated'] = False
            st.session_state['username'] = None
            # Clear other session data if needed
            for key in list(st.session_state.keys()):
                if key not in ['authenticated', 'username']:
                    del st.session_state[key]
            st.rerun()

    st.markdown("<p class='subtitle'>Your AI-powered career assistant</p>", unsafe_allow_html=True)
    
    # Create tabs
    tabs = st.tabs(["📄 Resume Analyzer", "🔍 Job Search", "🧭 Career Advisor", "📊 Dashboard & Insights"])
    # --- Dashboard & Insights Tab (Final Visuals) ---
    with tabs[3]:
        import plotly.graph_objects as go
        import plotly.express as px

        # 1. CSS for Perfect Dark Theme
        st.markdown("""
        <style>
            /* Main Background */
            .stApp { background-color: #0e1117; }
            
            /* Card Container */
            div.css-1r6slb0, div[data-testid="stMetric"] {
                background-color: #1f2937; 
                border: 1px solid #374151;
                padding: 15px;
                border-radius: 12px;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
            }
            
            /* Typography */
            h1, h2, h3, h4, p, span { color: #f3f4f6 !important; font-family: 'Inter', sans-serif; }
            
            /* Metric Value */
            div[data-testid="stMetricValue"] { color: #3b82f6 !important; font-weight: 700; }
            
            /* Divider Line */
            .gradient-line {
                height: 3px;
                background: linear-gradient(90deg, #ec4899, #8b5cf6, #3b82f6);
                border-radius: 5px;
                margin: 20px 0;
            }
        </style>
        """, unsafe_allow_html=True)

        # --- Header ---
        c1, c2 = st.columns([5,1])
        c1.markdown("## 📊 Career Insights Panel")
        if c2.button("Refresh Data ⟳", use_container_width=True):
            st.rerun()
        st.markdown('<div class="gradient-line"></div>', unsafe_allow_html=True)

        # --- 2. METRICS (Top Stats) ---
        skills_count = len(st.session_state.get('extracted_skills', []))
        jobs_count = len(st.session_state.get('job_recommendations', []))
        saved_count = len(st.session_state.get('saved_jobs', []))
        
        # Dynamic Mock Logic for Demo
        market_score = 85
        if jobs_count > 0: market_score = 92

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Skills Detected", skills_count, "Verified")
        col2.metric("Jobs Found", jobs_count, "Active")
        col3.metric("Saved Jobs", saved_count, "Favorites")
        col4.metric("Market Fit Score", f"{market_score}%", "High Relevance")
        
        st.markdown("---")

        # --- 3. CHARTS SECTION ---
        col_charts_1, col_charts_2 = st.columns(2)

        # --- Left: Job Type Distribution (Teal, Yellow, Orange, Purple) ---
        with col_charts_1:
            st.subheader("🍩 Job Type Distribution")
            
            # 1. Check Data
            if jobs_count > 0:
                job_types = [job.get('job_type', 'Full-time') for job in st.session_state.job_recommendations]
                unique_types = list(set(job_types))
                
                # TRICK: जर फक्त एकच प्रकारचा जॉब (उदा. Full-time) असेल, 
                # तर चार्ट बोरिंग दिसतो. म्हणून आपण Demo साठी Mock Data मिक्स करू.
                if len(unique_types) < 2:
                    df_pie = pd.DataFrame({
                        'Type': ['Full-time', 'Remote', 'Contract', 'Internship'], 
                        'Count': [jobs_count, max(1, jobs_count//2), max(1, jobs_count//3), max(1, jobs_count//4)]
                    })
                else:
                    # जर डेटा खरा आणि वेगळा असेल तर तोच वापरा
                    type_counts = pd.Series(job_types).value_counts().reset_index()
                    type_counts.columns = ['Type', 'Count']
                    df_pie = type_counts
            else:
                # Default Mock Data (जर काहीच सर्च नसेल तर)
                df_pie = pd.DataFrame({
                    'Type': ['Full-time', 'Remote', 'Contract', 'Internship'], 
                    'Count': [45, 25, 20, 10]
                })
            
            # 2. FORCE COLORS (Teal, Yellow, Orange, Purple)
            # आपण रंगांचे मॅपिंग फिक्स करत आहोत जेणेकरून रंग बदलणार नाहीत.
            color_map = {
                'Full-time': '#26A69A',  # Teal
                'Remote': '#FFEE58',     # Yellow
                'Contract': '#FF7043',   # Orange
                'Internship': '#AB47BC', # Purple
                'Part-time': '#AB47BC'   # Fallback Purple
            }
            
            fig_pie = px.pie(df_pie, values='Count', names='Type', hole=0.5, 
                             color='Type', color_discrete_map=color_map)
            
            fig_pie.update_layout(
                paper_bgcolor="rgba(0,0,0,0)", 
                plot_bgcolor="rgba(0,0,0,0)", 
                font_color="white",
                margin=dict(t=30, b=10, l=10, r=10),
                showlegend=True,
                legend=dict(orientation="v", yanchor="middle", y=0.5)
            )
            st.plotly_chart(fig_pie, use_container_width=True)

        # --- Right: Salary Trends (Steel Blue) ---
        with col_charts_2:
            st.subheader("💰 Salary Trends (Annual)")
            
            salary_ranges = ['30k-50k', '50k-80k', '80k-100k', '100k-120k', '120k+']
            job_avail = [5, 12, 18, 8, 4] # Mock data visual
            
            fig_bar = go.Figure(data=[go.Bar(
                x=salary_ranges, 
                y=job_avail,
                marker_color='#4682B4', # Steel Blue Hex Code
                width=0.6
            )])
            
            fig_bar.update_layout(
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="white",
                xaxis=dict(title="Salary Range", showgrid=False, gridcolor="#374151"),
                yaxis=dict(title="Jobs Available", showgrid=True, gridcolor="#374151"),
                margin=dict(t=30, b=10, l=10, r=10),
                height=350
            )
            st.plotly_chart(fig_bar, use_container_width=True)

        st.markdown("---")
        st.subheader("🧠 Advanced Analytics")

        # --- 4. ADVANCED ANALYTICS ---
        row2_c1, row2_c2 = st.columns([1, 2])

        # --- Left: Skill Gap (Blue vs Purple) ---
        with row2_c1:
            st.markdown("**Skill Gap Analysis**")
            categories = ['Python', 'React', 'SQL', 'AWS', 'Communication']
            
            fig_radar = go.Figure()
            
            # You (Blue)
            fig_radar.add_trace(go.Scatterpolar(
                r=[4, 3, 5, 2, 4], theta=categories, fill='toself', name='You',
                line_color='#29B6F6', fillcolor='rgba(41, 182, 246, 0.3)'
            ))
            # Market (Purple)
            fig_radar.add_trace(go.Scatterpolar(
                r=[5, 4, 5, 4, 5], theta=categories, fill='toself', name='Market',
                line_color='#AB47BC', fillcolor='rgba(171, 71, 188, 0.3)'
            ))

            fig_radar.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 5], gridcolor="#4b5563"), bgcolor="rgba(0,0,0,0)"),
                paper_bgcolor="rgba(0,0,0,0)", font_color="white",
                legend=dict(orientation="h", y=-0.1),
                margin=dict(t=20, b=20, l=30, r=30),
                height=350
            )
            st.plotly_chart(fig_radar, use_container_width=True)

        # --- Right: Market Trend (Green/Teal Gradient) ---
        with row2_c2:
            st.markdown("**📈 Job Market Trend (Last 6 Months)**")
            months = ['May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']
            openings = [120, 145, 130, 160, 190, 210]
            
            fig_area = go.Figure()
            fig_area.add_trace(go.Scatter(
                x=months, y=openings, fill='tozeroy', mode='lines', 
                line=dict(color='#00E676', width=3), # Bright Teal/Green
                fillcolor='rgba(0, 230, 118, 0.2)'
            ))
            
            fig_area.update_layout(
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="white",
                xaxis=dict(showgrid=False, gridcolor="#374151"),
                yaxis=dict(showgrid=True, gridcolor="#374151"),
                margin=dict(t=20, b=20, l=10, r=10),
                height=350
            )
            st.plotly_chart(fig_area, use_container_width=True)

        st.markdown("---")

        # --- 5. TOP COMPANIES (Table with Progress Bar) ---
        st.subheader("🏆 Top Recommended Companies")
        
        # Mock Data to match screenshot
        comp_data = [
            {"Rank": 1, "Company": "Tech Innovations Inc.", "Match Score": 0.98, "Open Roles": 3, "Status": "Actively Hiring"},
            {"Rank": 2, "Company": "DataMinds Analytics", "Match Score": 0.95, "Open Roles": 1, "Status": "Hiring"},
            {"Rank": 3, "Company": "CloudNative Systems", "Match Score": 0.92, "Open Roles": 2, "Status": "Urgent"},
            {"Rank": 4, "Company": "WebSolutions Ltd.", "Match Score": 0.88, "Open Roles": 5, "Status": "Active"},
        ]
        df_companies = pd.DataFrame(comp_data)
        
        st.dataframe(
            df_companies,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Rank": st.column_config.NumberColumn("Rank", format="%d", width="small"),
                "Company": st.column_config.TextColumn("Company"),
                "Match Score": st.column_config.ProgressColumn(
                    "Match Score", format="%.2f", min_value=0, max_value=1,
                    help="AI Match Score"
                ),
                "Status": st.column_config.TextColumn("Status")
            }
        )
            
    # Resume Analyzer Tab
    with tabs[0]:
        st.header("Resume Analyzer Bot")
        st.markdown("Upload your resume to get an analysis of your skills and suggestions for improvement.")
        
        # File uploader
        uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
        
        if uploaded_file is not None:
            # Extract text from the uploaded file
            if uploaded_file.type == "application/pdf":
                resume_text = extract_text_from_pdf(uploaded_file)
            elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                resume_text = extract_text_from_docx(uploaded_file)
            
            # Store the resume text in session state
            st.session_state.resume_data = resume_text
            
            # Extract skills from the resume
            skills = extract_skills(resume_text)
            st.session_state.extracted_skills = skills
            
            # Display the extracted skills
            st.subheader("Extracted Skills")
            if skills:
                # Create columns for skills display
                cols = st.columns(3)
                for i, skill in enumerate(skills):
                    cols[i % 3].markdown(f"✅ {skill}")
            else:
                st.warning("No skills were extracted from your resume. Please make sure your resume is properly formatted.")
            
            # Analyze the resume and provide feedback
            if skills:
                feedback = analyze_resume(resume_text, skills)
                
                st.subheader("Resume Feedback")
                for item in feedback:
                    st.markdown(f"🔹 {item}")
                
                # Provide a download button for the analysis
                analysis_data = {
                    "extracted_skills": skills,
                    "feedback": feedback,
                    "analysis_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                analysis_json = json.dumps(analysis_data, indent=4)
                st.download_button(
                    label="Download Analysis",
                    data=analysis_json,
                    file_name="resume_analysis.json",
                    mime="application/json"
                )

    # Job Search Tab
    with tabs[1]:
        st.header("Smart Job Search Bot")
        st.markdown("Get job recommendations based on your skills and preferences.")
        
        # Check if skills have been extracted
        if st.session_state.extracted_skills:
            st.success(f"Found {len(st.session_state.extracted_skills)} skills from your resume.")
            
            # Create columns for filters
            col1, col2 = st.columns(2)
            
            # Location input with suggestions
            with col1:
                location = st.text_input("Enter location (optional)")
                if location:
                    st.info("💡 You can enter city, state, or 'Remote' for remote jobs")
            
            # Experience level filter
            with col2:
                experience_options = ["All Levels", "Junior", "Mid-level", "Senior"]
                experience_filter = st.selectbox("Experience Level", experience_options, index=0)
            
            # Job type filter and number of results
            col3, col4 = st.columns(2)
            
            with col3:
                job_type_options = ["All Types", "Full-time", "Part-time", "Contract", "Internship"]
                job_type_filter = st.selectbox("Job Type", job_type_options, index=0)
            
            with col4:
                num_results = st.slider("Number of job recommendations", min_value=1, max_value=15, value=5)
                
            # Add salary range filter
            st.markdown("### Salary Range")
            salary_range = st.slider("Select desired salary range ($)", 30000, 200000, (50000, 150000), step=5000)
            st.markdown(f"Looking for jobs with salary between ${salary_range[0]:,} - ${salary_range[1]:,}")
            
            # Add date posted filter
            col5, col6 = st.columns(2)
            with col5:
                date_options = ["Any time", "Past week", "Past month", "Past 3 months"]
                date_filter = st.selectbox("Date Posted", date_options, index=0)
            
            # Add company size preference
            with col6:
                company_options = ["Any size", "Startup", "Small (10-100)", "Medium (100-1000)", "Large (1000+)"]
                company_filter = st.selectbox("Company Size", company_options, index=0)
            
            # Skills selection
            if st.session_state.extracted_skills:
                st.markdown("### Select skills to prioritize in your search")
                selected_skills = st.multiselect(
                    "Skills",
                    st.session_state.extracted_skills,
                    default=st.session_state.extracted_skills[:min(5, len(st.session_state.extracted_skills))]
                )
            else:
                selected_skills = []
            
            # Search button
            if st.button("Find Jobs"):
                with st.spinner("Searching for jobs that match your skills..."):
                    # Search for jobs based on extracted skills and filters
                    jobs = search_jobs(
                        skills=selected_skills if selected_skills else st.session_state.extracted_skills,
                        location=location,
                        num_results=num_results,
                        salary_range=salary_range,
                        date_filter=date_filter,
                        company_filter=company_filter
                    )
                    
                    # Apply additional filters
                    if experience_filter != "All Levels":
                        jobs = [job for job in jobs if experience_filter.lower() in job.get('experience_level', '').lower()]
                    
                    if job_type_filter != "All Types":
                        jobs = [job for job in jobs if job_type_filter.lower() in job.get('job_type', '').lower()]
                    
                    # Store results in session state
                    st.session_state.job_recommendations = jobs
                    
                    # Store search parameters for reference
                    st.session_state.last_search = {
                        "skills": selected_skills if selected_skills else st.session_state.extracted_skills,
                        "location": location,
                        "experience": experience_filter,
                        "job_type": job_type_filter,
                        "salary_range": salary_range,
                        "date_filter": date_filter,
                        "company_filter": company_filter
                    }
            
            # Display job recommendations
            if st.session_state.job_recommendations:
                if len(st.session_state.job_recommendations) > 0:
                    st.subheader(f"Top {len(st.session_state.job_recommendations)} Job Recommendations")
                    
                    # Show search summary
                    if 'last_search' in st.session_state:
                        with st.expander("Search Parameters", expanded=False):
                            search_params = st.session_state.last_search
                            col1, col2 = st.columns(2)
                            with col1:
                                st.markdown(f"**Location:** {search_params['location'] if search_params['location'] else 'Any'}")
                                st.markdown(f"**Experience Level:** {search_params['experience']}")
                                st.markdown(f"**Job Type:** {search_params['job_type']}")
                                st.markdown(f"**Date Posted:** {search_params['date_filter']}")
                            with col2:
                                st.markdown(f"**Salary Range:** ${search_params['salary_range'][0]:,} - ${search_params['salary_range'][1]:,}")
                                st.markdown(f"**Company Size:** {search_params['company_filter']}")
                                st.markdown(f"**Skills:** {', '.join(search_params['skills'][:5])}{'...' if len(search_params['skills']) > 5 else ''}")
                    
                    # Add sorting and view options
                    col1, col2, col3 = st.columns([3, 1, 1])
                    with col1:
                        sort_options = ["Match Percentage", "Salary (High to Low)", "Date Posted (Newest First)", "Company Name"]
                        sort_by = st.radio("Sort by", sort_options, horizontal=True)
                    with col2:
                        view_mode = st.selectbox("View Mode", ["Detailed", "Compact"], index=0)
                    with col3:
                        if st.button("Compare Jobs"):
                            st.session_state.show_job_comparison = True
                    
                    # Sort jobs based on selection
                    sorted_jobs = st.session_state.job_recommendations.copy()
                    if sort_by == "Salary (High to Low)":
                        # Extract numeric value from salary string (assuming format like "$X - $Y")
                        def extract_max_salary(job):
                            salary = job.get('salary', '$0')
                            if '-' in salary:
                                try:
                                    max_part = salary.split('-')[1].strip()
                                    return float(max_part.replace('$', '').replace(',', '').split('/')[0])
                                except:
                                    return 0
                            return 0
                        sorted_jobs.sort(key=extract_max_salary, reverse=True)
                    elif sort_by == "Date Posted (Newest First)":
                        # Sort by date posted (assuming format like "YYYY-MM-DD")
                        sorted_jobs.sort(key=lambda x: x.get('date_posted', ''), reverse=True)
                    elif sort_by == "Company Name":
                        # Sort alphabetically by company name
                        sorted_jobs.sort(key=lambda x: x.get('company', '').lower())
                    else:  # Default: Match Percentage
                        sorted_jobs.sort(key=lambda x: x.get('match_percentage', 0), reverse=True)
                        
                    # Add a summary of results
                    st.info(f"Found {len(sorted_jobs)} matching jobs. Displaying results sorted by {sort_by}.")
                    
                    # Add a filter for quick job type filtering
                    job_types = list(set([job.get('job_type', 'Unknown') for job in sorted_jobs]))
                    if len(job_types) > 1:  # Only show if there are multiple job types
                        selected_job_types = st.multiselect(
                            "Quick filter by job type",
                            options=["All"] + job_types,
                            default=["All"]
                        )
                        
                        # Apply quick filter
                        if selected_job_types and "All" not in selected_job_types:
                            display_jobs = [job for job in sorted_jobs if job.get('job_type', 'Unknown') in selected_job_types]
                        else:
                            display_jobs = sorted_jobs
                    else:
                        display_jobs = sorted_jobs
                        
                    # Job comparison feature
                    if 'show_job_comparison' in st.session_state and st.session_state.show_job_comparison:
                        with st.expander("Job Comparison Tool", expanded=True):
                            st.markdown("### Compare Jobs Side by Side")
                            st.markdown("Select jobs to compare their details side by side.")
                            
                            # Get all jobs for selection
                            all_jobs = display_jobs
                            job_titles = [f"{job['title']} at {job['company']}" for job in all_jobs]
                            
                            # Let user select jobs to compare
                            selected_job_indices = st.multiselect(
                                "Select jobs to compare (2-3 recommended)",
                                options=range(len(job_titles)),
                                format_func=lambda i: job_titles[i]
                            )
                            
                            if selected_job_indices:
                                if len(selected_job_indices) > 4:
                                    st.warning("Comparing more than 4 jobs may be difficult to view. Consider selecting fewer jobs.")
                                
                                # Create comparison table
                                selected_jobs = [all_jobs[i] for i in selected_job_indices]
                                
                                # Display comparison
                                cols = st.columns(len(selected_jobs))
                                for i, (job, col) in enumerate(zip(selected_jobs, cols)):
                                    with col:
                                        st.markdown(f"**{job['title']}**")
                                        st.markdown(f"*{job['company']}*")
                                        st.markdown(f"**Match:** {job['match_percentage']:.1f}%")
                                        st.markdown(f"**Salary:** {job['salary']}")
                                        st.markdown(f"**Location:** {job['location']}")
                                        st.markdown(f"**Type:** {job.get('job_type', 'Not specified')}")
                                        st.markdown(f"**Experience:** {job.get('experience_level', 'Not specified')}")
                                        st.markdown(f"**Posted:** {job['date_posted']}")
                                        
                                        # Show matching skills count
                                        st.markdown(f"**Skills Match:** {len(job['matching_skills'])}/{len(job['skills_match'])}")
                                        
                                        # Action buttons
                                        st.markdown(f"[View Job]({job['url']})")
                                
                                # Skill comparison section
                                st.markdown("### Skill Comparison")
                                
                                # Get all unique skills across selected jobs
                                all_skills = set()
                                for job in selected_jobs:
                                    all_skills.update(job['skills_match'])
                                
                                # Create skill comparison table
                                skill_data = []
                                for skill in sorted(all_skills):
                                    row = {"Skill": skill}
                                    for i, job in enumerate(selected_jobs):
                                        job_name = f"{job['company']} - {job['title']}"
                                        if skill in job['matching_skills']:
                                            row[job_name] = "✓ (You have)" 
                                        elif skill in job['skills_match']:
                                            row[job_name] = "Required"
                                        else:
                                            row[job_name] = "-"
                                    skill_data.append(row)
                                
                                # Display as dataframe
                                skill_df = pd.DataFrame(skill_data)
                                st.dataframe(skill_df, use_container_width=True)
                                
                                # Close comparison button
                                if st.button("Close Comparison"):
                                    st.session_state.show_job_comparison = False
                                    st.rerun()
                    
                    # Display jobs based on view mode
                    if view_mode == "Compact":
                        # Compact view - table format
                        job_data = []
                        for job in display_jobs:
                            job_data.append({
                                "Title": job['title'],
                                "Company": job['company'],
                                "Location": job['location'],
                                "Salary": job['salary'],
                                "Match": f"{job['match_percentage']:.1f}%",
                                "Posted": job['date_posted'],
                                "Job Type": job.get('job_type', 'Not specified'),
                                "Experience": job.get('experience_level', 'Not specified')
                            })
                        
                        # Convert to DataFrame for display
                        job_df = pd.DataFrame(job_data)
                        st.dataframe(job_df, use_container_width=True)
                        
                        # Add a note about detailed view
                        st.info("👆 Switch to 'Detailed' view to see full job descriptions and save jobs.")
                    else:
                        # Detailed view with expandable sections
                        for i, job in enumerate(display_jobs):
                            
                            # --- FIXED PART START ---
                            # Determine emoji based on match percentage (HTML colors don't work in expander titles)
                            if job['match_percentage'] >= 80:
                                match_icon = "🟢"  # Green
                            elif job['match_percentage'] >= 60:
                                match_icon = "🟠"  # Orange
                            else:
                                match_icon = "🔵"  # Blue

                            # Create clean header with emoji
                            expander_header = f"{job['title']} at {job['company']} - {match_icon} {job['match_percentage']:.1f}% Match"
                            
                            # Use this for color in the box inside
                            match_color = "#4CAF50" if job['match_percentage'] >= 80 else "#FFA500" if job['match_percentage'] >= 60 else "#2196F3"
                            # --- FIXED PART END ---

                            with st.expander(expander_header, expanded=False):
                                # Create two columns for job details
                                col_left, col_right = st.columns([2, 1])
                                
                                with col_left:
                                    st.markdown(f"### {job['title']}")
                                    st.markdown(f"**Company:** {job['company']}")
                                    st.markdown(f"**Location:** {job['location']}")
                                    st.markdown(f"**Job Type:** {job.get('job_type', 'Not specified')}")
                                    st.markdown(f"**Experience Level:** {job.get('experience_level', 'Not specified')}")
                                    st.markdown(f"**Description:**")
                                    st.markdown(f"{job['description']}")
                                    st.markdown(f"**Matching Skills ({len(job['matching_skills'])}/{len(job['skills_match'])}):**")
                                    
                                    # Display matching skills as pills with improved styling
                                    skill_html = ""
                                    for skill in job['skills_match']:
                                        if skill in job['matching_skills']:
                                            skill_html += f"<span style='background-color: #4CAF50; color: white; padding: 5px 10px; margin: 5px; border-radius: 20px; display: inline-block; font-weight: bold;'>{skill} ✓</span>"
                                        else:
                                            skill_html += f"<span style='background-color: #f1f1f1; color: #666; padding: 5px 10px; margin: 5px; border-radius: 20px; display: inline-block;'>{skill}</span>"
                                    st.markdown(skill_html, unsafe_allow_html=True)
                                
                                with col_right:
                                    # Add a visual match indicator
                                    st.markdown(f"<div style='background-color: {match_color}; color: white; padding: 10px; border-radius: 5px; text-align: center; margin-bottom: 10px;'><h3 style='margin: 0;'>{job['match_percentage']:.1f}% Match</h3></div>", unsafe_allow_html=True)
                                    
                                    st.markdown(f"**Salary:** {job['salary']}")
                                    st.markdown(f"**Posted:** {job['date_posted']}")
                                    
                                    # Progress bar for match percentage
                                    st.progress(min(job['match_percentage'] / 100, 1.0))
                                    
                                    # View job button with improved styling
                                    st.markdown(f"<a href='{job['url']}' target='_blank' style='display: inline-block; background-color: #2196F3; color: white; padding: 8px 16px; text-align: center; text-decoration: none; border-radius: 4px; margin: 5px 0;'>View Job Posting</a>", unsafe_allow_html=True)
                                    
                                    # Save job button
                                    if st.button(f"Save Job", key=f"save_job_{i}"):
                                        if 'saved_jobs' not in st.session_state:
                                            st.session_state.saved_jobs = []
                                    
                                        # Check if job is already saved
                                        job_ids = [j.get('id', j['title'] + j['company']) for j in st.session_state.saved_jobs]
                                        current_job_id = job.get('id', job['title'] + job['company'])
                                        
                                        if current_job_id not in job_ids:
                                            # Add job to saved jobs
                                            st.session_state.saved_jobs.append(job)
                                            st.success(f"Job saved! You have {len(st.session_state.saved_jobs)} saved jobs.")
                                        else:
                                            st.warning("This job is already in your saved jobs.")
                                            
                                    # Add apply button
                                    col1, col2 = st.columns(2)
                                    with col1:
                                        st.button(f"Apply Now", key=f"apply_job_{i}", help="This is a demo button. In a real app, this would take you to the application page.")
                                    with col2:
                                        if st.button(f"Interview Prep", key=f"interview_prep_{i}"):
                                            st.session_state.show_interview_prep = True
                                            st.session_state.interview_prep_job = job
                                    
                                # Add a section for similar jobs
                                if i < len(display_jobs) - 1:
                                    st.markdown("---")
                                    st.markdown("### Similar Jobs You Might Like")
                                    similar_jobs_html = ""
                                    # Find 2-3 similar jobs based on matching skills
                                    current_skills = set(job['skills_match'])
                                    similar_jobs = []
                                    
                                    for other_job in display_jobs:
                                        if other_job != job:  # Don't include the current job
                                            other_skills = set(other_job['skills_match'])
                                            similarity = len(current_skills.intersection(other_skills)) / len(current_skills.union(other_skills))
                                            if similarity > 0.3:  # Threshold for similarity
                                                similar_jobs.append((other_job, similarity))
                                    
                                    # Sort by similarity and take top 3
                                    similar_jobs.sort(key=lambda x: x[1], reverse=True)
                                    for similar_job, _ in similar_jobs[:3]:
                                        similar_jobs_html += f"<div style='margin: 5px 0;'><a href='#' style='text-decoration: none;'>{similar_job['title']} at {similar_job['company']}</a> - {similar_job['match_percentage']:.1f}% Match</div>"
                                    
                                    if similar_jobs_html:
                                        st.markdown(similar_jobs_html, unsafe_allow_html=True)
                                    else:
                                        st.markdown("No similar jobs found.")
                                        
                        # Add a section for saved jobs if any
                        if 'saved_jobs' in st.session_state and st.session_state.saved_jobs:
                            st.markdown("---")
                            with st.expander(f"Your Saved Jobs ({len(st.session_state.saved_jobs)})", expanded=False):
                                # Add download and clear buttons
                                col1, col2 = st.columns(2)
                                with col1:
                                    if st.button("Download Saved Jobs"):
                                        # Convert saved jobs to CSV
                                        
                                        # Prepare data for CSV
                                        saved_jobs_data = []
                                        for job in st.session_state.saved_jobs:
                                            job_data = {
                                                "Title": job['title'],
                                                "Company": job['company'],
                                                "Location": job['location'],
                                                "Salary": job['salary'],
                                                "Job Type": job.get('job_type', 'Not specified'),
                                                "Experience Level": job.get('experience_level', 'Not specified'),
                                                "Match Percentage": f"{job['match_percentage']:.1f}%",
                                                "URL": job['url'],
                                                "Date Posted": job['date_posted'],
                                                "Matching Skills": ", ".join(job['matching_skills']),
                                                "Required Skills": ", ".join(job['skills_match'])
                                            }
                                            saved_jobs_data.append(job_data)
                                        
                                        # Create DataFrame and CSV
                                        saved_jobs_df = pd.DataFrame(saved_jobs_data)
                                        csv = saved_jobs_df.to_csv(index=False)
                                        
                                        # Create download link
                                        b64 = base64.b64encode(csv.encode()).decode()
                                        href = f'<a href="data:file/csv;base64,{b64}" download="saved_jobs.csv">Download CSV File</a>'
                                        st.markdown(href, unsafe_allow_html=True)
                                
                                with col2:
                                    if st.button("Clear All Saved Jobs"):
                                        st.session_state.saved_jobs = []
                                        st.rerun()
                                
                                # Display saved jobs in a nicer format
                                st.markdown("### Your Saved Job List")
                                for i, saved_job in enumerate(st.session_state.saved_jobs):
                                    with st.container():
                                        col1, col2, col3 = st.columns([3, 1, 1])
                                        with col1:
                                            st.markdown(f"**{i+1}. {saved_job['title']} at {saved_job['company']}**")
                                            st.markdown(f"Location: {saved_job['location']} | Salary: {saved_job['salary']}")
                                            st.markdown(f"Match: {saved_job['match_percentage']:.1f}% | Posted: {saved_job['date_posted']}")
                                        
                                        with col2:
                                            st.markdown(f"[View Job]({saved_job['url']})")
                                        
                                        with col3:
                                            if st.button(f"Remove", key=f"remove_saved_{i}"):
                                                st.session_state.saved_jobs.pop(i)
                                                st.rerun()
                                    st.markdown("---")
                                
                                # Add job application tracker
                                st.markdown("### Job Application Tracker")
                                st.info("Track your application status for saved jobs. This is a demo feature.")
                                
                                # Create a simple application tracker
                                if 'job_applications' not in st.session_state:
                                    st.session_state.job_applications = {}
                                
                                # Display application tracker for saved jobs
                                for i, saved_job in enumerate(st.session_state.saved_jobs):
                                    job_id = saved_job.get('id', saved_job['title'] + saved_job['company'])
                                    
                                    # Initialize if not exists
                                    if job_id not in st.session_state.job_applications:
                                        st.session_state.job_applications[job_id] = {
                                            "status": "Not Applied",
                                            "notes": "",
                                            "date_applied": ""
                                        }
                                    
                                    with st.expander(f"Track: {saved_job['title']} at {saved_job['company']}"):
                                        # Application status
                                        status_options = ["Not Applied", "Applied", "Interview Scheduled", "Interview Completed", "Offer Received", "Rejected", "Not Interested"]
                                        new_status = st.selectbox(
                                            "Application Status",
                                            options=status_options,
                                            index=status_options.index(st.session_state.job_applications[job_id]["status"]),
                                            key=f"status_{job_id}"
                                        )
                                        
                                        # Update status if changed
                                        if new_status != st.session_state.job_applications[job_id]["status"]:
                                            st.session_state.job_applications[job_id]["status"] = new_status
                                            if new_status == "Applied" and not st.session_state.job_applications[job_id]["date_applied"]:
                                                from datetime import date
                                                st.session_state.job_applications[job_id]["date_applied"] = date.today().strftime("%Y-%m-%d")
                                        
                                        # Date applied
                                        date_applied = st.date_input(
                                            "Date Applied",
                                            value=None if not st.session_state.job_applications[job_id]["date_applied"] else 
                                                    datetime.strptime(st.session_state.job_applications[job_id]["date_applied"], "%Y-%m-%d"),
                                            key=f"date_{job_id}"
                                        )
                                        
                                        # Update date if changed
                                        if date_applied:
                                            st.session_state.job_applications[job_id]["date_applied"] = date_applied.strftime("%Y-%m-%d")
                                        
                                        # Notes
                                        notes = st.text_area(
                                            "Notes",
                                            value=st.session_state.job_applications[job_id]["notes"],
                                            key=f"notes_{job_id}"
                                        )
                                        
                                        # Update notes if changed
                                        if notes != st.session_state.job_applications[job_id]["notes"]:
                                            st.session_state.job_applications[job_id]["notes"] = notes
                                        
                                        # Check if job is already saved
                                        job_titles = [j['title'] for j in st.session_state.saved_jobs]
                                        if job['title'] not in job_titles:
                                            st.session_state.saved_jobs.append(job)
                                            st.success(f"Saved {job['title']} to your saved jobs!")
                                        else:
                                            st.info("This job is already in your saved jobs.")
                        
                        # Email job recommendations feature
                        with st.expander("Email Job Recommendations"):
                            st.markdown("### Email These Job Recommendations")
                            st.markdown("Send these job recommendations to your email for later reference.")
                            
                            # Email form
                            email = st.text_input("Your Email Address", placeholder="example@email.com")
                            include_options = st.multiselect(
                                "What to include in the email?",
                                options=["All Jobs", "Saved Jobs Only", "Job Details", "Skill Match Information", "Analytics Summary"],
                                default=["All Jobs", "Job Details"]
                            )
                            
                            # Additional message
                            additional_message = st.text_area("Additional Message (Optional)", 
                                                        placeholder="Add any notes or reminders about these job recommendations.")
                            
                            # Send button
                            if st.button("Send Email"):
                                if email and "@" in email and "." in email:
                                    # This is a mock email function since we can't actually send emails in this demo
                                    # In a real application, you would integrate with an email service
                                    st.success(f"📧 Email would be sent to {email} with your job recommendations!")
                                    st.info("This is a demo feature. In a real application, this would send an actual email.")
                                else:
                                    st.error("Please enter a valid email address.")
                            
                            st.markdown("")
                            st.markdown("**Note:** In a real application, this feature would:")
                            st.markdown("1. Format job recommendations in a professional email template")
                            st.markdown("2. Include direct links to apply to each position")
                            st.markdown("3. Provide a calendar integration to schedule application follow-ups")
                            st.markdown("4. Allow setting up job alerts for similar positions")
                        
                        # Provide a download button for the job recommendations
                        col1, col2 = st.columns([3, 1])
                        with col1:
                            jobs_data = {
                                "job_recommendations": sorted_jobs,
                                "search_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                "search_criteria": {
                                    "skills": selected_skills if selected_skills else st.session_state.extracted_skills,
                                    "location": location,
                                    "experience_level": experience_filter,
                                    "job_type": job_type_filter
                                }
                            }
                            jobs_json = json.dumps(jobs_data, indent=4)
                            st.download_button(
                                label="Download Job Recommendations",
                                data=jobs_json,
                                file_name="job_recommendations.json",
                                mime="application/json"
                            )
                        
                        with col2:
                            if st.button("Job Market Analytics"):
                                st.session_state.show_job_analytics = True
                        
                        # Interview Preparation Feature
                        if 'show_interview_prep' in st.session_state and st.session_state.show_interview_prep and 'interview_prep_job' in st.session_state:
                            with st.expander("Interview Preparation Guide", expanded=True):
                                job = st.session_state.interview_prep_job
                                st.markdown(f"### Interview Preparation for: {job['title']} at {job['company']}")
                                
                                # Create tabs for different interview preparation aspects
                                prep_tabs = st.tabs(["Key Skills", "Common Questions", "Technical Prep", "Company Research", "Your Strengths"])
                                
                                # Tab 1: Key Skills
                                with prep_tabs[0]:
                                    st.markdown("### Key Skills for This Position")
                                    st.markdown("Focus on these skills during your interview preparation:")
                                    
                                    # Divide skills into categories
                                    technical_skills = []
                                    soft_skills = []
                                    domain_skills = []
                                    
                                    # This is a simplified categorization - in a real app, you'd use NLP or a predefined categorization
                                    tech_keywords = ["python", "java", "javascript", "react", "angular", "vue", "node", "express", "django", 
                                                        "flask", "sql", "nosql", "mongodb", "aws", "azure", "gcp", "docker", "kubernetes", 
                                                        "ci/cd", "git", "algorithm", "data structure", "machine learning", "ai", "frontend", "backend"]
                                    
                                    soft_keywords = ["communication", "teamwork", "leadership", "problem solving", "critical thinking", 
                                                        "time management", "adaptability", "creativity", "emotional intelligence", "conflict resolution", 
                                                        "negotiation", "presentation", "collaboration", "agile", "scrum"]
                                    
                                    domain_keywords = ["finance", "healthcare", "education", "retail", "e-commerce", "marketing", 
                                                        "sales", "hr", "customer service", "logistics", "supply chain", "manufacturing", 
                                                        "consulting", "legal", "media", "entertainment", "gaming", "travel", "hospitality"]
                                    
                                    for skill in job['skills_match']:
                                        skill_lower = skill.lower()
                                        if any(keyword in skill_lower for keyword in tech_keywords):
                                            technical_skills.append(skill)
                                        elif any(keyword in skill_lower for keyword in soft_keywords):
                                            soft_skills.append(skill)
                                        elif any(keyword in skill_lower for keyword in domain_keywords):
                                            domain_skills.append(skill)
                                        else:
                                            # Default to technical if not categorized
                                            technical_skills.append(skill)
                                    
                                    # Display skills by category with preparation tips
                                    col1, col2 = st.columns(2)
                                    
                                    with col1:
                                        st.markdown("#### Technical Skills")
                                        for skill in technical_skills:
                                            if skill in job['matching_skills']:
                                                st.markdown(f"- **{skill}** ✓ *You have this skill*")
                                                st.markdown(f"  - Prepare examples of how you've used {skill} in past projects")
                                                st.markdown(f"  - Be ready to discuss your proficiency level")
                                            else:
                                                st.markdown(f"- **{skill}** ⚠️ *Skill gap*")
                                                st.markdown(f"  - Research basics of {skill} before the interview")
                                                st.markdown(f"  - Prepare to discuss how you plan to learn this skill")
                                        
                                        if domain_skills:
                                            st.markdown("#### Domain Knowledge")
                                            for skill in domain_skills:
                                                if skill in job['matching_skills']:
                                                    st.markdown(f"- **{skill}** ✓")
                                                else:
                                                    st.markdown(f"- **{skill}** ⚠️")
                                    
                                    with col2:
                                        st.markdown("#### Soft Skills")
                                        for skill in soft_skills:
                                            if skill in job['matching_skills']:
                                                st.markdown(f"- **{skill}** ✓")
                                            else:
                                                st.markdown(f"- **{skill}** ⚠️")
                                        
                                        # Skill gap analysis
                                        missing_skills = [s for s in job['skills_match'] if s not in job['matching_skills']]
                                        if missing_skills:
                                            st.markdown("#### Skill Gap Strategy")
                                            st.markdown(f"You're missing {len(missing_skills)} out of {len(job['skills_match'])} required skills.")
                                            st.markdown("Preparation strategy:")
                                            st.markdown("1. Focus on transferable skills from your experience")
                                            st.markdown("2. Prepare examples of quick learning ability")
                                            st.markdown("3. Show enthusiasm for learning these skills")
                                
                                # Tab 2: Common Questions
                                with prep_tabs[1]:
                                    st.markdown("### Common Interview Questions")
                                    st.markdown("Prepare answers for these likely questions based on the job requirements:")
                                    
                                    # Generate questions based on job details and skills
                                    questions = [
                                        f"Tell me about your experience with {', '.join(job['matching_skills'][:3])}.",
                                        f"How would you approach a project that requires {', '.join(job['skills_match'][:3])}?",
                                        f"Describe a challenging situation you faced while working with {job['matching_skills'][0] if job['matching_skills'] else 'a team'}.",
                                        f"Why are you interested in working at {job['company']}?",
                                        f"How does this {job['title']} role align with your career goals?",
                                        "What's your greatest professional achievement?",
                                        "How do you handle tight deadlines and pressure?",
                                        "Describe your ideal work environment.",
                                        f"What do you know about {job['company']}?",
                                        "Where do you see yourself in 5 years?"
                                    ]
                                    
                                    # Add some technical questions based on skills
                                    technical_questions = []
                                    if any("python" in s.lower() for s in job['skills_match']):
                                        technical_questions.append("Explain the difference between lists and tuples in Python.")
                                    if any("javascript" in s.lower() for s in job['skills_match']):
                                        technical_questions.append("What is the difference between '==' and '===' in JavaScript?")
                                    if any("sql" in s.lower() for s in job['skills_match']):
                                        technical_questions.append("Explain the difference between INNER JOIN and LEFT JOIN in SQL.")
                                    if any("react" in s.lower() for s in job['skills_match']):
                                        technical_questions.append("What are React hooks and why are they useful?")
                                    if any("data" in s.lower() for s in job['skills_match']):
                                        technical_questions.append("How would you handle missing data in a dataset?")
                                    
                                    # Display behavioral questions
                                    st.markdown("#### Behavioral Questions")
                                    for i, question in enumerate(questions):
                                        with st.expander(f"Q{i+1}: {question}"):
                                            st.markdown("**Preparation Tips:**")
                                            st.markdown("- Use the STAR method: Situation, Task, Action, Result")
                                            st.markdown("- Keep your answer concise (1-2 minutes)")
                                            st.markdown("- Include quantifiable achievements when possible")
                                            st.markdown("- Connect your answer to the job requirements")
                                            
                                            # Add a text area for the user to practice their answer
                                            st.text_area("Practice your answer here:", key=f"answer_{i}", height=100)
                                    
                                    # Display technical questions if any
                                    if technical_questions:
                                        st.markdown("#### Technical Questions")
                                        for i, question in enumerate(technical_questions):
                                            with st.expander(f"TQ{i+1}: {question}"):
                                                st.markdown("**Preparation Tips:**")
                                                st.markdown("- Be clear and concise in your explanation")
                                                st.markdown("- Use examples to demonstrate your understanding")
                                                st.markdown("- If you don't know, explain how you would find the answer")
                                                
                                                # Add a text area for the user to practice their answer
                                                st.text_area("Practice your answer here:", key=f"tech_answer_{i}", height=100)
                                
                                # Tab 3: Technical Prep
                                with prep_tabs[2]:
                                    st.markdown("### Technical Preparation")
                                    st.markdown("Prepare for technical aspects of the interview based on job requirements:")
                                    
                                    # Technical preparation recommendations
                                    if technical_skills:
                                        st.markdown("#### Technical Topics to Review")
                                        for skill in technical_skills:
                                            with st.expander(f"Prepare for: {skill}"):
                                                st.markdown(f"**Key Concepts in {skill}:**")
                                                st.markdown("- Review fundamental concepts and recent developments")
                                                st.markdown("- Prepare to discuss projects where you've applied this skill")
                                                st.markdown("- Be ready to solve problems related to this skill")
                                                
                                                # Add mock technical questions
                                                st.markdown("**Sample Technical Questions:**")
                                                st.markdown(f"1. Explain how you've used {skill} in a past project")
                                                st.markdown(f"2. What are the advantages and limitations of {skill}?")
                                                st.markdown(f"3. How would you solve [specific problem] using {skill}?")
                                                
                                                # Add resources for preparation
                                                st.markdown("**Resources for Preparation:**")
                                                st.markdown(f"- Online courses on {skill}")
                                                st.markdown(f"- Technical documentation for {skill}")
                                                st.markdown(f"- Practice problems related to {skill}")
                                    
                                    # Code challenge preparation if relevant
                                    if any(keyword in job['title'].lower() for keyword in ["developer", "engineer", "programmer", "coder"]):
                                        st.markdown("#### Coding Challenge Preparation")
                                        st.markdown("Many technical interviews include coding challenges. Prepare by:")
                                        st.markdown("1. Practicing algorithm problems on platforms like LeetCode or HackerRank")
                                        st.markdown("2. Reviewing data structures (arrays, linked lists, trees, graphs, etc.)")
                                        st.markdown("3. Practicing explaining your thought process while coding")
                                        st.markdown("4. Reviewing time and space complexity analysis")
                                        
                                        # Sample coding challenge
                                        with st.expander("Sample Coding Challenge"):
                                            st.markdown("**Problem:** Write a function to find the most frequent element in an array.")
                                            st.markdown("**Input:** An array of elements")
                                            st.markdown("**Output:** The most frequent element in the array")
                                            
                                            # Code editor for practice
                                            st.markdown("**Practice your solution:**")
                                            st.code("""
# Write your solution here
def find_most_frequent(arr):
    # Your code here
    pass

# Test cases
print(find_most_frequent([1, 2, 3, 2, 2, 3, 1, 2]))
# Expected output: 2
                                            """, language="python")
                                
                                # Tab 4: Company Research
                                with prep_tabs[3]:
                                    st.markdown("### Company Research")
                                    st.markdown(f"Research {job['company']} before your interview:")
                                    
                                    # Company research guidance
                                    col1, col2 = st.columns(2)
                                    
                                    with col1:
                                        st.markdown("#### What to Research")
                                        st.markdown("1. **Company Mission and Values**")
                                        st.markdown("2. **Products and Services**")
                                        st.markdown("3. **Recent News and Developments**")
                                        st.markdown("4. **Company Culture**")
                                        st.markdown("5. **Competitors and Market Position**")
                                        st.markdown("6. **Leadership Team**")
                                        st.markdown("7. **Financial Performance (if public)**")
                                    
                                    with col2:
                                        st.markdown("#### Where to Research")
                                        st.markdown("1. **Company Website**")
                                        st.markdown("2. **LinkedIn Company Page**")
                                        st.markdown("3. **Glassdoor Reviews**")
                                        st.markdown("4. **News Articles**")
                                        st.markdown("5. **Annual Reports**")
                                        st.markdown("6. **Social Media Accounts**")
                                        st.markdown("7. **Current Employees (if possible)**")
                                    
                                    # Questions to ask the interviewer
                                    st.markdown("#### Questions to Ask the Interviewer")
                                    st.markdown("Prepare thoughtful questions to ask at the end of the interview:")
                                    
                                    questions_to_ask = [
                                        "What does success look like in this role in the first 90 days?",
                                        "How would you describe the team culture?",
                                        "What are the biggest challenges facing the team/department right now?",
                                        "How does this role contribute to the company's overall goals?",
                                        "What opportunities for professional development are available?",
                                        "Can you tell me about the team I'll be working with?",
                                        "What's your favorite part about working at this company?",
                                        "What are the next steps in the interview process?"
                                    ]
                                    
                                    for i, question in enumerate(questions_to_ask):
                                        st.markdown(f"{i+1}. {question}")
                                    
                                    # Company research notes
                                    st.markdown("#### Your Research Notes")
                                    st.text_area("Take notes on your company research here:", height=150, key="company_research")
                                
                                # Tab 5: Your Strengths
                                with prep_tabs[4]:
                                    st.markdown("### Highlight Your Strengths")
                                    st.markdown("Prepare to showcase your relevant strengths for this position:")
                                    
                                    # Strengths based on matching skills
                                    st.markdown("#### Your Matching Skills")
                                    st.markdown("These are your strengths that align with the job requirements:")
                                    
                                    if job['matching_skills']:
                                        for skill in job['matching_skills']:
                                            st.markdown(f"- **{skill}**")
                                            st.text_area(f"Prepare an example of how you've demonstrated {skill}:", key=f"strength_{skill}", height=100)
                                    else:
                                        st.warning("No direct skill matches found. Focus on transferable skills and learning ability.")
                                    
                                    # Prepare your elevator pitch
                                    st.markdown("#### Your Elevator Pitch")
                                    st.markdown("Prepare a 30-60 second introduction that highlights your relevant experience and interest in the role:")
                                    st.text_area("Draft your elevator pitch here:", height=150, key="elevator_pitch")
                                    
                                    # Prepare examples using the STAR method
                                    st.markdown("#### STAR Method Examples")
                                    st.markdown("Prepare examples from your experience using the STAR method (Situation, Task, Action, Result):")
                                    
                                    star_template = """**Situation:** Describe the context and background

**Task:** Explain the challenge or responsibility you faced

**Action:** Detail the specific actions you took

**Result:** Share the outcomes and what you learned"""
                                    
                                    with st.expander("Example 1: Problem Solving"):
                                        st.text_area("Prepare a STAR example about problem solving:", star_template, key="star_1", height=200)
                                    
                                    with st.expander("Example 2: Teamwork"):
                                        st.text_area("Prepare a STAR example about teamwork:", star_template, key="star_2", height=200)
                                    
                                    with st.expander("Example 3: Technical Achievement"):
                                        st.text_area("Prepare a STAR example about a technical achievement:", star_template, key="star_3", height=200)
                                
                                # Close button
                                if st.button("Close Interview Prep"):
                                    st.session_state.show_interview_prep = False
                                    st.rerun()
                        
                        # Job Market Analytics
                        if 'show_job_analytics' in st.session_state and st.session_state.show_job_analytics:
                            with st.expander("Job Market Analytics", expanded=True):
                                st.markdown("### Job Market Insights")
                                st.markdown("Analysis based on your current job search results.")
                                
                                # Prepare data for analysis
                                jobs = sorted_jobs
                                
                                # 1. Salary Distribution
                                st.subheader("Salary Distribution")
                                
                                # Extract numeric salary values (assuming format like "$X - $Y")
                                salary_data = []
                                for job in jobs:
                                    salary = job.get('salary', '$0')
                                    if '-' in salary:
                                        try:
                                            parts = salary.replace('$', '').replace(',', '').split('-')
                                            min_part = float(parts[0].strip().split('/')[0])
                                            max_part = float(parts[1].strip().split('/')[0])
                                            avg_salary = (min_part + max_part) / 2
                                            salary_data.append(avg_salary)
                                        except:
                                            pass
                                
                                if salary_data:
                                    fig, ax = plt.subplots(figsize=(10, 4))
                                    ax.hist(salary_data, bins=10, alpha=0.7, color='#2196F3')
                                    ax.set_xlabel('Salary ($)')
                                    ax.set_ylabel('Number of Jobs')
                                    ax.set_title('Salary Distribution')
                                    ax.grid(axis='y', alpha=0.75)
                                    st.pyplot(fig)
                                    
                                    # Salary statistics
                                    col1, col2, col3 = st.columns(3)
                                    with col1:
                                        st.metric("Average Salary", f"${np.mean(salary_data):,.2f}")
                                    with col2:
                                        st.metric("Median Salary", f"${np.median(salary_data):,.2f}")
                                    with col3:
                                        st.metric("Salary Range", f"${min(salary_data):,.0f} - ${max(salary_data):,.0f}")
                                else:
                                    st.info("Not enough salary data available for analysis.")
                                
                                # 2. Job Types Distribution
                                st.subheader("Job Types")
                                job_types = [job.get('job_type', 'Not specified') for job in jobs]
                                job_type_counts = {}
                                for jt in job_types:
                                    if jt in job_type_counts:
                                        job_type_counts[jt] += 1
                                    else:
                                        job_type_counts[jt] = 1
                                
                                # Create pie chart for job types
                                if job_type_counts:
                                    fig, ax = plt.subplots(figsize=(8, 6))
                                    ax.pie(job_type_counts.values(), labels=job_type_counts.keys(), autopct='%1.1f%%', 
                                            startangle=90, shadow=False, explode=[0.05]*len(job_type_counts))
                                    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
                                    st.pyplot(fig)
                                
                                # 3. Most In-Demand Skills
                                st.subheader("Most In-Demand Skills")
                                
                                # Collect all skills from job listings
                                all_skills = {}
                                for job in jobs:
                                    for skill in job['skills_match']:
                                        if skill in all_skills:
                                            all_skills[skill] += 1
                                        else:
                                            all_skills[skill] = 1
                                
                                # Sort skills by frequency
                                sorted_skills = sorted(all_skills.items(), key=lambda x: x[1], reverse=True)
                                top_skills = sorted_skills[:15]  # Get top 15 skills
                                
                                if top_skills:
                                    # Create horizontal bar chart
                                    fig, ax = plt.subplots(figsize=(10, 8))
                                    y_pos = np.arange(len(top_skills))
                                    skill_names = [skill[0] for skill in top_skills]
                                    skill_counts = [skill[1] for skill in top_skills]
                                    
                                    # Create horizontal bars
                                    bars = ax.barh(y_pos, skill_counts, align='center', alpha=0.7, color='#4CAF50')
                                    ax.set_yticks(y_pos)
                                    ax.set_yticklabels(skill_names)
                                    ax.invert_yaxis()  # Labels read top-to-bottom
                                    ax.set_xlabel('Number of Job Listings')
                                    ax.set_title('Most In-Demand Skills')
                                    
                                    # Add count labels to the bars
                                    for i, v in enumerate(skill_counts):
                                        ax.text(v + 0.1, i, str(v), va='center')
                                    
                                    st.pyplot(fig)
                                    
                                    # Your skills coverage
                                    user_skills = set()
                                    for job in jobs:
                                        user_skills.update(job['matching_skills'])
                                    
                                    top_skill_names = set(skill[0] for skill in top_skills)
                                    user_top_skills = user_skills.intersection(top_skill_names)
                                    
                                    st.info(f"You have {len(user_top_skills)} of the top {len(top_skills)} in-demand skills ({len(user_top_skills)/len(top_skills)*100:.1f}%).")
                                    
                                    # Suggest skills to learn
                                    missing_top_skills = top_skill_names - user_skills
                                    if missing_top_skills:
                                        st.markdown("**Skills to consider learning:**")
                                        for i, skill in enumerate(list(missing_top_skills)[:5]):
                                            st.markdown(f"- {skill}")
                                
                                # Close analytics button
                                if st.button("Close Analytics"):
                                    st.session_state.show_job_analytics = False
                                    st.rerun()
                else:
                    st.warning("No jobs found matching your criteria. Try adjusting your filters or adding more skills.")
        else:
            st.warning("Please upload your resume in the Resume Analyzer tab first.")

    # Career Advisor Tab
    with tabs[2]:
        st.header("Career Advisor Bot")
        st.markdown("Get personalized career advice based on your skills and experience.")
        
        # Check if skills have been extracted
        if st.session_state.extracted_skills:
            st.success(f"Found {len(st.session_state.extracted_skills)} skills from your resume.")
            
            # Career goals input
            st.subheader("Your Career Goals")
            career_goal = st.text_area("What are your career goals for the next 1-3 years?", 
                                        placeholder="E.g., I want to transition into a data science role, or I want to advance to a senior position in my current field.")
            
            # Work preferences
            st.subheader("Work Preferences")
            col1, col2 = st.columns(2)
            
            with col1:
                work_environment = st.selectbox(
                    "Preferred Work Environment",
                    ["Remote", "Hybrid", "On-site", "No preference"]
                )
                
                industry_interest = st.multiselect(
                    "Industries of Interest",
                    ["Technology", "Healthcare", "Finance", "Education", "Manufacturing", 
                    "Retail", "Media", "Government", "Non-profit", "Consulting"],
                    default=["Technology"]
                )
            
            with col2:
                company_size = st.selectbox(
                    "Preferred Company Size",
                    ["Startup", "Small (10-100 employees)", "Medium (100-1000 employees)", 
                    "Large (1000+ employees)", "No preference"]
                )
                
                work_life_balance = st.slider(
                    "Importance of Work-Life Balance",
                    min_value=1,
                    max_value=10,
                    value=7,
                    help="1 = Not important, 10 = Extremely important"
                )
            
            # Skills to develop
            st.subheader("Skills Development")
            skill_interests = st.multiselect(
                "Select areas you're interested in developing further",
                ["Technical Skills", "Leadership", "Project Management", "Communication", 
                "Data Analysis", "Design", "Marketing", "Sales", "Research", "Product Management"],
                default=["Technical Skills", "Leadership"]
            )
            
            # Generate advice button
            if st.button("Generate Career Advice"):
                with st.spinner("Analyzing your profile and generating personalized career advice..."):
                    # Get years of experience if available
                    years_exp = st.session_state.get('years_of_experience', 0)
                    education = st.session_state.get('education', [])
                    
                    # Collect work preferences
                    work_preferences = {
                        "environment": work_environment,
                        "industry": industry_interest,
                        "company_size": company_size,
                        "work_life_balance": work_life_balance
                    }
                    
                    # Generate career advice based on extracted skills and additional inputs
                    advice = generate_career_advice(st.session_state.extracted_skills, career_goal, work_preferences, skill_interests)
                    st.session_state.career_advice = advice
            
            # Display career advice
            if st.session_state.career_advice:
                advice = st.session_state.career_advice
                
                # Create tabs for different sections of advice
                advice_tabs = st.tabs(["Overview", "Career Paths", "Skill Development", "Learning Resources"])
                
                # Overview tab
                with advice_tabs[0]:
                    st.markdown("### Your Career Profile")
                    st.subheader(f"Career Advice for {advice['top_field']}")
                    
                    # Strengths and areas for improvement
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown("#### Your Strengths")
                        st.markdown("- Strong technical foundation")
                        st.markdown("- Specialized knowledge in your field")
                        st.markdown("- Adaptable to new technologies")
                    
                    with col2:
                        st.markdown("#### Areas for Development")
                        st.markdown("- Leadership and management skills")
                        st.markdown("- Cross-functional collaboration")
                        st.markdown("- Advanced certifications")
                
                # Career Paths tab
                with advice_tabs[1]:
                    st.markdown("### 🛣️ Recommended Career Paths")
                    st.markdown("Based on your skills, experience, and preferences, here are some career paths to consider:")
                    
                    for i, path in enumerate(advice['career_paths']):
                        with st.expander(f"{path}"):
                            st.markdown(f"**{path}**")
                            st.markdown("This career path aligns with your current skills and future goals.")
                            
                            # Display match percentage
                            match_percentage = 85
                            st.markdown(f"**Match with your profile:** {match_percentage}%")
                            st.progress(match_percentage/100)
                            
                            # Potential job titles
                            st.markdown("**Potential Job Titles:**")
                            st.markdown(f"Senior {path}, Lead {path}, {path} Architect")
                            
                            # Salary range
                            st.markdown(f"**Typical Salary Range:** $90,000 - $150,000")
                
                # Skill Development tab
                with advice_tabs[2]:
                    st.markdown("### 🧠 Skill Development Plan")
                    
                    # Short-term skills (3-6 months)
                    st.markdown("#### Short-term (3-6 months)")
                    for i, skill in enumerate(advice['skill_recommendations'][:3]):
                        st.markdown(f"- **{skill}**: Essential for career advancement")
                    
                    # Medium-term skills (6-12 months)
                    st.markdown("#### Medium-term (6-12 months)")
                    for i, skill in enumerate(advice['skill_recommendations'][3:6] if len(advice['skill_recommendations']) > 3 else []):
                        st.markdown(f"- **{skill}**: Important for specialization")
                    
                    # Long-term skills (1-2 years)
                    st.markdown("#### Long-term (1-2 years)")
                    for i, skill in enumerate(advice['skill_recommendations'][6:] if len(advice['skill_recommendations']) > 6 else []):
                        st.markdown(f"- **{skill}**: Valuable for leadership roles")
                
                # Learning Resources tab
                with advice_tabs[3]:
                    st.markdown("### 📚 Learning Resources")
                    
                    # Filter resources by category
                    resource_categories = ["All", "Courses", "Books", "Certifications", "Communities"]
                    selected_category = st.selectbox("Filter by category", resource_categories)
                    
                    # Display resources
                    for i, resource in enumerate(advice['learning_resources']):
                        with st.expander(f"{resource}"):
                            st.markdown(f"**{resource}**")
                            st.markdown("Comprehensive learning resource for skill development")
                            st.markdown(f"[Learn More](https://example.com/resource/{i})")
                            
                            # Display cost and time commitment
                            col1, col2 = st.columns(2)
                            with col1:
                                st.markdown("**Cost:** $0-$499")
                            with col2:
                                st.markdown("**Time Commitment:** 4-8 weeks")
                    
                    # Display industry trends
                    st.markdown("### 📈 Industry Trends")
                    st.markdown(advice['industry_trends'])
                
                # Provide a download button for the career advice
                advice_data = {
                    "career_advice": st.session_state.career_advice,
                    "generation_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "user_inputs": {
                        "career_goal": career_goal,
                        "work_preferences": {
                            "environment": work_environment,
                            "industry": industry_interest,
                            "company_size": company_size,
                            "work_life_balance": work_life_balance
                        },
                        "skill_interests": skill_interests
                    }
                }
                advice_json = json.dumps(advice_data, indent=4)
                st.download_button(
                    label="Download Career Advice",
                    data=advice_json,
                    file_name="career_advice.json",
                    mime="application/json"
                )
        else:
            st.warning("Please upload your resume in the Resume Analyzer tab first.")

# --- App Entry Point ---

def main():
    # Page Config MUST be the first command in main
    st.set_page_config(page_title="HireIQ", page_icon="💼", layout="wide")

    # 1. Initialize Session State variables
    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False
    
    if 'username' not in st.session_state:
        st.session_state['username'] = None
        
    # 2. Initialize the User Database
    init_user_db()

    # 3. Authentication Check
    if not st.session_state['authenticated']:
        show_login_page()
    else:
        # If logged in, show the main application
        # NOTE: Ensure Hire_IQ_app() does NOT have st.set_page_config inside it
        Hire_IQ_app()

if __name__ == "__main__":
    main()