import streamlit as st

if "flag" not in st.session_state:
    st.session_state.flag = False
"st.session_state object:",st.session_state
ep = st.empty()

col1,sp,col2 = ep.columns([2,1,2])



def state():
    st.session_state.flag = True
def lbs_kg():
    st.session_state.kg = st.session_state.lb/10

def kg_lbs():
    st.session_state.lb = st.session_state.kg*10


with col1:
    po = st.number_input("Pounds",key="lb",on_change = lbs_kg)

with sp:
    but = st.button("Change",key="State",on_click = state)

with col2:
    kg = st.number_input("Kilo",key = "kg",on_change = kg_lbs)

if(st.session_state.flag):
    ep.empty()
    with st.container():
        st.header("Kaisa Bhaya College")
        in1 = st.text_input("Name : ")
        in2 = st.text_input("Roll Number : ",help = "(Ex. a08, a50)..", max_chars = 3)

# streamlit run pounds_kg.py