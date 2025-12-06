import streamlit as st

st.title("🎮 Hobbies")

st.write("")

st.write(
    """
    As a young and passionate man, I enjoy doing many things in my free time. 
    """
)

st.write("")

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/Anime.jpg", width=230)

with col2:
    st.write(
        """
        ### Video Games and Anime

        Video games have been a big part of my life since childhood, and teaming up late at night with my best friend is still one of the best feelings.  
        """
    )

st.write("")

st.write(
    """
    I also love watching anime and TV shows which people sometimes call me nerdy for it, but I always take it as a compliment 😎
    """
)

st.write("")

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.write(
        """
        ### Collecting Figure

        Another hobby I’ve had since I was a kid is collecting and playing with figures. 
        It’s one of my **all time favorites** and something that still brings me a lot of joy today.
        """
        
    )
with col2:
    st.image("./assets/Bandai.JPG", width=250)

st.write("")

st.write(
    """
    ### Sports

    I’m also lucky to have a great group of friends who share similar interests. We play **football, badminton, go swimming, hiking**, 
    and try out many other sports together. Besides that, I like staying updated with the latest news and keeping track of new technologies that are coming out.
    """
)

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/Hiking.jpg", width=350)
with col2:
    st.image("./assets/Bestie.JPG", width=350   )
