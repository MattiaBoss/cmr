import streamlit as st

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
        st.title("CMR Builder")
        st.write("Step 1: What date?")
        date = st.date_input("Select date", st.session_state.data.get('date'))
        st.session_state.data['date'] = date

    elif st.session_state.step == 2:
        st.title("CMR Builder")
        st.write("Step 2: Choose destination")
        destinations = ['Porto', 'Lisbon', 'Madrid', 'Paris', 'Berlin', 'Rome']
        destination = st.selectbox(
            "Destination", 
            destinations,
            index=destinations.index(st.session_state.data.get('destination')) if st.session_state.data.get('destination') in destinations else 0
        )
        st.session_state.data['destination'] = destination

    elif st.session_state.step == 3:
        st.title("CMR Builder")
        st.write("Step 3: Summary")
        st.write(f"**Date:** {st.session_state.data.get('date')}")
        st.write(f"**Destination:** {st.session_state.data.get('destination')}")

if __name__ == "__main__":
    main()
