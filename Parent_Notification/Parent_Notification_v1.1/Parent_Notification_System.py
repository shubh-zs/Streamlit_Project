import streamlit as st
from navigation import nav_page
from edit_prepare import status
import os
import sys
from streamlit_extras.switch_page_button import switch_page

if "a" not in st.session_state:
    st.session_state["a"] = 0

st.set_page_config(page_title="Notification System",page_icon="🧊",initial_sidebar_state="collapsed")
st.session_state 

def get_platform():                         #These three lines are reponsible to display appropate links
    platforms = {
        'linux' : 'https://askubuntu.com/questions/225666/copy-file-and-folder-path-from-nautilus',
        'linux1' : 'https://askubuntu.com/questions/225666/copy-file-and-folder-path-from-nautilus',
        'linux2' : 'https://askubuntu.com/questions/225666/copy-file-and-folder-path-from-nautilus',
        'darwin' : 'https://support.apple.com/en-in/guide/mac-help/mchlp1774/mac',
        'win32' : 'https://techcommunity.microsoft.com/t5/windows-11/how-do-i-copy-file-paths-on-windows-11/m-p/3061750'
    }
    return platforms[sys.platform]
def check_path(up_file):
    if(os.path.exists(up_file)==False):   
        st.text("Input the Correct and Full Path")
        st.stop()
    if(up_file[-5:]!=".xlsx"): 
        st.text("Input the correct file with .xlsx extension")
        st.stop()

f_name = "file_path.txt"
if os.path.exists(f_name):
    file = open(f_name,"r+")
else:
    file = open(f_name,"a+")


if("open_page" not in st.session_state):    #It is a flag that represents the flag that tells the next page to enable its function
    st.session_state["open_page"]=False


st.title("Parent Notification System")

st.write("#")                               #This hash is for the newline in the frontend
value  = st.slider("Input the value for filteration of students : ",0,100,75,key="value_for_filteration")
st.caption("Students below "+str(value)+" percent will be having their parents sent message to!")
                                            

st.write("#")
st.subheader("Upload Students Attendance File")
uploaded_file = st.text_input("Choose a Student Data File",key="upld_file",placeholder="Insert Path or Click The Question Button"
                              ,help="If you are not able to, then click the following link "+get_platform())
if uploaded_file is not None:               #These if else statement check if the file is of xlsx extension
    check_path(uploaded_file)


st.write("#")
st.subheader("Select Parent Data File")

data = ["Select... "]
data_path = []
a=0
for i in file.readlines():
    # if(os.path.exists(i)==True):          #Even if the path exists this function returns false 
        data_path.append(i)
    # print(a,"path :",i,"flag : ",os.path.exists(i),"array : ",data_path)   This line is for the debugging
    # a=a+1
data.extend(data_path)


opt = st.selectbox("Select one of the following files : ",options=data,index=0)

st.subheader("Type Path to the Parent Data File ! ")
text_input = st.text_input("Input Parent Data File : ",placeholder="Insert Path or Click The Question Button"
                           ,help="If you are not able to, then click the following link "+get_platform())
st.info('Make Sure that the File is Closed. ', icon="ℹ️")

button = st.button("Insert")
text_flag = False
if button:
    if text_input:                          #Assuming the file is correct
        check_path(text_input)
        text_flag = True
        # if text_input not in file.readlines()[:][:-3]:      #This is not working
        file.write(text_input+'\n')   
        data.append(text_input)
    else:
        st.warning("There is nothing in the Input Box",icon="🚨")

status_flag = False
if(opt is not None and opt!=data[0] and not status_flag and st.session_state["a"]==0):
    st.session_state["open_page"]=status(uploaded_file,opt[:-1],value)
    st.session_state['a'] = st.session_state["a"]+1

if st.session_state["open_page"]:
    with open("var.txt","w") as file:
        file.write(uploaded_file+"\n")
        file.write(str(value)+"\n")


if(st.session_state["open_page"]):
    st.subheader("Go to the next Page : ")
    if st.button("Next >",key="idk"):
        status_flag = True
        # st.session_state["a"] = 0
        switch_page("upload student file")
        

        # nav_page("Upload_Student_File")

if(text_flag and not st.session_state["open_page"]):
    st.error("The Editing Was NOT Done Properly. Check if the File is close otherwise editing will not be possible")

file.close()