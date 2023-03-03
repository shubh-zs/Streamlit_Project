import streamlit as st
import os

st.title("Parent Notification System")
st.subheader("Select from the Message template! ")
st.write("#")

if os.path.exists("temp.txt"):
    file = open("temp.txt","w+")
else:
    file = open("temp.txt","w+")

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
    else:
        st.warning("There is nothing in the Input Box",icon="🚨")



file.close()


