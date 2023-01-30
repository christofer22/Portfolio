from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "main.css"
resume_file = current_dir / "CV.pdf"
profile_pic = current_dir / "foto.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Christofer Rivas"
PAGE_ICON = ":wave:"
NAME = "Christofer Rivas"
DESCRIPTION = """
Data Analyst, Analyst BI, apasionado por los datos para generar insights y valor en las empresas.
"""
EMAIL = "christoferrivas9@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/christofer-rivas-792526232/",
    "GitHub": "https://github.com/christofer22",
    "Instagram": "https://www.instagram.com/christoferriv/",
}
PROJECTS = {
    "🏆 DASHBOARDS DE ANALISIS DE INVENTARIO CONSTRUCTORA GHG S.A": "https://onedrive.live.com/edit.aspx?resid=850389E3A0625A35!1934&cid=850389e3a0625a35&CT=1673984254890&OR=ItemsView",
    "🏆 ANALISIS DEL INDICE SP500 CON PYTHON USANDO WEB SCRAPING Y EDA HASTA UN DASHBOARD FINAL": "https://github.com/christofer22/Proyecto-S-P500/blob/main/Proyecto%20SP5.ipynb",
}




# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:

    a = """<style>[data-testid="stAppViewContainer"]{
background-color: rgba(158, 152, 152, 0.33);
opacity: 1;
background-image: radial-gradient(circle at center center, rgba(0, 0, 0, 0), rgba(158, 152, 152, 0.33)), repeating-radial-gradient(circle at center center, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0), 27px, transparent 54px, transparent 27px);
background-blend-mode: multiply;
            }</style>"""

    st.markdown(a, unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Experiencia práctica y conocimiento en Python y Excel, Power BI, SQL
- ✔️ Buena comprensión de los principios estadísticos y sus respectivas aplicaciones.
- ✔️ Excelente trabajador en equipo y muestra un fuerte sentido de iniciativa en las tareas
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (numpy, Pandas, seaborn, selenium), SQL, VBA
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: MySQL, SQL Server
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Ayudante Universidad de Tarapacá (Ciencia De Datos y Diseño e implementación de estrategias funcionales y creación de valor**")
st.write("08/2022 - 12/2022")
st.write(
    """
- ► Se realizo tutorías en el área de machine learning con modelos algoritmos como KNN,clusters, arboles de decisión, etc.
- ► Organizo grupos de trabajo para un correcto entendimiento de los contenidos y la información
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Formulador de Proyectos**")
st.write("06/2022 - 07/2022")
st.write(
    """
- ► Analizar presupuestos de los proyectos para realizar propuestas económicas en base a las características planteadas de los participantes.
- ► Validar propuestas técnicas para una adecuada postulación y validación de los requisitos por proyecto.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Análisis de inventario**")
st.write("01/2022 - 03/2022")
st.write(
    """
- ► Creación de Dashboard dinámico en Excel.
- ► Reportes de flujo de entradas y salida de inventario.
- ► Mejora de proceso, para la toma de decisiones.
"""
)

# --- Datos académicos ---
st.write('\n')
st.subheader("Datos académicos")
st.write(
    """
- Egresado en ingeniería civil industrial Universidad De Tarapacá | marzo 2017 - Actual
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
