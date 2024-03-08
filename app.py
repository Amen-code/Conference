import streamlit as st

# List of random visitor names

def main():
    st.set_page_config(" Hammamet conference 2024",page_icon="conference.png")
    st.title("Stochastics in Mathematical Finance and Physics Conference")
    st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">', unsafe_allow_html=True)
    st.markdown("Time and place: <i class='fas fa-clock'></i> Oct. 21–Oct. 25, 2024, <i class='fas fa-map-marker-alt'></i> Radisson Blue Resort Thalasso, Hammamet, Tunisia", unsafe_allow_html=True)
    st.write("The conference is an occasion to bring together researchers in the beautiful Hammamet to discuss recent developments in stochastics with applications to mathematical finance and  physics  .")
    
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
    
    st.subheader(":blue[Call for Abstracts]")
    st.write("A call for abstract is open to propose a contributed talk or a poster. There are limited slots for contributed talks. The form is [here](https://forms.gle/FXaQ37w8x7CHxDL99).")
    st.error("Deadline for submission is September 5th. You will be notified about your proposed talk/poster within September 15th.")

    # Button to register (redirects to Google Form)
    st.subheader(":blue[Registration]")
    st.write("The registration form is available [here](https://docs.google.com/forms/d/e/1FAIpQLScJtPavmI45WvgrrMSHVJUc6xAcEktuBd--JZ53DgQWjVBZXg/viewform).")

    st.subheader(":blue[Program]")
    st.write("A full list of speakers will be available together with the program.")

    st.subheader(":blue[Transport]")
    st.write("The best way to reach the conference venue for international participants is to fly to the International airport of Tunis-Carthage. Local transportation between the airport and the conference hotel is organized and included in the rates. Please fill the registration form above to secure the service.")

    st.subheader(":blue[Sponsors]")
    st.write("This event is organized by the collaboration of several universities and organizations. Financial support is also received from FWO Scientific Research Network ModSimFIE.")

    st.subheader(":blue[Organizers]")
    organizers = [
        "**Saloua Mani Aouadi**", 
        "**Giulia di Nunno**", 
        "**Olfa Draouil**", 
        "**Martin Friesen**", 
        "**Asma Khedher**", 
        "**Astrid Hilbert**", 
        "**Bernt Øksendal**", 
        "**Barbara Rüdiger**",
        "**Josef Teichmann**",
        "**Nizar Touzi**",
        "**Michèle Vanmaele**"
    ]
    st.write(", ".join(organizers))
if __name__ == '__main__':
    main()
