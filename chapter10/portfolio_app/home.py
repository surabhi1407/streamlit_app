import streamlit as st
import os

def show():
    st.set_page_config(page_title='John Newman Portfolio', layout='wide')

    tabs = ['Home', 'Portfolio', 'Projects', 'Experience', 'Contact']
    chosen_tab = st.tabs(tabs)

    col1, col2, col3, col4 = st.columns((1,1,1,1))

    with col2:
        st.header("John Turner")

        st.write("""
                    ###### Data Exploration | Data Visualization | Story Telling 
                    Hello! I'm John Turner, a passionate data professional focused on building stories from the data. I love analyzing the data, cleaning it and looking for patterms. 
                    I have considerable experience in building complex pipelines for Data ingestion and modeling. I have worked with numerous business and Creative stakeholders. 
                    I believe every Dataset has a story to be told 
                """)
        st.write("""
                        - **Key Skills**: 
                            - Data Exploration
                            - Data Modeling
                            - Building Ingestion pipeline 
                            - Business Intelligence
                                                        
                        - **Hobbies and Interests**: 
                            - Photography 
                            - Travel 
                            - Reading
                    """)
        st.markdown("[LinkedIn](https://www.linkedin.com/in/johnturner)[|Twitter|](https://www.twitter.com/johnturner) [GitHub](https://www.github.com/johnturner) [|Instagram](https://www.instagram.com/johnturner)")

    with col3:
        base_dir = os.path.dirname(__file__)
        image_path = os.path.join(base_dir, 'images', 'portfolio1.png')
        st.image(image_path, width=500)

if __name__ == "__main__":
    show()
