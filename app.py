import streamlit as st



def generate_card(name, university):
    st.write(f"**{name}  {university}**")
    
    
def main():
    st.set_page_config(" Hammamet conference 2024",page_icon="Logo.png")
    st.title("Stochastics in Mathematical Finance and Physics Conference")
    st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">', unsafe_allow_html=True)
    st.markdown("Time and place: <i class='fas fa-clock'></i> Oct. 21–Oct. 25, 2024, <i class='fas fa-map-marker-alt'></i> Radisson Blue Resort Thalasso, Hammamet, Tunisia", unsafe_allow_html=True)
    st.write("The conference is an occasion to bring together researchers in the beautiful Hammamet to discuss recent developments in stochastics with applications to mathematical   finance and  physics")
    # Display conference name
    st.markdown("""
    
    """,unsafe_allow_html=True)
    st.markdown(
        """
       <style>
       footer {visibility:hidden;}
       #MainMenu {visibility: hidden;}
       [data-testid="stSidebar"][aria-expanded="true"]{min-width: 250px;max-width: 250px;}
       </style>
       """,
        unsafe_allow_html=True,
    )  

    # Display hotel image
    
    st.image('hotel.jpg', width = 600 ,output_format = "JPEG")

    # Button to register (redirects to Google Form)
    st.subheader(":blue[ For Registration]")
    st.write("The registration form is available [here](https://docs.google.com/forms/d/e/1FAIpQLScJtPavmI45WvgrrMSHVJUc6xAcEktuBd--JZ53DgQWjVBZXg/viewform).")
    st.error("Deadline for submission is September 5th.")

    st.subheader(":blue[Program]")
    st.write("A full list of speakers will be available together with the program.")

    st.subheader(":blue[Transport]")
    st.write("The best way to reach the conference venue for international participants is to fly to the International airport of Tunis-Carthage. Local transportation between the airport and the conference hotel is organized and included in the rates. Please fill the registration form above to secure the service.")

    st.subheader(":blue[Sponsors]")
    st.write("This event is organized by the collaboration of several universities and organizations. Financial support is also received from FWO Scientific Research Network ModSimFIE .")

    st.subheader(":blue[Organizers]")
    organizers = [
    ("Saloua Mani Aouadi", "(Tunis El Manar University)"),
    ("Giulia di Nunno", "(University of Oslo)"),
    ("Olfa Draouil", "(Tunis El Manar University)"),
    ("Martin Friesen", "(Dublin City University)"),
    ("Asma Khedher", "(University of Amsterdam)"),
    ("Astrid Hilbert", "(Linnaeus University)"),
    ("Bernt Øksendal", "(University of Oslo)"),
    ("Barbara Rüdiger", "(Bergische University Wuppertal)"),
    ("Nizar Touzi", "(New York University)"),
    ("Michèle Vanmaele", "(Ghent University)"),
    ("Josef Teichmann", "(ETH Zürich)")
]
    for i in range(0, len(organizers), 3):
        row = organizers[i:i+3]
        col1, col2, col3 = st.columns(3)

        with col1:
            if i < len(organizers):
                generate_card(row[0][0], row[0][1])
        with col2:
            if i + 1 < len(organizers):
                generate_card(row[1][0], row[1][1])
        with col3:
            if i + 2 < len(organizers):
                generate_card(row[2][0], row[2][1])
    
    st.image("Logo.png")
    
    
if __name__ == '__main__':
    main()
