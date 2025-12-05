import streamlit as st

st.title("🎓 Uni Life")

#Vietnamese-German Uni Life
st.write(
    """
    ### Vietnamese-German University

    In 2023, I walked up to the university door, facing a new challenge in my life.  
    I choose Computer Science as my major even though I got a 50% scholarship for Business Administration.  
    At that time, I was dreaming of becoming a billionaire by being a CEO and creating my own application like Facebook or Instagram.

    I got thousands of questions about my future job. But it is not until CS hit me with Algebra, Computer Architecture,
    and Operating Systems that I realise the journey is not easy for me.  
    It makes me question my decision and somehow also question my existence 🫠

    **But then I realise that it is not about the job. It is about the experience we have along the way that matters.**
    """
)

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/Friend.jpg", width=230)

with col2:
    st.write(
        """
        I meet a lot of great buddies, doing projects together, being gymbros, 
        joining clubs, doing volunteer work, and going to as many events as I can.  
        """
    )

st.write("")

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.write(
        """
        Those moments became some of my best memories. From late night study sessions to fighting in the gym, 
        from building small projects to becoming best friends.
        """
        
    )
with col2:
    st.image("./assets/FC.JPG", width=230)

st.write("")

st.image("assets/AIot.jpg", use_container_width=True)
st.caption("Successfully qualified for the final round of AIoT")

st.markdown("<div style='text-align: center;'>Life was pretty great for the first two years in uni.</div>", unsafe_allow_html=True)

st.write("")

st.write(
    """
    ### Bonn-Rhein-Sieg University of Applied Sciences
    """
)

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/Germany.jpg", width=230)

with col2:
    st.write(
        """
        In 2025, I was fortunate to be granted the ISAP Scholarship, the first step toward my dream of going abroad and exploring a new world. 
        At that moment, everything felt bright; I could finally see the life I had always imagined.

        But reality hit me hard.

        """
    )

st.write("")

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.write(
        """
        Living alone in a completely new country was far from easy. I faced unexpected challenges, both physically and mentally. 
        From 2 times-ER visits to surviving the harsh climate with barely any sunlight, I learned that this path was never meant to be easy.

        Yet these struggles taught me something more valuable than anyone ever could.
        """
    )
with col2:
    st.image("./assets/ER.JPG", width=230)

st.write("")



st.write("")

st.write(
    """
    I began to understand why Germany is known for world-class education. I was inspired not only by Germans but also by students from across Europe, 
    people of different cultures, backgrounds, and ways of thinking. Their discipline, determination, and calmness showed me a new way of approaching life.

    Living here changed my mindset. It reset my perspective. It helped me realize the purpose behind all my efforts.

    Most importantly, this journey helped me find a new dream to chase.
    """
)

st.write("")

st.image("assets/Buddy.JPG", use_container_width=True)

st.write("**Setting foot in a new country wasn’t just a trip. It was an adventure that taught me resilience, independence, and growth in ways I never expected**")


