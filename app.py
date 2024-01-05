import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
def get_transactions_per_day(df):
    df['Time'] = pd.to_datetime(df['Time'])
    df['Time'] = df['Time'].transform(lambda x : x.date())
    transactions = df.groupby(["Time"])["Amount"].count()
    return transactions

def get_average_per_day(df):
    df['Time'] = pd.to_datetime(df['Time'])
    df['Time'] = df['Time'].transform(lambda x : x.date())
    average = df.groupby(["Time"])["Amount"].mean()
    return average

def get_transactions_per_month(df):
    df['Time'] = pd.to_datetime(df['Time'])
    df['Month'] = df['Time'].transform(lambda x : str(x.month) + " / " + str(x.year))
    transactions = df.groupby(['Month'])["Amount"].count()
    return transactions

def get_average_per_month(df):
    df['Time'] = pd.to_datetime(df['Time'])
    df['Month'] = df['Time'].transform(lambda x : str(x.month) + " / " + str(x.year))
    average = df.groupby(['Month'])["Amount"].mean()
    return pd.DataFrame(average)

def get_transactions_per_year(df):
    df['Time'] = pd.to_datetime(df['Time'])
    df['year'] = df['Time'].dt.year
    transactions = df.groupby(['year'])["Amount"].count()
    return transactions

def get_average_per_year(df):
    df['Time'] = pd.to_datetime(df['Time'])
    df['year'] = df['Time'].dt.year
    average = df.groupby(['year'])["Amount"].mean()
    return average
    
st.markdown("<h1 style='text-align: center;'>Transaction Dashboard</h1>", unsafe_allow_html=True)


file= st.file_uploader("Upload Transaction History")
if file is not None:
    df=pd.read_csv(file)
    cols=df.columns

    st.markdown('## Transaction Summary')
    colss=["Time",'Trans_Id','Name','Acc Num','Merchant Name','Amount','Category']
    st.dataframe(df[colss])

    import pickle
    with open(r'C:\Users\akash\OneDrive\Desktop\IITM_Hackthon\IITM_Cyberpunks_ML\models\amount_clusters.pkl','rb') as amount_model:
        model_cluster= pickle.load(amount_model)
    res=model_cluster.predict([[np.log(df['Amount']).mean()]])
    spending_category= 'Low Spender' if res ==0 else 'High Spender'

    co1,co2,co3=st.columns(3)

    with co2:
        st.metric('Customer Category',spending_category)

  


    value = st.selectbox("Select type of Chart",('per_day','per_month','per_year'))

    print('sammm',get_average_per_month(df))
 
    print("hi",value)
    if value=="per_day":
        func=get_average_per_day(df.copy())
    elif value=='per_month':
        print('hiiii')
        func=get_average_per_month(df.copy())
    elif value=="per_year":
        func=get_average_per_year(df.copy())



    if value=="per_day":
        func_trans=get_transactions_per_day(df)
    elif value=='per_month':
        func_trans=get_transactions_per_month(df)
    elif value=="per_year":
        func_trans=get_transactions_per_year(df)

    col1,col2=st.columns(2)

    with col1:
        st.markdown('### Average Amount')
        chart=st.bar_chart(func)
    with col2:
        st.markdown('### No Of Transactions')
        chart_trans=st.bar_chart(func_trans)


    cols=['misc', 'grocery', 'entertainment', 'gas_transport', 'shopping',
                'food_dining', 'personal_care', 'health_fitness', 'travel',
                'kids_pets','home']


    import plotly.express as px
    grouped_df = df.groupby('Category')['Amount'].sum().reset_index()

    fig = px.pie(grouped_df, values='Amount', names='Category', title='Amount Spent by Category',
                height=800, width=800)  
    st.markdown(
        """
        <style>
            .stPlot {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.plotly_chart(fig)

