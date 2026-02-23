import streamlit as st
st.title("basic calculator")

num1=st.number_input("enter your first number", step=1, format="%d")
num2=st.number_input("enter your second number", step=1, format="%d")

operation =st.selectbox("choose op",["add","sub","mul","div"])

if st.button("calculate"):
    if operation == "add":
     st.write(int(num1 + num2))
    elif operation == "sub":
            st.write(int(num1 - num2))
    elif operation == "mul":
        st.write(int(num1 * num2))
    elif operation == "div":
        if num2!=0:
          st.write(int(num1 / num2))
        else:
            st.write("can not divide by 0")
