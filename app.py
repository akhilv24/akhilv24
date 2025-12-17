"""
Portfolio Dashboard Application
Author: Akhil
Description: Interactive portfolio dashboard showcasing skills, projects, and experience
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="Akhil's Portfolio Dashboard",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.5rem;
        text-align: center;
        color: #555;
        margin-bottom: 2rem;
    }
    .skill-badge {
        display: inline-block;
        padding: 5px 15px;
        margin: 5px;
        background-color: #e3f2fd;
        border-radius: 20px;
        font-weight: 500;
    }
    .project-card {
        padding: 20px;
        border-radius: 10px;
        background-color: #f5f5f5;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .metric-card {
        text-align: center;
        padding: 20px;
        border-radius: 10px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio(
    "Select a section:",
    ["🏠 Home", "💼 Skills", "📂 Projects", "📊 Analytics", "📧 Contact"]
)

# ====================
# HOME PAGE
# ====================
if page == "🏠 Home":
    st.markdown('<div class="main-header">Hi 👋 I\'m Akhil</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">🚀 AI/ML Explorer / Data Analysis 📊 | 💻 Programmer & Developer | 🌱 Always Learning</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # About Me Section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("📝 About Me")
        st.write("""
        Welcome to my portfolio dashboard! I'm passionate about leveraging technology 
        to solve real-world problems through AI, Machine Learning, and Data Science.
        
        **Current Focus:**
        - 🔭 Working on AI, Machine Learning, and Data Science Projects
        - 🌱 Learning & exploring: Python, ML, Data Analysis, Java, C, C++, HTML, CSS, JS, SQL
        - ⚙️ Love building: Chatbots, Dashboards, ML Models, and Web Apps
        - 📫 Reach me at: **akhilv2402@gmail.com**
        """)
        
        st.write("🌐 **Connect with me:**")
        col_gh, col_li, col_ig = st.columns(3)
        with col_gh:
            st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?style=for-the-badge&logo=github)](https://github.com/akhilv24)")
        with col_li:
            st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/akhil2402/)")
        with col_ig:
            st.markdown("[![Instagram](https://img.shields.io/badge/Instagram-Follow-E4405F?style=for-the-badge&logo=instagram)](https://www.instagram.com/akhilz.24/)")
    
    with col2:
        st.header("📊 Quick Stats")
        st.metric("Projects Completed", "10+", "+2 this month")
        st.metric("Technologies Mastered", "15+", "+3 this quarter")
        st.metric("Lines of Code", "50K+", "↗️")
        st.metric("GitHub Repositories", "25+", "🚀")
    
    st.markdown("---")
    
    # Timeline
    st.header("🎯 Journey Timeline")
    timeline_data = pd.DataFrame({
        'Year': [2023, 2023, 2024, 2024, 2024],
        'Milestone': [
            'Started ML Journey',
            'Built First Chatbot',
            'Data Analysis Projects',
            'Web Development Skills',
            'Advanced AI Projects'
        ],
        'Category': ['Learning', 'Project', 'Project', 'Learning', 'Project']
    })
    
    fig = px.timeline(
        timeline_data,
        x_start='Year',
        x_end='Year',
        y='Milestone',
        color='Category',
        title='My Learning & Development Journey'
    )
    st.plotly_chart(fig, use_container_width=True)

# ====================
# SKILLS PAGE
# ====================
elif page == "💼 Skills":
    st.title("💼 Technical Skills & Expertise")
    
    st.markdown("---")
    
    # Skills by Category
    tab1, tab2, tab3, tab4 = st.tabs(["Programming", "ML & AI", "Web Dev", "Tools"])
    
    with tab1:
        st.header("💻 Programming & Scripting")
        skills_prog = {
            'Python': 95,
            'Java': 85,
            'C': 80,
            'C++': 80,
            'JavaScript': 75,
            'SQL': 85
        }
        
        for skill, level in skills_prog.items():
            col1, col2 = st.columns([1, 4])
            with col1:
                st.write(f"**{skill}**")
            with col2:
                st.progress(level / 100)
                st.caption(f"{level}%")
    
    with tab2:
        st.header("🤖 Machine Learning & AI")
        skills_ml = {
            'PyTorch': 85,
            'TensorFlow': 80,
            'Scikit-learn': 90,
            'OpenCV': 75,
            'NLP': 80,
            'Deep Learning': 85
        }
        
        for skill, level in skills_ml.items():
            col1, col2 = st.columns([1, 4])
            with col1:
                st.write(f"**{skill}**")
            with col2:
                st.progress(level / 100)
                st.caption(f"{level}%")
    
    with tab3:
        st.header("🌐 Web & App Development")
        skills_web = {
            'HTML': 90,
            'CSS': 85,
            'JavaScript': 75,
            'PHP': 70,
            'Flask': 85,
            'Streamlit': 90
        }
        
        for skill, level in skills_web.items():
            col1, col2 = st.columns([1, 4])
            with col1:
                st.write(f"**{skill}**")
            with col2:
                st.progress(level / 100)
                st.caption(f"{level}%")
    
    with tab4:
        st.header("🛠️ Tools & Platforms")
        tools = ['Git', 'GitHub', 'VS Code', 'Linux', 'Figma', 'MySQL', 'SQLite', 'Docker']
        
        cols = st.columns(4)
        for idx, tool in enumerate(tools):
            with cols[idx % 4]:
                st.button(tool, key=f"tool_{idx}", use_container_width=True)
    
    st.markdown("---")
    
    # Skills Distribution Chart
    st.header("📊 Skills Distribution")
    skills_categories = pd.DataFrame({
        'Category': ['Programming', 'ML & AI', 'Web Dev', 'Databases', 'Tools'],
        'Proficiency': [85, 82, 80, 85, 88]
    })
    
    fig = px.bar(
        skills_categories,
        x='Category',
        y='Proficiency',
        color='Proficiency',
        color_continuous_scale='Blues',
        title='Overall Proficiency by Category'
    )
    st.plotly_chart(fig, use_container_width=True)

# ====================
# PROJECTS PAGE
# ====================
elif page == "📂 Projects":
    st.title("📂 Featured Projects")
    
    st.markdown("---")
    
    # Project 1
    with st.container():
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        col1, col2 = st.columns([3, 1])
        with col1:
            st.subheader("🤖 Medical Chatbot")
            st.write("""
            A comprehensive voice-enabled chatbot designed for healthcare assistance.
            
            **Features:**
            - Voice input and output capabilities
            - Chat history management
            - Medicine lookup functionality
            - Health statistics extraction
            - Streamlit-based intuitive UI
            
            **Tech Stack:** Python, Streamlit, NLP, Speech Recognition
            """)
        with col2:
            st.metric("Status", "✅ Live")
            st.metric("Users", "500+")
            if st.button("View Project", key="proj1"):
                st.info("🔗 Project repository link")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Project 2
    with st.container():
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        col1, col2 = st.columns([3, 1])
        with col1:
            st.subheader("🖨️ DataSense AI")
            st.write("""
            An intelligent conversational data analysis tool that makes data insights accessible.
            
            **Features:**
            - Upload any dataset (CSV, Excel)
            - Ask questions in natural language
            - Get instant visualizations
            - AI-powered insights generation
            - Export analysis reports
            
            **Tech Stack:** Python, Pandas, Plotly, LangChain, Streamlit
            """)
        with col2:
            st.metric("Status", "✅ Live")
            st.metric("Datasets", "1000+")
            if st.button("View Project", key="proj2"):
                st.info("🔗 Project repository link")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Project 3
    with st.container():
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        col1, col2 = st.columns([3, 1])
        with col1:
            st.subheader("📊 Employee Attrition Analysis")
            st.write("""
            Machine learning solution for predicting and preventing employee turnover.
            
            **Features:**
            - ML model with 85%+ accuracy
            - Interactive visual dashboards
            - Risk factor analysis
            - Retention strategy recommendations
            - Real-time predictions
            
            **Tech Stack:** Python, Scikit-learn, XGBoost, Tableau, Flask
            """)
        with col2:
            st.metric("Status", "✅ Complete")
            st.metric("Accuracy", "87%")
            if st.button("View Project", key="proj3"):
                st.info("🔗 Project repository link")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Project Statistics
    st.header("📈 Project Statistics")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Projects", "10+", "+2")
    with col2:
        st.metric("Active Projects", "3", "")
    with col3:
        st.metric("Technologies Used", "15+", "+3")
    with col4:
        st.metric("GitHub Stars", "100+", "+15")

# ====================
# ANALYTICS PAGE
# ====================
elif page == "📊 Analytics":
    st.title("📊 Portfolio Analytics")
    
    st.markdown("---")
    
    # Contribution Activity
    st.header("🔥 Contribution Activity")
    
    # Generate sample data
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    contributions = [45, 52, 68, 55, 72, 85, 90, 78, 95, 88, 92, 100]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=months,
        y=contributions,
        mode='lines+markers',
        name='Contributions',
        line=dict(color='#1f77b4', width=3),
        marker=dict(size=10)
    ))
    fig.update_layout(
        title='GitHub Contribution Trends (2024)',
        xaxis_title='Month',
        yaxis_title='Contributions',
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Language Distribution
    st.header("💻 Language Distribution")
    col1, col2 = st.columns(2)
    
    with col1:
        languages = ['Python', 'JavaScript', 'Java', 'C++', 'HTML/CSS', 'SQL']
        usage = [45, 20, 15, 10, 7, 3]
        
        fig = px.pie(
            values=usage,
            names=languages,
            title='Programming Languages Used',
            color_discrete_sequence=px.colors.sequential.Blues_r
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        project_types = ['ML/AI', 'Web Apps', 'Data Analysis', 'Automation', 'Other']
        proj_count = [5, 3, 4, 2, 1]
        
        fig = px.pie(
            values=proj_count,
            names=project_types,
            title='Project Categories',
            color_discrete_sequence=px.colors.sequential.Greens_r
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Technology Radar Chart
    st.header("🎯 Technology Proficiency Radar")
    categories = ['ML/AI', 'Web Dev', 'Data Analysis', 'Backend', 'Frontend', 'DevOps']
    values = [90, 85, 95, 80, 75, 70]
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Current Skills'
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=True,
        title='Technology Proficiency Overview'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Activity Metrics
    st.header("📈 Activity Metrics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Code Commits", "1,250", "+45 this week")
    with col2:
        st.metric("Pull Requests", "180", "+5 this week")
    with col3:
        st.metric("Issues Closed", "120", "+3 this week")
    with col4:
        st.metric("Repos Created", "25", "+1 this month")

# ====================
# CONTACT PAGE
# ====================
elif page == "📧 Contact":
    st.title("📧 Get In Touch")
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("💌 Send Me a Message")
        
        with st.form("contact_form"):
            name = st.text_input("Your Name *")
            email = st.text_input("Your Email *")
            subject = st.selectbox(
                "Subject *",
                ["General Inquiry", "Project Collaboration", "Job Opportunity", "Consultation", "Other"]
            )
            message = st.text_area("Message *", height=150)
            
            submitted = st.form_submit_button("Send Message 📨")
            
            if submitted:
                if name and email and message:
                    st.success("✅ Thank you for your message! I'll get back to you soon.")
                    st.balloons()
                else:
                    st.error("❌ Please fill in all required fields.")
    
    with col2:
        st.header("📍 Contact Information")
        st.write("**Email:**")
        st.code("akhilv2402@gmail.com")
        
        st.write("**Location:**")
        st.write("🌍 Available for Remote Work")
        
        st.write("**Social Media:**")
        st.markdown("- [GitHub](https://github.com/akhilv24)")
        st.markdown("- [LinkedIn](https://www.linkedin.com/in/akhil2402/)")
        st.markdown("- [Instagram](https://www.instagram.com/akhilz.24/)")
        
        st.markdown("---")
        
        st.info("💡 **Quick Response Time:** Usually within 24-48 hours")
    
    st.markdown("---")
    
    # FAQ Section
    st.header("❓ Frequently Asked Questions")
    
    with st.expander("What types of projects do you work on?"):
        st.write("""
        I work on a variety of projects including:
        - Machine Learning and AI applications
        - Data analysis and visualization dashboards
        - Web applications using Python frameworks
        - Chatbots and conversational AI
        - Automation tools and scripts
        """)
    
    with st.expander("Are you available for freelance work?"):
        st.write("Yes! I'm open to freelance opportunities, especially in ML/AI and data science projects. Feel free to reach out!")
    
    with st.expander("What's your tech stack?"):
        st.write("My primary stack includes Python, Machine Learning libraries (PyTorch, TensorFlow, Scikit-learn), web frameworks (Flask, Streamlit), and databases (MySQL, SQLite).")
    
    with st.expander("How can we collaborate?"):
        st.write("I'm always interested in collaborating on interesting projects! Send me a message using the form above or connect with me on LinkedIn or GitHub.")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #888; padding: 20px;'>
        <p><b>Always learning. Always building. Always improving.</b></p>
        <p>Made with ❤️ using Streamlit | © 2024 Akhil | All Rights Reserved</p>
    </div>
    """,
    unsafe_allow_html=True
)
