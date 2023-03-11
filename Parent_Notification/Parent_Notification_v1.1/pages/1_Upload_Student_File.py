import streamlit as st
from navigation import nav_page
import os
from pathlib import Path
from streamlit_extras.switch_page_button import switch_page
import sys
import json
# from Parent_Notification_System import flag
#The problem is with calling another file that causes every element to be generated alongside the content in the new txt file
st.title("Parent Notification System")
try:
    with open("var.txt", "r") as file:
        flag = file.readlines()[0][:-1]
        
except FileExistsError:
    st.error("There has been an error opening a file.")
    st.stop()
    # Your error handling goes here
# flag = r"C:\Users\TransTele\Desktop\2021-22\StreamLit\Parent_Notification\Sample Data\Student Attendance.xlsx"

if flag == "":
    st.caption("Please Go to the Home page")
    if st.button("Home >"):
        nav_page(r"Parent_Notification_\Parent_Notification_v1.1\Parent_Notification_System")
    st.stop()
else:
    st.subheader("Now , You Can open the file of Filtered Students")
    
if(flag == True):
    uploaded_file = ""
else:
    uploaded_file = flag
if st.button("Open",key="open"):           #This funtion will open excel
        if(sys.platform == "win32"): 
            os.system("start excel "+json.dumps(uploaded_file).replace(r"\\\\",chr(92))) #This is not working "Most frustating of them all"
        elif (sys.platform == "darwin"):
            uploaded_file = uploaded_file.replace(" ", "/ ")
            print(uploaded_file)
            os.system('open %s -a "Microsoft Excel"' %(uploaded_file))
    
st.write("#")

st.subheader("Go to the next Page : ")
if st.button("Next >"):
    switch_page("template selection")

    # nav_page("2_Template_Selection")
