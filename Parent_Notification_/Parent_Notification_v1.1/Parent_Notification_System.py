import streamlit as st
import os
from navigation import nav_page
from edit_prepare import status
import sys
st.set_page_config(page_title="Notification System",page_icon="🧊",initial_sidebar_state="collapsed")


def get_platform():
    platforms = {
        'linux1' : 'https://askubuntu.com/questions/225666/copy-file-and-folder-path-from-nautilus',
        'linux2' : 'https://askubuntu.com/questions/225666/copy-file-and-folder-path-from-nautilus',
        'darwin' : 'https://support.apple.com/en-in/guide/mac-help/mchlp1774/mac',
        'win32' : 'https://techcommunity.microsoft.com/t5/windows-11/how-do-i-copy-file-paths-on-windows-11/m-p/3061750'
    }
    return platforms[sys.platform]

if("f_open_file" not in st.session_state):
    st.session_state["f_open_file"]=True


st.title("Parent Notification System")
value  = st.slider("Input the value for filteration of students : ",0,100,75,key="value_for_filteration")
temp = "Students below "+str(value)+" percent will be having their parents sent message to!"
st.caption(temp)

temp = "\n"+get_platform()
uploaded_file = st.text_input("Choose a file",key="upld_file",help="If you are not able to, then click the following link "+temp)
st.info('Input the full path of the file. ', icon="ℹ️")

# Here I'm Assuming that the teacher ONLY teaches a single class although it would be easy to implement a file system
# But for the sake of completing this project im going to overlook.

if(1==1): print("yes")

if uploaded_file is not None:
    if(os.path.exists(uploaded_file)==False):
        st.text("Input the correct path")
        st.stop()
    if(uploaded_file[-5:]!=".xlsx"): 
        st.text("Input the correct file with .xlsx extension")
        st.stop()

st.write("#")




st.session_state["f_open_file"]=status(uploaded_file)





col1, col2= st.columns(2)

with col1:
   st.caption("\n\nHere is the file with students filtered to the critria : ")

with col2:
   if st.button("Open",key="open",disabled=st.session_state["f_open_file"]):
       if(sys.platform == "win32"): os.system("start excel "+uploaded_file)
       elif (sys.platform == "darwin"): os.system('open %s -a "Microsoft Excel"' %(uploaded_file))

if st.button("Next >"):
    nav_page("Upload_Student_File")

    
    