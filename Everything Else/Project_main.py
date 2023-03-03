import csv
import streamlit as st

if "a" not in st.session_state:
    st.session_state.a = False
if "b" not in st.session_state:
    st.session_state.b = False
fields = ['id', 'ide', 'qn01', 'qn02', 'qn03', 'qn04', 'qn05', 'qn06', 'qn07', 'qn08', 'qn09', 'qn10', 'qn11', 'qn12', 'qn13', 'qn14', 'qn15']
if "x" not in st.session_state:   
    st.session_state.b = False
    with open("data.csv",'w') as file:
            write = csv.writer(file)
            write.writerow(fields)


student = ["Select ...",'SAHDEV SINGH', 'ANSHIKA PANDEY', 'PRIYA GARG', 'VAIBHAV KUMAR', 'YASH', 'RIDDHI KAILASH', 'SHUBH AGGARWAL', "NAKUL SATYAWALI", 'DRASHTI GUPTA', "ISHITA SHARMA", "PRATIKSHA DANDRIYAL", "UMA SHANKAR", "PRIYA", "PUNEET KUMAR", "NIHAL JYOTIRAJ", "SURAJ RAWAT", "KESHAV KUMAR MISHRA", "ARYA", "URVASHI", "SATYAM VASHISTHA","SAGAR RAJ", "YAGYESH DUTT", "HARSH CHOUDHARY", "AMAN KUMAR", "NIKHIL KUMAR SINGH", "AAYUSH BHADULA", "SAMARPITH KANDHARI", "PRANAV RAI", "RAHUL", 'PIYUSH GUPTA', 'SHUBHANSHU UPADHYAY', 'NIKUNJ TYAGI', 'SHRIYANSHU SHARMA', 'LAKSHAY VASHISTH', 'SHIVAM DHAMA', 'JATIN SHARMA', 'RAHUL SHUKLA', "TUSHAR MISHRA", 'AADITYA JAIN', 'CHETAN', 'KARTIK KUMAR SINGH', 'ROHIT BHATT', 'PIYUSH GUPTA', 'ARYAN SAXENA', 'ABHISHEK SINGH', 'RANVEER YADAV', 'VAIBHAV SHARMA', 'ANUPAM KUMAR CHAUDHARY', 'AAKASH KUMAR JANGID', 'KUNAL BHARAGAV', 'UMANG PANDEY', 'HARSH', 'RAYMAN KUMAR MODI', 'AYAAN SAIFI']

"st.session_state object:",st.session_state


ept1 = st.empty()
ept2 = st.empty()

con1 = ept1.container()
con2 = ept2.container()

def state():
    st.session_state.a = True

def state1():
    st.session_state.b = True

with con1:
    st.title("Hola, Namaster and Welcome to The Ultimate KBC")
    st.header("Kaisa Bhaya College")
    in1 = st.selectbox("Name : ",student,key = "id")
    in2 = st.text_input("Email  : ",key = "ide")
    b = st.button("Submit",key = 1, on_click = state)


if(st.session_state.a):
    ept1.empty()
    with con2:
        st.title("Kaisa Bhaya College")
        st.header("So the simple task will be that everyone will get some questions that you guys have to answer using the data sheet given to everyone!!")

        # qn01 = st.text("Who has the best personality among everyone in the class : ")
        # st.selectbox("Select the name",student, key = "qn01")

        qn01 = st.text("Who's most likely to die a virgin among everyone in the class : ")
        st.selectbox("Select the name",student, key = "qn01")

        qn02 = st.text("Who has a unique personality among everyone in the class : ")
        st.selectbox("Select the name",student, key = "qn02")

        qn03 = st.text("Who has worst sense of humour among everyone in the class : ")
        st.selectbox("Select the name",student, key = "qn03")

        qn04 = st.text("Who do you think has brightest future ahead of him among everyone in the class : ")
        st.selectbox("Select the name",student, key = "qn04")

        qn05 = st.text("Who's the Dramatic personality in out class among everyone in the class : ")
        st.selectbox("Select the name",student, key = "qn05")

        qn06 = st.text("Who's the class clown among everyone in the class : ")
        st.selectbox("Select the name",student, key = "qn06")

        qn07 = st.text("Who's the most handsome guy among everyone in the class : ")
        st.selectbox("Select the name",student, key = "qn07")

        qn08 = st.text("Who's the dumbo in our class among everyone in the class : ")
        st.selectbox("Select the name",student, key = "qn08")

        qn09 = st.text("Who's the prettiest girl among everyone in the class : ")
        st.selectbox("Select the name",student, key = "qn09")

        qn10 = st.text("Who's the simp(desperate for attention from opp gender) among everyone in the class : ")
        st.selectbox("Select the name",student, key = "qn10")


        qn11 = st.text("Who has the best dressing sense among everyone in the class : ")
        st.selectbox("Select the name",student, key = "qn11")


        qn12 = st.text("Who's the person who thinks too much of themselves among everyone in the class : ")
        st.selectbox("Select the name",student, key = "qn12")


        qn13 = st.text("Who is the underrated person among everyone in the class : ")
        st.selectbox("Select the name",student, key = "qn13")


        qn14 = st.text("Who's do you think is the teachers pet among everyone in the class : ")
        st.selectbox("Select the name",student, key = "qn14")


        qn15 = st.text("Who has most annoying voice among everyone in the class : ")
        st.selectbox("Select the name",student, key = "qn15")
        
        s  = st.button("Submit",key = 2,on_click = state1)


if(st.session_state.b):
    dic = st.session_state
    sa = dict(sorted(dic.items(), key = lambda kv: kv[0]))
    for i in ['2','b','a','1','x']:
        del sa[i]
    st.write(sa)

    with open("data.csv",'a') as file:
        write = csv.writer(file)
        write.writerow(list(sa.values()))
        


# streamlit run Project_main.py