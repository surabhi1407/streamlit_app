import streamlit as st
import os
def portfolio_show():
    st.title('Portfolio')

    # Creating two columns for the expanders
    col1, col2 = st.columns(2)

    with col1:
        with st.expander("Experience & Awards"):
            st.write("""
                    - 5+ Years of experience
                    - Specialized in UX/UI
                    - Marketing Specialization
                    - Graphic Design Certification
                """)

    with col2:
        with st.expander("Education"):
            st.write("""
                    - Post graduation in Computer
                    - Design degree
                    - Marketing course in Udemy
                    - Graphic Design Certification
                """)

    col1, col2, col3 = st.columns((1,2,1))

    with col2 :
        with st.expander("My favorite Projects"):
            st.write("""
                    - Building a Master Data Layer for Analytics and Data Science
                    - Building a self serve data analytics platform for the prganization
                    - Building customer acquisition and churn prediction model
                    - On-going contributor to open-source library 
                """)
            col1, col2, col3 = st.columns((1,2,1))
            with col2:
                base_dir = os.path.dirname(__file__)
                cv_path = os.path.join(base_dir, 'assets', 'John_Turner_CV.pdf')
                if os.path.exists(cv_path):
                    with open(cv_path, "rb") as file:
                        btn = st.download_button(
                            label="Download CV",
                            data=file,
                            file_name="John_Doe_CV.pdf",
                            mime="application/pdf"
                        )
                else:
                    st.write("Reach out to me to get my CV")




