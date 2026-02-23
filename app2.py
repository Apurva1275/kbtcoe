import streamlit as st
st.title("welcome to basit streamlit app")
age =st.slider("select your age",1,100)
city =st.selectbox("select your city",["delhi","mumbai","nashik"])
if st.button("show details"):
    st.write("age",age)
    st.write("city",city)