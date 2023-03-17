import streamlit as st
import os
from streamlit_extras.switch_page_button import switch_page

st.session_state

st.title("Parent Notification System")
st.subheader("Select from the Message template! ")
st.text("Template provides the option to input the Following variables :")
col1 , col2  = st.columns(2)

with col1:
    st.subheader("Variable")
    st.text("1. Parent Name")
    st.text("2. Student Roll Number")

with col2:
    st.subheader("Input")
    st.text("{name}")
    st.text("{rno}")

st.subheader("You have to Select the input in the Selection Box")
f_name = "temp.txt"
if os.path.exists(f_name):
    file = open(f_name,"r+")
else:
    file = open(f_name,"a+")

st.write("#")
data = ["Select... "]
data.extend(file.readlines())
opt = st.selectbox("Select one of the following template : ",options=data,index=0)

st.write("#")
st.write("#")

st.subheader("Write a new Message template! ")
text_input = st.text_input("Enter the message : ",placeholder="This is a placeholder")
button = st.button("Insert")
if button:
    if text_input: 
        file.write(text_input+"\n")
        data.append(text_input)
    else:
        st.warning("There is nothing in the Input Box",icon="🚨")
file.close()

if(opt is not None and opt != data[0]):
    if st.button("Next >",key="idk1"):
        with open("var.txt","a") as file:
            file.write(opt)
        switch_page("processing")
else:
    st.text("To go to Page Select the Appropiate Option from the Selection Box!")


