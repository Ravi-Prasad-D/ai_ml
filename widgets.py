import streamlit as st
import pandas as pd
st.title("streamlit text input ")

name=st.text_input("Enter your name:")
age=st.slider("select your age:",0,100,25)
st.write(f"your age is {age},")
options=["python","java","c++","javascript"]
choice=st.selectbox("choose your favoruite langauge:",options)
st.write(f"you selected {choice} as your favoruite language.")
if name:
    st.write(f"Hello, {name}") 

data={
    'Name':['Alice','Bob','Charlie','David'],  
    'Age':[24,30,22,35],
    'City':['New York','Los Angeles','Chicago','Houston']
}   
df=pd.DataFrame(data)
df.to_csv('sample_data.csv')
st.write(df)

uploaded_file=st.file_uploader("choose a csv file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)    