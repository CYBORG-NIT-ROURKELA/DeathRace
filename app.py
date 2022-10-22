import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(layout="wide")
st.header("Death Race")
st.subheader("Event By Cyborg ❤️")

bg_pattern = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #e5e5f7;
    opacity: 0.8;
    background-image: radial-gradient(#444cf7 0.5px, #e5e5f7 0.5px);
    background-size: 10px 10px;
}
[data-testid="stToolbar"] {
    display: none;
}
[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0);
}

span {
    color: black;
}
</style>
"""

details = """
<style>
    color: black;
</style>

"""

st.markdown(bg_pattern, unsafe_allow_html=True)
details = """
    <style>
        .text-center {
            text-align: center;
        }
        #event-details {
            text-align: center;
        }
    </style>
    <h2>Event Details</h2>
"""
col1, col2 = st.columns([2,3])
with col1:
    st.image('DeathRace.jpg')
with col2: 
    st.markdown("<div class='event-details'>"+details+"</div>", unsafe_allow_html=True)


st.markdown("<h2 class='text-center'>PROBLEM STATEMENT LINK <a href='https://drive.google.com/file/d/17hyl0eAVeuoSGZPHqp3aECtBXY5fl1Zv/view?usp=sharing'>HERE</a></h2>", unsafe_allow_html=True)

# import base64
# def add_bg_from_local(image_file):
#     with open(image_file, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read())
#     st.markdown(
#     f"""
#     <style>
#     .stApp {{
#         background-image: url(data:image/{"jpeg"};base64,{encoded_string.decode()});
#         background-size: cover
        
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
#     )
# add_bg_from_local('62d98ff9ce4cc1042322ac42.jpeg')