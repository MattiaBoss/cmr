import streamlit as st
import pandas as pd

def main():
    st.title("CMR Builder")

    # Initialize session state variables
    if "step" not in st.session_state:
        st.session_state.step = 1
    if "date_cmr" not in st.session_state:
        st.session_state.date_cmr = None
    if "location" not in st.session_state:
        st.session_state.location = None
    if "numar_auto" not in st.session_state:
        st.session_state.numar_auto = ""
    if "numar_sigiliu" not in st.session_state:
        st.session_state.numar_sigiliu = ""
    if "numar_kg" not in st.session_state:
        st.session_state.numar_kg = ""
    if "excel_file" not in st.session_state:
        st.session_state.excel_file = None
    if "df" not in st.session_state:
        st.session_state.df = None
    if "pallet_numbers" not in st.session_state:
        st.session_state.pallet_numbers = ""

    # Location dictionary: name → full address for PDF
    location_dict = {
        "Fan Romania": """FAN COURIER EXPRESS SRL
SOS. DE CENTURA BUCURESTI NR 32
STEFANESTII DE JOS IF 077175
ROMANIA""",
        "Fan Bulgaria": """FAN COURIER
（Econt）
Sofia, Gorublyane district,5a Eng. Georgi Belov Street
GPS Location: 42.63832, 23.40207""",
        "Boxnow": """Box NOW
（Boulevard "Professor Tsvetan 
Lazarov" 8, 1592 Sofia""",
        "Express One": """Express One  
1582 Sofia, 117 "Tsvetan 
Lazarov" blvd.""",
        "Packeta": """PACKETA ROMANIA SRL
STR. VIRGINIA, NR. 4
CTP PARK A1 KM 13, DRAGOMIRESTI
ROMANIA""",
        "Equick": """Equick - TEMU Bulgarian Post
r.d. Nova Vrazhdebna, 31 Chelopeshko shose Str.,
1900 Sofia, Bulgaria"""
    }

    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back", disabled=st.session_state.step == 1):
            st.session_state.step -= 1
    with col2:
        if st.button("➡️ Next", disabled=st.session_state.step == 8):
            st.session_state.step += 1

    # Step 1: Data CMR (date input)
    if st.session_state.step == 1:
        st.subheader("Data CMR")
        st.session_state.date_cmr = st.date_input("Selectați data CMR:", value=st.session_state.date_cmr)

    # Step 2: Locatie (select location)
    elif st.session_state.step == 2:
        st.subheader("Locație")
        options = list(location_dict.keys())
        index = options.index(st.session_state.location) if st.session_state.location in options else 0
        st.session_state.location = st.selectbox("Selectați locația:", options, index=index)

    # Step 3: (You said summary last, so we skip summary here or just a placeholder)
    elif st.session_state.step == 3:
        st.subheader("")

    # Step 4: Numar auto (text input)
    elif st.session_state.step == 4:
        st.subheader("Număr auto")
        st.session_state.numar_auto = st.text_input("Introduceți numărul auto:", value=st.session_state.numar_auto)

    # Step 5: Numar sigiliu (text input)
    elif st.session_state.step == 5:
        st.subheader("Număr sigiliu")
        st.session_state.numar_sigiliu = st.text_input("Introduceți numărul sigiliu:", value=st.session_state.numar_sigiliu)

    # Step 6: Upload Excel file
    elif st.session_state.step == 6:
        st.subheader("Încarcă fișierul EXCEL cu paleți")
        uploaded_file = st.file_uploader("Alegeți fișierul Excel", type=["xls", "xlsx"])
        if uploaded_file is not None:
            try:
                df = pd.read_excel(uploaded_file)
                st.session_state.df = df
                st.success("Fișier încărcat cu succes!")
            except Exception as e:
                st.error(f"Eroare la încărcarea fișierului: {e}")
        elif st.session_state.df is not None:
            st.info("Fișierul este deja încărcat.")

    # Step 7: Input pallet numbers and Numar kg
    elif st.session_state.step == 7:
        st.subheader("Ce paleți?")
        st.write("Introduceți numerele paleților separate prin virgulă.")
        pallets_input = st.text_input("Numere paleți:", value=st.session_state.pallet_numbers)
        st.session_state.pallet_numbers = pallets_input

        st.subheader("Număr kg")
        st.session_state.numar_kg = st.text_input("Introduceți numărul de kg:", value=st.session_state.numar_kg)

        if st.session_state.df is not None and pallets_input.strip():
            pallets_list = [p.strip() for p in pallets_input.split(",") if p.strip()]

            # Filter dataframe rows where Package ID matches any pallet number
            if "Package ID" in st.session_state.df.columns:
                df_filtered = st.session_state.df[st.session_state.df["Package ID"].astype(str).isin(pallets_list)]
            else:
                st.error("Coloana 'Package ID' nu există în fișierul Excel.")
                df_filtered = pd.DataFrame()  # empty df to avoid errors

            if not df_filtered.empty:
                try:
                    # Identification Number in column G (index 6)
                    # Number of Boxes in column D (index 3)
                    id_numbers = df_filtered.iloc[:, 6].astype(str)
                    boxes = df_filtered.iloc[:, 3].astype(float)
                    grouped = df_filtered.groupby(id_numbers).agg({df_filtered.columns[3]: "sum"})
                    grouped = grouped.reset_index()
                    grouped.columns = ["Identification Number", "Total Boxes"]

                    st.write("Date extrase:")
                    st.dataframe(grouped)
                except Exception as e:
                    st.error(f"Eroare la procesarea datelor: {e}")
            else:
                st.warning("Nu s-au găsit paleții specificați în fișier.")
        else:
            st.info("Introduceți numerele paleților și încărcați un fișier Excel pentru a afișa date.")

    # Step 8: Final Summary
    elif st.session_state.step == 8:
        st.subheader("Rezumat Final")
        st.write(f"**Data CMR:** {st.session_state.date_cmr}")
        st.write(f"**Locație:** {st.session_state.location}")
        st.write(f"**Număr auto:** {st.session_state.numar_auto}")
        st.write(f"**Număr sigiliu:** {st.session_state.numar_sigiliu}")
        st.write(f"**Număr kg:** {st.session_state.numar_kg}")
        st.write(f"**Numere paleți:** {st.session_state.pallet_numbers}")

if __name__ == "__main__":
    main()
