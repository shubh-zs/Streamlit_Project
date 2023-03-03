import streamlit as st

st.title("Parent Notification System")
st.subheader("Now , You have to upload the file of filtered Students")
st.caption("If Nothing is Showing then you must not have selected a file")

filt_file = st.file_uploader("Choose a file",type="xlsx")
