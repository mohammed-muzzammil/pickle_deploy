import pickle
import streamlit as st
import os

# Header
st.title("Salary prediction model with pickle")

# "/app/{repository name}/ {file.extension}"
Pkl_Filename = "/app/pickle_deploy/Model.pkl"

# Import the machine learning model using pickle
with open(Pkl_Filename, 'rb') as f:
    regressor = pickle.load(f)


# Function to predict salary based on experience

yoe = st.slider('Years of Experience', 0, 10)
if st.button('Predict'):
    salary = regressor.predict([[yoe]])

    st.success('Salary is $ {}'.format(salary))


