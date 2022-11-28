import streamlit as st

st.header("Week 8 Assignment- YASHWANT RAJ - 21f1001547")

number1 = st.number_input('Insert First Number',value=0.0) 

number2 = st.number_input('Insert Second Number',value=0.0)

if number1 is not None and number2 is not None:
    st.write("Subtraction of the numbers is: {}".format((number1-number2)))

