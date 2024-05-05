import numpy as py
from pandas import options
import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
with open("C:\\Users\\user\\Desktop\\heartprediction\\model.pkl","rb") as f:
    model=pickle.load(f)

def predict(data):
    scale =StandardScaler()
    x_test= scale.fit_transform(data)
    prediction=model.predict(x_test)
    return prediction


def main():
    header=st.container()
    dataset=st.container()
    with header :
        st.title("heart Disease Prediction")
        st.text("predict if the person has heart disease or not:")
        with dataset:
            st.header("Data input")
            st.text("provide following info ")
            age=st.number_input("Age",min_value=0,step =1)
            sex=st.selectbox("Sex",["Female","MAle"])
            cp = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
            trtbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0, step=1)
            chol = st.number_input("Cholesterol (mg/dl)", min_value=0, step=1)
            fps = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["False", "True"])
            restecg = st.selectbox("Resting Electrocardiographic Results", ["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"])
            thalachh = st.number_input("Maximum Heart Rate Achieved", min_value=0, step=1)
            exng = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
            caa = st.number_input("Number of Major Vessels (0-3)", min_value=0, max_value=3, step=1)
            sex=1 if sex=="Male" else 0
            cp_mapping={"Typical Angina": 0,"Atypical Angina":1,"Non-anginal Pain":2,"Asymptomatic":3}
            cp=cp_mapping[cp]
            fps=1 if fps=="True" else 0
            restecg_mapping={"Normal":0, "ST-T wave abnormality":1, "Left ventricular hypertrophy":2}
            restecg=restecg_mapping[restecg]
            exng=1 if exng=='Yes' else 0

            input_data={
            "age": age,
            "sex": sex,
            "cp": cp,
            "trtbps": trtbps,
            "chol": chol,
            "fps": fps,
            "restecg": restecg,
            "thalach": thalachh,
            "exng": exng,
            "caa": caa
            }
            df=pd.DataFrame(data=[input_data])
            if st.button('predict'):
                prediction=predict(df)
                if prediction[0]==1:
                    st.success('You have heart disease')
                else:
                    st.success("You dont have a hd")

if __name__=='__main__':
    main()