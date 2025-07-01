import streamlit as st

def main():
    st.title("CMR BUILDER")

    date = st.date_input("What date?")
    
    destinations = ['Porto', 'Lisbon', 'Madrid', 'Paris', 'Berlin', 'Rome']
    destination = st.selectbox("Choose destination", destinations)

    excel_file = st.file_uploader("Upload Excel file", type=["xlsx"])

    kilos = st.number_input("How many kilos?", min_value=0)

    if st.button("Submit"):
        st.write("You entered:")
        st.write(f"Date: {date}")
        st.write(f"Destination: {destination}")
        if excel_file:
            st.write(f"Excel file uploaded: {excel_file.name}")
        else:
            st.write("No Excel file uploaded")
        st.write(f"Kilos: {kilos}")

if __name__ == "__main__":
    main()
