import streamlit as st

st.title("🧑‍💼 Overview")

st.write("")

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/Avatar.png", width=230)

with col2:
    st.title("Nguyen Duy Phat", anchor=False)
    st.write(
        "Software Developer and AI Enthusiast"
    )

st.write(
    """
    ### Achievements & Awards
    - DAAD Additional Sur-Place Scholarships for Winter Semester 2024/25
    - ISAP Scholarships for Study-Stay in Germanyfor Winter Semester 2025/26
    - Consolation prize at the Final round of AIoT Developer InnoWorks 2025
    """
)

st.write("")

st.write(
    """
    ### Skills
    - Programming Language: Python, C++, C, Javascript
    - Soft skills: Communication, Presentation, Problem-Solving
    - Research experience  
    - Team collaboration  
    """
)
