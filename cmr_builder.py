import streamlit as st

def main():
    st.title("CMR Builder")

    if "step" not in st.session_state:
        st.session_state.step = 1
    if "date" not in st.session_state:
        st.session_state.date = None
    if "destination" not in st.session_state:
        st.session_state.destination = None

    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back", disabled=st.session_state.step == 1):
            st.session_state.step -= 1
    with col2:
        if st.button("➡️ Next", disabled=st.session_state.step == 3):
            st.session_state.step += 1

    # Steps
    if st.session_state.step == 1:
        st.subheader("Step 1: What date?")
        st.session_state.date = st.date_input("Select date", value=st.session_state.date)

    elif st.session_state.step == 2:
        st.subheader("Step 2: Choose destination")
        options = ['Porto', 'Lisbon', 'Madrid', 'Paris', 'Berlin', 'Rome']
        index = options.index(st.session_state.destination) if st.session_state.destination in options else 0
        st.session_state.destination = st.selectbox("Select destination", options, index=index)

    elif st.session_state.step == 3:
        st.subheader("Step 3: Summary")
        st.write(f"**Date:** {st.session_state.date}")
        st.write(f"**Destination:** {st.session_state.destination}")

if __name__ == "__main__":
    main()
