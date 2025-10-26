import streamlit as st

st.title("Registration Form")
st.header("Complite your information")

fname = st.text_input("Enter your First name: ")
mname = st.text_input("Enter your Middel name: ")
lname = st.text_input("Enter your Last name: ")
add = st.text_area("Enter your Permenent address: ")
add2 = st.text_area("Enter your Temparary address: ")
classdata = st.selectbox("Enter your Gender: ",("Male","Female"))

button = st.button("Done")
if button :
    st.markdown(f"""
    First name : {fname}\n
    Middel name : {mname}\n
    Last name : {lname}\n
    Permenent address : {add}\n
    Temaparary address : {add2}\n
    Gender : {classdata}""")