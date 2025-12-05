import streamlit as st

with st.sidebar:
    st.title("Welcome to my portfolio")


about_page = st.Page(
    page="views/DefaultPage.py",   # NEW DEFAULT PAGE
    title="About This Web",
    icon=":material/info:",
    default=True
)

overview_page = st.Page(
    page="views/Overview.py",
    title="Overview",
    icon="🧑‍💻"
)

unilife_page = st.Page(
    page="views/UniLife.py",
    title="Uni Life",
    icon="🎓"
)

hobbies_page = st.Page(
    page="views/Hobbies.py",
    title="Hobbies",
    icon="🎮"
)

# ---- NAVIGATION ----


st.navigation({
    "Info": [about_page, overview_page, unilife_page, hobbies_page]
}).run()
