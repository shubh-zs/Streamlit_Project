import streamlit as st
import os

st.session_state

st.title("Parent Notification System")
st.subheader("Select from the Message template! ")
st.write("#")
f_name = "temp.txt"
if os.path.exists(f_name):
    file = open(f_name,"r+")
else:
    file = open(f_name,"a+")

data = ["Select... "]
data.extend(file.readlines())
st.selectbox("Select one of the following template : ",options=data,index=0)

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


