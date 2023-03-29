# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu


diabetes_model = pickle.load(open("Diabetes_model.sav",'rb'))
Heart_dieases_model = pickle.load(open("Heart_model.sav",'rb'))


with st.sidebar:
    selected = option_menu('Dieases predictive system',
                           ['Diabetes Prediction',
                            'Heart Disease prediction'],
                           icons = ['activity','heart'],
                           default_index = 0)


if (selected == 'Diabetes Prediction'):
    st.title('Diabetes prediction using ML')
    
    col1,col2,col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.slider('Number of prehnancies')
    
    with col2:
        Glucose = st.slider('Glucose level')
    
    with col3:
        BloodPressure = st.slider('Blood pressure value')
    
    with col1:
        SkinThickness = st.slider('Skin Thickness value')
    
    with col2:
        Insulin = st.slider('Insulin level')
    
    with col3:
        BMI = st.slider('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.slider('Diabetes Pedigree Function value')
        
    with col2:
        Age = st.slider('Age of the Person')
    
    
    # prediction
    dia_diagnosis = ''
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if (diab_prediction[0] == 0):
            dia_diagnosis  = 'The person is not diabetic'
        else:
            dia_diagnosis = 'The person is diabetic'
            
    st.success(dia_diagnosis)
    


    
    
if (selected == 'Heart Disease prediction'):
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.slider('Age')
        
    with col2:
        sex = st.slider('Sex')
        
    with col3:
        cp = st.slider('Chest Pain types')
        
    with col1:
        trestbps = st.slider('Resting Blood Pressure')
        
    with col2:
        chol = st.slider('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.slider('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.slider('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.slider('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.slider('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.slider('ST depression induced by exercise')
        
    with col2:
        slope = st.slider('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.slider('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.slider('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
    heart_diagnosis = ''
    
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = Heart_dieases_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
    
    
    
    
    

