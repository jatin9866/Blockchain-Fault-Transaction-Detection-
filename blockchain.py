import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

# Load the saved model
transaction_model = pickle.load(open('C:/Users/SLIM 3/Desktop/block chain fault transaction.ff/block chain fault transaction/transaction.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Transaction Fault Prediction using ML', ['Home'], default_index=0)

# Home page
if selected == 'Home':
    # Page title
    st.title('Transaction Prediction using ML')
    st.image("download1.jpg")

    # Get the input data from the user
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        Avgminbetweensenttnx = st.text_input('Avg min between sent tnx')
    with col2:
        Avgminbetweenreceivedtnx = st.text_input('Avg min between received tnx')
    with col3:
        time_diff_input = st.text_input('Time Diff between first and last (Mins)')
    with col4:
        Senttnx = st.text_input('Sent tnx')
    with col5:
        ReceivedTnx = st.text_input('Received Tnx')

    with col1:
        NumberofCreatedContracts = st.text_input('Number of Created Contracts')
    with col2:
        maxvaluereceived = st.text_input('Max value received')
    with col3:
        avgvalreceived = st.text_input('Avg val received')
    with col4:
        avgvalsent = st.text_input('Avg val sent')
    with col5:
        totalEthersent = st.text_input('Total Ether sent')
    with col1:
        totaletherbalance = st.text_input('Total ether balance')
    with col2:
        ERC20totalEtherreceived = st.text_input('ERC20 total Ether received')
    with col3:
        ERC20totalethersent = st.text_input('ERC20 total Ether sent')
    with col4:
        ERC20totalEthersentcontract = st.text_input('ERC20 total Ether sent contract')
    with col5:
        ERC20uniqsentaddr = st.text_input('ERC20 uniq sent addr')
    with col1:
        ERC20uniqrectokenname = st.text_input('ERC20 uniq rec token name')

    # Repeat similar structure for other input fields and columns

    # Prediction code
    transaction_prediction = None

    # Create a button for Prediction
    if st.button('Transaction Result'):
        try:
            # Convert inputs to floats
            input_data = [
                float(Avgminbetweensenttnx),
                float(Avgminbetweenreceivedtnx),
                float(time_diff_input) if time_diff_input else None,
                float(Senttnx),
                float(ReceivedTnx),
                float(NumberofCreatedContracts),
                float(maxvaluereceived),
                float(avgvalreceived),
                float(avgvalsent),
                float(totalEthersent),
                float(totaletherbalance),
                float(ERC20totalEtherreceived),
                float(ERC20totalethersent),
                float(ERC20totalEthersentcontract),
                float(ERC20uniqsentaddr),
                float(ERC20uniqrectokenname)
            ]

            # Make prediction
            transaction_prediction = transaction_model.predict([input_data])

            # Display the result with interpretation
            if transaction_prediction == 1:
                st.success('The prediction result is Fraud (1).')
            else:
                st.success('The prediction result is Not Fraud (0).')
        except ValueError as e:
            st.error(f"Error: {e}")

# Add other pages (e.g., About) as needed

