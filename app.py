from pathlib import Path
import streamlit as st
from PIL import Image

#---- PATH SETTINGS-------#
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
print("The current working directory is: "+str(current_dir))

css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "madhu.png"

#---------GENERAL SETTINGS------------#
PAGE_TITLE = "Digital CV | Madhusudhan B"
PAGE_ICON = ":wave:"
NAME = "Madhusudhan B"
DESCRIPTION = """
Motivated Data Scientist with 6+ years of experience in executing data-driven solutions in diverse fields
such as Energy, Manufacturing & CPG. Academically sound with Dual Masters in Manufacturing & Data
Science, proficient in building Machine Learning & Deep Learning models for classification, regression
& forecasting tasks
"""
EMAIL = "madhuhotmail2005@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/madhusudhan-datascience",
    "GitHub": "https://github.com/madhuyadu"
}
PROJECTS = {
    "🏆 History-based & Potential-based product recommendations to stores on B2B App",
    "🏆 Customized item recommendations to stores via Offline route(traditional channel)",
    "🏆 Generation of Substitute & Complimentary item recommendations to stores on B2B App",
    "🏆 Store sale value forecasting using Forecasting approach",
    "🏆 Building Analytics platform for Energy Efficient heating solution"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title("Hello there !")