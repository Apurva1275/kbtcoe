import streamlit as st

st.title("📝 Application Form")

# Custom CSS for button
st.markdown("""
    <style>
        .stButton > button {
            background-color: green;
            color: white;
            border-radius: 8px;
            height: 40px;
            width: 150px;
        }
    </style>
""", unsafe_allow_html=True)

# Create a form
with st.form("application_form"):

    name = st.text_input("Enter your Name")
    age = st.number_input("Enter your Age", min_value=1, max_value=100, step=1)
    gender = st.radio("Select your Gender", ["Male", "Female", "Other"])
    city = st.selectbox("Select your City", ["Delhi", "Mumbai", "Nashik"])

    submit = st.form_submit_button("Submit Application")

    if submit:
        if name.strip() == "":
            st.warning("Please enter your name")
        else:
            st.success("Application Submitted Successfully ✅")
            st.write("### Submitted Details")
            st.write("Name:", name)
            st.write("Age:", age)
            st.write("Gender:", gender)
            st.write("City:", city)