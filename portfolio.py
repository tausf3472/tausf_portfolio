import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="MD Tausif Ahmad | Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS FOR STYLING ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #f0f2f6;
    }
    
    /* Typography */
    h1, h2, h3 {
        font-family: 'Helvetica', sans-serif;
        color: #0e1117;
    }
    h1 {
        text-align: center;
        color: #0056b3; /* Professional Blue */
        font-weight: 800;
        margin-bottom: 5px;
    }
    h2 {
        text-align: center;
        margin-top: 40px;
        margin-bottom: 20px;
        border-bottom: 2px solid #d32f2f; /* Accent Red */
        display: inline-block;
        padding-bottom: 10px;
        text-transform: uppercase;
        font-size: 1.5rem;
        letter-spacing: 1px;
    }
    
    /* Header & Contact */
    .header-subtitle {
        text-align: center;
        color: #555;
        font-size: 1.2rem;
        font-weight: 500;
        margin-bottom: 15px;
    }
    .contact-info {
        text-align: center;
        font-size: 1rem;
        color: #333;
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin: 0 auto 20px auto;
        max-width: 800px;
    }
    .contact-info a {
        text-decoration: none;
        color: #0056b3;
        font-weight: bold;
        margin: 0 10px;
    }
    .contact-info a:hover {
        text-decoration: underline;
    }
    
    /* Card Styling */
    .css-card {
        background-color: white;
        padding: 25px;
        border-radius: 12px;
        box_shadow: 0 4px 6px rgba(0,0,0,0.08);
        margin-bottom: 20px;
        border-left: 5px solid #0056b3;
        transition: transform 0.2s;
    }
    .css-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.12);
    }
    
    /* Experience Components */
    .exp-title {
        font-weight: 700;
        color: #2c3e50;
        font-size: 1.15rem;
    }
    .exp-company {
        color: #555;
        font-weight: 500;
        font-size: 1rem;
    }
    .exp-date {
        color: #d32f2f;
        font-weight: 600;
        font-size: 0.9rem;
        float: right;
    }
    
    /* Skills */
    .skill-tag {
        display: inline-block;
        background-color: #e8f0fe;
        color: #1557b0;
        padding: 6px 12px;
        margin: 4px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        border: 1px solid #b3d7ff;
    }
    
    /* Footer */
    footer {visibility: hidden;}
    .footer-text {
        text-align: center;
        color: #888;
        font-size: 0.8rem;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("<h1>MD TAUSIF AHMAD</h1>", unsafe_allow_html=True)
st.markdown("<div class='header-subtitle'>B.Tech in Computer Science (Data Science)</div>", unsafe_allow_html=True)

# Contact Info Bar
st.markdown("""
<div class='contact-info'>
    📞 +91 7488871375 &nbsp;|&nbsp; 
    ✉️ <a href='mailto:ahmadtausif2004@gmail.com'>Email</a> &nbsp;|&nbsp; 
    🔗 <a href='https://linkedin.com/in/mohammad-tausif-ahmad' target='_blank'>LinkedIn</a> &nbsp;|&nbsp; 
    💻 <a href='https://github.com/tausf3472' target='_blank'>GitHub</a> <br>
    📍 Bokaro, Jharkhand, India
</div>
""", unsafe_allow_html=True)

# --- EDUCATION SECTION ---
st.markdown("<center><h2>Education</h2></center>", unsafe_allow_html=True)
col_edu1, col_edu2 = st.columns(2)

with col_edu1:
    st.markdown("""
    <div class="css-card">
        <div style="font-size:1.1rem; font-weight:bold;">Guru Gobind Singh Educational Society’s Technical Campus</div>
        <div><i>Bachelor of Technology in Computer Science (Data Science)</i></div>
        <div style="color:#d32f2f; font-weight:bold; margin-top:5px;">May 2027 (Expected)</div>
        <div style="margin-top:10px; font-size:0.9rem;">
        <b>Coursework:</b> Data Structures, Algorithms, Machine Learning, Database Systems
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_edu2:
    st.markdown("""
    <div class="css-card">
        <div style="font-size:1.1rem; font-weight:bold;">Ran Vijay Smarak Mahavidyalaya</div>
        <div><i>Intermediate (Science)</i></div>
        <div style="color:#d32f2f; font-weight:bold; margin-top:5px;">Passout 2023</div>
        <div style="margin-top:10px; font-size:0.9rem;">
        Focus on Physics, Chemistry, and Mathematics
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- PROFESSIONAL EXPERIENCE ---
st.markdown("<center><h2>Professional Experience</h2></center>", unsafe_allow_html=True)

# Role 1
st.markdown("""
<div class="css-card">
    <span class="exp-date">Dec 2025 – Jun 2026</span>
    <div class="exp-title">Data Science Engineer Intern</div>
    <div class="exp-company">Internship Studio | Remote</div>
    <hr style="margin: 10px 0; border-top: 1px solid #eee;">
    <ul>
        <li>Developing scalable data pipelines and ETL processes to transform raw data into actionable business insights.</li>
        <li>Building and optimizing machine learning models using Scikit-learn, achieving measurable performance improvements.</li>
        <li>Deploying predictive models to production and creating interactive dashboards for stakeholder decision-making.</li>
        <li>Collaborating with cross-functional teams to define data requirements and deliver analytics solutions.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Role 2
st.markdown("""
<div class="css-card">
    <span class="exp-date">Dec 2025 – Feb 2026</span>
    <div class="exp-title">Python Developer Intern</div>
    <div class="exp-company">Technex, IIT (BHU) | Varanasi, India</div>
    <hr style="margin: 10px 0; border-top: 1px solid #eee;">
    <ul>
        <li>Developing and maintaining Python applications for India’s largest technical festival, serving 50,000+ participants.</li>
        <li>Automating repetitive workflows using Python scripts, reducing manual processing time by 70%.</li>
        <li>Conducting code reviews and implementing best practices to ensure code quality and maintainability.</li>
        <li>Collaborating with distributed teams using Git version control and Agile sprint methodologies.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Role 3
st.markdown("""
<div class="css-card">
    <span class="exp-date">Sep 2025 – Nov 2025</span>
    <div class="exp-title">Python Developer Intern</div>
    <div class="exp-company">Main Flow Services and Technologies Pvt. Ltd. | Remote</div>
    <hr style="margin: 10px 0; border-top: 1px solid #eee;">
    <ul>
        <li>Engineered scalable Python applications following SOLID principles and design patterns.</li>
        <li>Optimized legacy code, improving application performance by 40% through profiling and refactoring.</li>
        <li>Participated in full SDLC including sprint planning, daily stand-ups, and retrospectives in an Agile environment.</li>
        <li>Debugged complex issues using systematic troubleshooting and implemented comprehensive unit tests.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Role 4
st.markdown("""
<div class="css-card">
    <span class="exp-date">Jun 2025 – Aug 2025</span>
    <div class="exp-title">Cybersecurity & Python Programming Intern</div>
    <div class="exp-company">Guru Gobind Singh Educational Society’s Technical Campus</div>
    <hr style="margin: 10px 0; border-top: 1px solid #eee;">
    <ul>
        <li>Implemented security-focused Python applications including encryption algorithms and vulnerability scanners.</li>
        <li>Demonstrated rapid learning ability by mastering new security protocols and frameworks within tight deadlines.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Role 5
st.markdown("""
<div class="css-card">
    <span class="exp-date">Jun 2024 – Jul 2024</span>
    <div class="exp-title">Python Programming & Cryptography Intern</div>
    <div class="exp-company">Guru Gobind Singh Educational Society’s Technical Campus</div>
    <hr style="margin: 10px 0; border-top: 1px solid #eee;">
    <ul>
        <li>Developed cryptographic applications implementing RSA, AES, and hash functions in Python.</li>
        <li>Enhanced algorithmic problem-solving skills through hands-on projects and code optimization challenges.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# --- SKILLS SECTION ---
st.markdown("<center><h2>Technical Skills</h2></center>", unsafe_allow_html=True)

s_col1, s_col2, s_col3 = st.columns(3)

with s_col1:
    with st.container(border=True):
        st.subheader("Languages & Core")
        st.markdown("""
        <span class="skill-tag">Python</span>
        <span class="skill-tag">SQL</span>
        <span class="skill-tag">HTML</span>
        <span class="skill-tag">Data Structures</span>
        <span class="skill-tag">Algorithms</span>
        <span class="skill-tag">Cryptography</span>
        """, unsafe_allow_html=True)

with s_col2:
    with st.container(border=True):
        st.subheader("Data Science")
        st.markdown("""
        <span class="skill-tag">Pandas</span>
        <span class="skill-tag">NumPy</span>
        <span class="skill-tag">Scikit-learn</span>
        <span class="skill-tag">Feature Engineering</span>
        <span class="skill-tag">Model Deployment</span>
        <span class="skill-tag">Predictive Modeling</span>
        """, unsafe_allow_html=True)

with s_col3:
    with st.container(border=True):
        st.subheader("Tools & Methodologies")
        st.markdown("""
        <span class="skill-tag">Git & GitHub</span>
        <span class="skill-tag">VS Code</span>
        <span class="skill-tag">Jupyter</span>
        <span class="skill-tag">Agile / Scrum</span>
        <span class="skill-tag">SDLC</span>
        <span class="skill-tag">Linux CMD</span>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("---")
st.markdown("<div class='footer-text'>© 2026 MD Tausif Ahmad. All rights reserved. <br> Built with Python & Streamlit</div>", unsafe_allow_html=True)