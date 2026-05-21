import pandas as pd
import streamlit as st
import joblib

st.title(":green[Model1] :streamlit:")


study=st.number_input("Enter ur study hours:",min_value=0,max_value=20, value=5)
attendance=st.number_input("Enter ur attendance:",min_value=0,max_value=100)
sleep=st.number_input("Enter ur sleep hours:",min_value=0,max_value=10)
internet=st.number_input("Enter ur usage of internets:",min_value=0,max_value=15)
assignment=st.number_input("Enter no. of completed assignment:",min_value=0,max_value=15)
score=st.number_input("enter ur score:",min_value=2,max_value=170)


# checkbox=st.checkbox("I agree these all conditions")
submit=st.button("Predict")
if submit:
        try:
            model = joblib.load("new_model.pkl")
            print("Model Loaded Sucessfully !!")
            response = model.predict([[study,attendance,sleep,internet,assignment,score]])
            st.write(response)
        except Exception as e:
            print("Model error ",e)
