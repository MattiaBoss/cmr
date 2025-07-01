import streamlit as st
import pandas as pd

def step1():
    st.header("Step 1: Date and Destination")
    date = st.date_input("What date?")
    destinations = ['Porto', 'Lisbon', 'Madrid', 'Paris', 'Berlin', 'Rome']
    destination = st.selectbox("Choose destination", destinations)
    return date, destination

def step2():
    st.header("Step 2: Upload Excel")
    excel_file = st.file_uploader("Upload Excel file", type=["xlsx"])
    df = None
    if excel_file:
        df = pd.read_excel(excel_file)
        st.write("Units found:")
        st.dataframe(df)
    return excel_file, df

def step3(df):
    st.header("Step 3: Select Units")
    if df is not None:
        units = st.multiselect("Select units to include", options=df['Unit'].tolist())
    else:
        units = []
    return units

def step4():
    st.header("Step 4: How many kilos?")
    kilos = st.number_input("Enter kilos", min_value=0)
    return kilos

def main():
    if 'step' not in st.session_state:
        st.session_state.step = 1

    if 'data' not in st.session_state:
        st.session_state.data = {}

    # Navigation buttons
    col1, col2 = st.columns([1,1])
    with col1:
        if st.session_state.step > 1:
            if st.button("Back"):
                st.session_state.step -= 1
    with col2:
        if st.session_state.step < 4:
            if st.button("Next"):
                st.session_state.step += 1

    # Step content
    if st.session_state.step == 1:
        date, destination = step1()
        st.session_state.data['date'] = date
        st.session_state.data_

