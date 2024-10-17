import streamlit as st
import pandas as pd
import numpy as np
st.title("My first app")
number = st.slider("Select a number",0,1000,100) #Adding Slider to take input from user
st.write(number)
# Adding Button
if st.button("Say Hello"):
    st.write("bye")
else:
    st.write("Hello")

#Adding Checkbox
st.radio("Please select one",("1st Year","2nd Year","3rd Year","4th Year"))

# Adding Dropdown List
st.selectbox("Please select",(1,2,3,4))

# Adding Selection Slider
st.select_slider("Please select",(1,2,3,4,7))

#SideBar
st.sidebar.selectbox("Please select",(1,2,3,4,7))

st.text_input("Enter your name")


st.sidebar.text_input("Enter your Surname")

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

