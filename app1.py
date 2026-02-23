import streamlit as st 
st.title("simple input app")
name =st.text_input("enter your name")
if st.button("submit"):
        st.write("hello",name)
   

