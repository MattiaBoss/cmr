import streamlit as st
import pandas as pd

<<<<<<< HEAD
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
=======
def main():
    if 'step' not in st.session_state:
        st.session_state.step = 1
    if 'data' not in st.session_state:
        st.session_state.data = {}

    # Navigation buttons
    back_disabled = st.session_state.step == 1
    next_disabled = st.session_state.step == 3

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back", disabled=back_disabled):
            st.session_state.step -= 1
    with col2:
        if st.button("Next", disabled=next_disabled):
            st.session_state.step += 1

    # Pages
    if st.session_state.step == 1:
        st.write("Step 1: What date?")
        date = st.date_input("Select date", st.session_state.data.get('date'))
        st.session_state.data['date'] = date

    elif st.session_state.step == 2:
        st.write("Step 2: Choose destination")
        destinations = ['Porto', 'Lisbon', 'Madrid', 'Paris', 'Berlin', 'Rome']
        destination = st.selectbox("Destination", destinations, index=destinations.index(st.session_state.data.get('destination')) if st.session_state.data.get('destination') in destinations else 0)
        st.session_state.data['destination'] = destination

    elif st.session_state.step == 3:
        st.write("Step 3: Summary")
        st.write(f"Date: {st.session_state.data.get('date')}")
        st.write(f"Destination: {st.session_state.data.get('destination')}")
>>>>>>> d369d5a (Added multi-step form)

