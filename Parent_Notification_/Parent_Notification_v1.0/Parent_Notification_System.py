import streamlit as st
from navigation import nav_page

if "ufile" not in st.session_state:
    st.session_state.ufile = False

def set_state_visible():
    st.session_state.ufile = False
    

st.title("Parent Notification System")
value  = st.slider("Input the value for filteration of students : ",0,100,75,key="value_for_filteration")
temp = "Students below "+str(value)+" percent will be having their parents sent message to!"
st.caption(temp)
uploaded_file = st.file_uploader("Choose a file",type="xlsx",on_change=set_state_visible,key="upld_file")

if uploaded_file is None:
    st.session_state.ufile = True
else :
    print(uploaded_file)


st.write("#")


col1, col2= st.columns(2)

with col1:
   st.caption("\n\nHere is the file with students filtered to the critria : ")
   st.caption("If download button is not there then you must not have selected a file")

with col2:
   st.download_button("Download",data = file, file_name="filterdatalist.txt",disabled=st.session_state.ufile)

if st.button("Next >"):
    nav_page("Upload_Student_File")
    
    