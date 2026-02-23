import streamlit as st

st.title("Welcome to Basit Streamlit App")

# Custom CSS (place it at the top)
st.markdown("""
    <style>
        .stButton > button {
            background-color: green;
            color: yellow;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

age = st.slider("Select your age", 1, 100)
city = st.selectbox("Select your city", ["Delhi", "Mumbai", "Nashik"])

if st.button("Show details"):
    st.write("Age:", age)
    st.write("City:", city)