import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
diabetics_model=pickle.load(open('https://github.com/teja96764247/MULTIPLE-DISEASE-PREDICTIVE-SYSTEM./blob/main/diabetic_model.sav','rb'))


parkinsson_model=pickle.load(open('D:\machine learning projects\MULTIPLE DISEASE PREDICTION\multiple_disease/parkinsson_disease.sav','rb'))



#side bar for navigation......

with st.sidebar:
    selected=option_menu('Multiple Disease Prediction System',
                         ['Diabetics Predcition','Parkinsson Disease Prediction'],
                         icons=['activity','person'],
                         default_index=0)

if(selected=='Diabetics Predcition'):
    st.title('Diabetics Predcition using ML')
    Pregnancies=st.text_input('Number of Pregnancies')
    Glucose=st.text_input('Glucose Level of the body')
    BloodPressure=st.text_input('BloodPressure of person')
    SkinThickness=st.text_input('SkinThickness of the person')
    Insulin=st.text_input('Insulin of the body')
    BMI=st.text_input('Body Mass Index')
    DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction of body')
    Age=st.text_input('Age of the person')
    
    result=""
    if(st.button('check for diabetics')):
        prediction=diabetics_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    
        if(prediction[0]==0):
            result='The person is not having DIABETICS'
        else:
            result='The person is having DIABETICS'
    st.success(result)
    

if(selected=='Parkinsson Disease Prediction'):
    st.title('Parkinsson Prediction using ML')
    MDVPFo=st.text_input('MDVP:Fo(Hz)')
    MDVPFhi=st.text_input('MDVP:Fhi(Hz)')
    MDVPFlo=st.text_input('MDVP:Flo(Hz)')
    MDVPJitter=st.text_input('MDVP:Jitter(%)')
    MDVPJitterAbs=st.text_input('MDVP:Jitter(Abs)')
    MDVPRAP=st.text_input('MDVP:RAP')
    MDVPPPQ=st.text_input('MDVP:PPQ ')
    JitterDDP=st.text_input('Jitter:DDP')
    MDVPShimmer=st.text_input('MDVP:Shimmer')
    MDVPShimmer=st.text_input('MDVP:Shimmer(dB)')
    ShimmerAPQ3=st.text_input('Shimmer:APQ3')
    ShimmerAPQ5=st.text_input('Shimmer:APQ5 ')
    MDVPAPQ=st.text_input('MDVP:APQ')
    ShimmerDDA=st.text_input('Shimmer:DDA')
    NHR=st.text_input('NHR')
    HNR=st.text_input('HNR')
    RPDE=st.text_input('RPDE')
    DFA=st.text_input('DFA')
    spread1=st.text_input('spread1')
    spread2=st.text_input('spread2')
    D2=st.text_input('D2')
    PPE=st.text_input('PPE')
    result=""
    if(st.button('check for parkinsson')):
        prediction2=parkinsson_model.predict([[MDVPFo,MDVPFhi,MDVPFlo,MDVPJitter,MDVPJitterAbs,MDVPRAP,MDVPPPQ,JitterDDP,MDVPShimmer,MDVPShimmer,ShimmerAPQ3,ShimmerAPQ5,MDVPAPQ,ShimmerDDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        if(prediction2[0]==0):
            result='The person is not having the parkinsson disease'
        else:
            result='The person having a parkinsson disease'
    st.success(result)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
