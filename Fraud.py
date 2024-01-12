# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 19:50:18 2023

@author: 91836
"""

#----- import libraries -----
import pandas as pd
import streamlit as st
import pickle
from streamlit_lottie import st_lottie
import requests
from PIL import Image

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#----- LOAD ASSESTS -----
lottie_fraud = load_lottieurl("https://lottie.host/f45a0e5c-f14e-46dc-8c44-c55a6ad120f8/iQRTNq0h1W.json")
img_fraud = Image.open(r"D:\FINAL PROJECT\images\fraud.png", )
img_nofraud = Image.open(r"D:\FINAL PROJECT\images\no fraud.png")

model=pickle.load(open(r"D:\FINAL PROJECT\model.pkl",'rb'))     ## Load pickeled ml model

st.set_page_config(page_title="Fraud detection", layout="wide")

#----- HEADER SECTION ----- 
with st.container():
    st.title("Fraud Detection In Mobile Payment Systems")
    st.subheader("Hi, I am Smit :wave:")
    st.subheader("A data analyst From India.")
    st.write("This is my final project of my classes BIA. My project is on Fraud detection. You can check my github to know more about my projects.")
    st.write("[This is my Github page.](https://github.com/Smitgal?tab=repositories)")
    
#----- ABOUT THE PROJECT -----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About the data")
        st.write("##")
        st.write(
            """
            There is a lack of public available datasets on financial services and specially in the emerging mobile money transactions domain. Financial datasets are important to many researchers and in particular to us performing research in the domain of fraud detection. Part of the problem is the intrinsically private nature of financial transactions, that leads to no publicly available datasets.

We present a synthetic dataset generated using the simulator called PaySim as an approach to such a problem. PaySim uses aggregated data from the private dataset to generate a synthetic dataset that resembles the normal operation of transactions and injects malicious behaviour to later evaluate the performance of fraud detection methods.

Content
PaySim simulates mobile money transactions based on a sample of real transactions extracted from one month of financial logs from a mobile money service implemented in an African country. The original logs were provided by a multinational company, who is the provider of the mobile financial service which is currently running in more than 14 countries all around the world.
"""
)
    with right_column:
        st_lottie(lottie_fraud, height=400, key="Fraud")
        st.write("[For more facts about Fraud Detection in Mobile Payment Systems](https://link.springer.com/article/10.1007/s10796-022-10346-6)")
        
#----- FRAMING UI STRUCTURE -----
def main():
    st.write("---")
    st.title("--- Check For Fraud ---")
    
    step = st.slider("Enter step :", 1, 743, 300)                                                                  # slider for user input(ranges from 1 to 75 & default 30)

    type = st.selectbox("How did you transfer? :", ["TRANSFER", "CASH_OUT"])
    if type == "CASH_OUT":
        type = 0
    else:
        type = 1
        
    st.write("*There is no option for CASH_IN, DEBIT, PAYMENT because they is no fraud to be found in that type of transaction.")
    
    amount = st.number_input("Transaction amount :") # input your transaction amount

    oldbalanceOrg = st.number_input("Your old balance :") # input your old balance
    
    newbalanceOrig = st.number_input("Your new balance :") # input your old balance
    
    oldbalanceDest = st.number_input("recipients old balance :") # input your old balance
    
    newbalanceDest = st.number_input("recipients new balance :") # input your old balance
    
    data = {"step":step, "type":type, "amount":amount, "oldbalanceOrg":oldbalanceOrg, "newbalanceOrig":newbalanceOrig, "oldbalanceDest":oldbalanceDest, "newbalanceDest":newbalanceDest}
    
    df =pd.DataFrame(data, index = [0])
    return df

data = main()

#----- PREDICTION -----
if st.button("predict"):
    result = model.predict(data)
    if result [0] == 0:
        st.write("***Congratulation !!!....*** **There is no Fraud!**")
        st.image(img_nofraud, width = 400)
    else:
        st.write("***You have lost your money.*** **Game Over!**")
        st.image(img_fraud, width = 400)
         





    

        
        
        
        
        
        
        
        
        
        
        
        
        
        