import streamlit as st
import pandas as pd
# import plost
import numpy as np
# import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import pickle
from final import *

st.title('Transaction Simulation')

file= st.file_uploader("Upload Transaction History")
if file is not None:
    df=pd.read_csv(file)
    colss=["Time",'Trans_Id','Name','Acc Num','Merchant Name','Amount','Category']
    st.dataframe(df[colss])
import pandas as pd

transactions_data = pd.DataFrame(columns=['TransactionID', 'Amount','Account Number', 'Category', 'Name'])

# Function to add a new transaction
def add_transaction(transaction_id, amount,acc_no ,category, name):
    global transactions_data
    new_transaction = pd.DataFrame({
        'TransactionID': [transaction_id],
        'Amount': [amount],
        'Account Number':[acc_no],
        'Category': [category],
        'Name': [name]
    })
    transactions_data = pd.concat([transactions_data, new_transaction], ignore_index=True)

# Streamlit App
st.title("Transaction Input Form")

# Input forms
transaction_id = st.text_input("Transaction ID")
amount = st.number_input("Amount")
acc_no= st.number_input('Account Number')
category = st.text_input("Category")
name = st.text_input("Name")

# Button to add transaction
if st.button("Add Transaction"):
    if transaction_id and amount and acc_no and category and name:
        add_transaction(transaction_id, amount, acc_no,category, name)
        st.success("Transaction added successfully!")
    else:
        st.warning("Please fill in all the details.")

# Display current transactions
st.title("Current Transactions")
st.table(transactions_data) 

# if st.button('Submit'):
print('hiiii',transactions_data)
if transactions_data['Amount'] is not None and transactions_data is not None:
    anomaly_score_1=get_amount_anomalous_score(df,transactions_data['Amount'][0])
    anomaly_score_2=get_category_anomalous_score(df,transactions_data['Category'][0],transactions_data['Amount'][0])
    # st.write(anomaly_score_1)
    # st.write(anomaly_score_2)
    final_score=0.6*anomaly_score_2 + 0.4 * anomaly_score_1
    # st.write(final_score)
    if final_score<-0.69:
        st.warning(f"Anomalous transaction found . Anomality Score : {final_score}")
    else:
        st.success(f"It is a Normal Transaction. Anomality Score :{final_score}")
# import smtplib
# from email.mime.text import MIMEText

# email_sender = "dummy05102003@gmail.com"
# email_receiver = "akashranges07@gmail.com"
# subject = "Anomaly transaction"
# body = "We detected a fradulent transaction. Raise a ticket if you havent done it"
# password = "dummyaccount2#"

# if st.button("Send Email"):
#     try:
#         msg = MIMEText(body)
#         msg['From'] = email_sender
#         msg['To'] = email_receiver
#         msg['Subject'] = subject

#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(email_sender, password)
#         server.sendmail(email_sender, email_receiver, msg.as_string())
#         server.quit()

#         st.success('Email sent successfully! 🚀')
#     except Exception as e:
#         st.error(f"Erreur lors de l’envoi de l’e-mail : {e}")





# misc_to_forest={

# 0: r".\models\amount_by_misc\segment_1_iForest.pkl",
# 1: r".\models\amount_by_misc\segment_0_iForest.pkl",
# 2: r".\models\amount_by_misc\segment_2_iForest.pkl"
# }

# misc_to_food_dining={

#     0:r'.\models\amount_by_food_dining\segment_2_iForest.pkl',
#     1:r'.\models\amount_by_food_dining\segment_1_iForest.pkl'
# }

# travel_to_forest={

#     0: r'.\models\amount_by_travel\segment_0_iForest.pkl',
#     1: r'.\models\amount_by_travel\segment_1_iForest.pkl'
# }

# shopping_to_forest={

#     0: r'.\models\amount_by_shopping\segment_1_iForest.pkl',
#     1: r'.\models\amount_by_shopping\segment_0_iForest.pkl'
# }

# grocery_to_forest={

# 0: r".\models\amount_by_grocery\segment_1_iForest.pkl",
# 1: r".\models\amount_by_grocery\segment_2_iForest.pkl",
# 2: r".\models\amount_by_grocery\segment_0_iForest.pkl"
# }