import streamlit as st

if 'num1' not in st.session_state:
    st.session_state.num1 = ''
if 'num2' not in st.session_state:
    st.session_state.num2 = ''

def value_reset():
    st.session_state.num1 = ''
    st.session_state.num2 = ''

st.title(" Calculator ...")

num1 = st.text_input("Enter the first number", key='num1')

num2 = st.text_input("Enter the second number", key='num2')

col1, col2, col3 = st.columns(3,vertical_alignment="bottom")


with col1:
    add_clicked = st.button("Add",icon="➕")

with col2:
    substract_clicked = st.button("Subtract",icon="➖")

with col3:
    st.button("Reset",on_click=value_reset)

if add_clicked:
    st.write("Result:", float(num1) + float(num2))
if substract_clicked:
    st.write("Result:", float(num1) - float(num2))

