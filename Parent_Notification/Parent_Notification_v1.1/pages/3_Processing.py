import streamlit as st
import pywhatkit.whats as pwk
from openpyxl import Workbook, load_workbook 
# from 2_Template_Selection import opt
import time

try:
    with open("var.txt","r") as file:
        data = file.readlines()
        upfile = data[0][:-1]
        temp = data[-1]
except FileExistsError:
    st.error("There has been an error opening a file.")
    st.stop()

st.title("Parent Notification System")

if upfile :
    st.subheader("Message selected is going in the process of being sent to the Parents!")
    # st.session_state 
    st.write("#")
    st.write("#")
    st.text("It is recommended if you dont use it for a couple of minutes.")
    st.text("It is dependent on the number of contacts the message has to be sent to.")

    #To solve the import problem of template python file I have to make a new txt file
    wb_attendance = load_workbook(upfile)
    sheet = wb_attendance["Edit Data"]

    roll_Number = {}
    row = 1
    for no in sheet["C"]:
        if(row != 1):
            if(no.value is not None):
                roll_Number[sheet["A"+str(row)].value] = no.value
        row +=1

    parent_info = {}
    row = 1
    for name in sheet["B"]:
        if(row != 1):
            if(name.value is not None):
                parent_info[sheet["A"+str(row)].value] = name.value
        row +=1
    
    st.subheader("The total number of Contacts Messages are being sent to : "+str(len(parent_info)))
    p_inc = 0
    p_text = "Number of people message has been sent to : "
    pgs = st.progress(0,p_text+str(0))
    templ = temp
    for num in roll_Number.values():
        if "{name}" in temp:
            temp = temp.replace("{name}",list(parent_info.values())[p_inc])           #p_inc is used here as it works like indexing would
        if "{rno}" in temp: 
            temp = temp.replace("{rno}",str(list(parent_info.keys())[p_inc]))         #p_inc is used here as it works like indexing would
        time.sleep(0.5)
        pwk.sendwhatmsg_instantly("+91"+str(num),temp,tab_close=True,close_time=1)
        temp = templ
        p_inc +=1
        pgs.progress(int((p_inc/len(parent_info))*100),p_text+str(p_inc))
    if(p_inc == len(parent_info)):
        st.write("#")
        st.subheader("The processing has been Finished")
        st.subheader("You can Close this Window")        
    


    
    
else:
    st.error("Error! Please Start from the beggining")
