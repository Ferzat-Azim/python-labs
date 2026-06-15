

import streamlit as st

if "num1" not in st.session_state:
    st.session_state.num1 = 0.0

if "num2" not in st.session_state:
    st.session_state.num2 = 0.0



num1 = st.number_input("Enter first number", key="num1")
num2 = st.number_input("Enter second number", key="num2")
op = st.selectbox("select operator", ["+", "-", "*", "/","^","√"])


col1, col2 = st.columns(2)

with col1:
    calculate_btn = st.button("Calculate")
with col2:
    ac_btn = st.button("AC")


if calculate_btn:
    if op == "+":
        st.write(num1 + num2)
    elif op == "-":
        st.write(num1 - num2)
    elif op == "*":
        st.write(num1 * num2)
    elif op == "/":
        if num2 == 0:
            st.error("Error: Division by zero")
        else:
            st.write(num1 / num2)
    elif op == "^":
        st.write(num1**num2)
    elif op == "√":
        result = num1**0.5
        st.write(round(result, 2))
    else:
        st.error("Invalid operator")

if ac_btn:
    st.session_state.clear()
    st.rerun()