import streamlit as st
e1 = st.empty()
e2 = st.empty()

c1  = e1.container()
c2 = e2.container()
student = ['SAHDEV SINGH', 'ANSHIKA PANDEY', 'PRIYA GARG', 'VAIBHAV KUMAR', 'YASH', 'RIDDHI KAILASH', 'SHUBH AGGARWAL', "NAKUL SATYAWALI", 'DRASHTI GUPTA', "ISHITA SHARMA", "PRATIKSHA DANDRIYAL", "UMA SHANKAR", "PRIYA", "PUNEET KUMAR", "NIHAL JYOTIRAJ", "SURAJ RAWAT", "KESHAV KUMAR MISHRA", "ARYA", "URVASHI", "SATYAM VASHISTHA","SAGAR RAJ", "YAGYESH DUTT", "HARSH CHOUDHARY", "AMAN KUMAR", "NIKHIL KUMAR SINGH", "AAYUSH BHADULA", "SAMARPITH KANDHARI", "PRANAV RAI", "RAHUL", 'PIYUSH GUPTA', 'SHUBHANSHU UPADHYAY', 'NIKUNJ TYAGI', 'SHRIYANSHU SHARMA', 'LAKSHAY VASHISTH', 'SHIVAM DHAMA', 'JATIN SHARMA', 'RAHUL SHUKLA', "TUSHAR MISHRA", 'AADITYA JAIN', 'CHETAN', 'KARTIK KUMAR SINGH', 'ROHIT BHATT', 'PIYUSH GUPTA', 'ARYAN SAXENA', 'ABHISHEK SINGH', 'RANVEER YADAV', 'VAIBHAV SHARMA', 'ANUPAM KUMAR CHAUDHARY', 'AAKASH KUMAR JANGID', 'KUNAL BHARAGAV', 'UMANG PANDEY', 'HARSH', 'RAYMAN KUMAR MODI', 'AYAAN SAIFI']

with c1:
    st.write("This is the first container")
    st.selectbox("Select the name",student)




# streamlit run test.py