from pathlib import Path
import streamlit as st
from PIL import Image


current_dir= Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file= current_dir/"styles"/"main.css"
resume_file = current_dir/"assets"/"RajapandiSresumesp.pdf"
profile_pic= current_dir/"assets"/"profile-pic (12).png"


Page_Title= "Digital CV | Raja Pandi S"
Page_icon=":star:"
Name= "Raja Pandi S"
Description = """
Student | Machine Learning Engineer & Data Scientist """
Email="rajapandivnr1@gmail.com"
social_media={
    "linkedin": "https://www.linkedin.com/in/raja-pandi-s/",
    "github" : "https://github.com/Rawwire"
}
Projects={
    "SNAPGRADE: CGPA & GPA Calculator from Marksheet Photos":"https://github.com/Rawwire/CGPA-calculator",
    "Amazon Price Monitoring and Review Authentication System":"https://amazonreviewsystem.streamlit.app/",
    "Spam Text Classification Using Python":"https://rajapandispantextclassification.streamlit.app/",
    "Banking System Management using Servlets":"https://github.com/Rawwire/BankingSystem",
    "Employee Task Tracker using Servlets":"https://github.com/Rawwire/EmployeeTracker"
}

st.set_page_config(page_title=Page_Title,page_icon=Page_icon)
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)
with open (resume_file,"rb") as pdf_file:
    PDFbyte= pdf_file.read()
    profile_pic= Image.open(profile_pic)

col1,col2= st.columns(2, gap="small")
with col1:
    st.image(profile_pic,width=230)
with col2:
    st.title(Name)
    st.write(Description)
    st.download_button(
        label= "📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write("📧", Email)
    st.write("#")
cols= st.columns(len(social_media))
for index,(platform,link) in enumerate(social_media.items()):
    cols[index].write(f"[{platform}]({link})")

st.write("#")
st.header("Internships")
st.subheader('''
Machine Learning with Python - Acmegrade
''')
st.write('''
- Acquired skills in data preprocessing and implemented various algorithms including Logistic
regression, Decision trees, K-nearest neighbors, and Naive Bayes.
- Applied Random Forest, SVM, K-Means, PCA, LDA, and used Cross-validation and K-fold techniques
for robust model evaluation and validation.
''')
st.subheader('''
Data Science using Python - NSIC. Ltd
''')
st.write('''
- Gained expertise in Python libraries such as NumPy, Pandas, and Matplotlib for data analysis and
visualization.
- Enhanced core Python skills and learned to use Pickle for data serialization and storage.
''')
st.write("---")

st.write("#")
st.header("Hard Skills")
st.subheader("Programming Language and Web Development")
st.write('''
- 🐍 Python
- 🖼️ HTML
- 🖌️ CSS
- 🖥️ Django
''')
st.subheader("Machine Learning and Data Science")
st.write('''
- 🟰 Numpy 
- 🐼 Pandas
- 📊 Matplotlib
- 📈 Seaborn
- 🔬 Sci-kit Learn
- 🖹 Spacy
- 🗟 NLTK
- 🖺 Textblob
- 🌟 Streamlit
''')
st.subheader("Database and Automation")
st.write('''
- 🫙 MySQL
- 🍲 BeautifulSoup
''')
st.header("Soft Skills")
st.write('''
- 🧑‍🎓 Leadership
- 📖 Continuous Learning
- 🚩 Problem Solving
''')
st.write("---")
st.write("#")
st.header("Projects")
for project, link in Projects.items():
    st.write(f"[{project}]({link})")
