import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

# loading the saved models
transaction_model = pickle.load(open('C:/Users/admin/Downloads/block chain fault transaction/transaction.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('transaction fault prediction using ML',
                          ['Home'],
                          default_index=0)

# personality prediction Page
if selected == 'Home':
    # page title
    st.title('Transaction Prediction using ML')
    st.image("download1.jpg")

    # getting the input data from the user
    col1, col2, col3, col4, col5 = st.columns(5)

    # ... (previous code)


with col1:
    Avgminbetweensenttnx = st.text_input('Avg min between sent tnx')
with col2:
    NumberofCreatedContracts = st.text_input('Number of Created Contracts')
with col3:
    ERC20totalEtherreceived = st.text_input('ERC20 total Ether received')
with col4:
    Senttnx = st.text_input('Sent tnx')
with col5:
    ReceivedTnx = st.text_input('Received Tnx')

with col1:
     maxvaluereceived = st.text_input('max value received')
with col2:
      avgvalreceived = st.text_input('avg val received')
with col3:
      avgvalsent = st.text_input('avg val sent')
with col4:
      totalEthersent = st.text_input('total Ether sent')
with col5:
      totaletherbalance = st.text_input('total ether balance')
with col1:
      ERC20totalEtherreceived = st.text_input('ERC20 total Ether received')
with col2:
      ERC20totalethersent = st.text_input('ERC20 total ether sent')
with col3:
      ERC20totalEthersentcontract = st.text_input('ERC20 total Ether sent contract')
with col4:
      ERC20uniqsentaddr = st.text_input('ERC20 uniq sent addr')
with col5:
       ERC20uniqrectokenname = st.text_input('ERC20 uniq rec token name')
 
    # Repeat similar structure for other input fields and columns

    # code for Predic
transaction_prediction = ''

    # creating a button for Prediction
if st.button('Transaction Result'):
        # Convert input values to numerical types
        Avgminbetweensenttnx = float(Avgminbetweensenttnx)
        NumberofCreatedContracts = float(NumberofCreatedContracts)
        ERC20totalEtherreceived = float(ERC20totalEtherreceived)
        Senttnx=float(Senttnx)
        ReceivedTnx=float(ReceivedTnx)
        NumberofCreatedContracts=float(NumberofCreatedContracts)
        maxvaluereceived=float(maxvaluereceived)
        avgvalreceived =float(avgvalreceived)
        avgvalsent=float(avgvalsent)
        totalEthersent=float(totalEthersent)
        totaletherbalance=float(totaletherbalance)
        ERC20totalEtherreceived=float(ERC20totalEtherreceived)
        ERC20totalethersent=float(ERC20totalethersent)
        ERC20totalEthersentcontract=float(ERC20totalEthersentcontract)
        ERC20uniqsentaddr=float(ERC20uniqsentaddr)
        ERC20uniqrectokenname=float(ERC20uniqrectokenname)





        # Use the input values for model prediction
        transaction_prediction = transaction_model.predict([[Avgminbetweensenttnx, NumberofCreatedContracts, ERC20totalEtherreceived,Senttnx,ReceivedTnx,NumberofCreatedContracts,maxvaluereceived,avgvalreceived,avgvalsent,totalEthersent,totaletherbalance,ERC20totalEtherreceived,ERC20totalethersent,ERC20totalEthersentcontract,ERC20uniqsentaddr,ERC20uniqrectokenname]])
        st.success('The output is {}'.format(transaction_prediction))

if selected == "About":
    st.text("Let's Learn")
    st.text("Built with Streamlit")
