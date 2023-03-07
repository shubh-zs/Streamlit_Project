import streamlit as st
from navigation import nav_page
import os
import sys
from Parent_Notification_System import flag

st.title("Parent Notification System")
if flag:
    st.subheader("Now , You have to upload the file of filtered Students")
if(not flag or "upld_file" not in st.session_state or st.session_state["upld_file"]==""):
    st.caption("Please Go to the Home page")
    if st.button("Home >"):
        nav_page(r"Parent_Notification_\Parent_Notification_v1.1\Parent_Notification_System")
    st.stop()


uploaded_file = st.session_state["upld_file"]
if st.button("Open",key="open"):           #This funtion will open excel
       if(sys.platform == "win32"): os.system("start excel "+uploaded_file)
       elif (sys.platform == "darwin"): os.system('open %s -a "Microsoft Excel"' %(uploaded_file))
    
st.write("#")

st.subheader("Go to the next Page : ")
if st.button("Next >"):
    nav_page("Template_Selection")
