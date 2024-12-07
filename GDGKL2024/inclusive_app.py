import streamlit as st
import pandas as pd
import altair as alt

# App title
st.title("Inclusive Form-Based Web Application")
st.write("This app demonstrates inclusivity through customizable forms and dynamic visualizations.")

# Sidebar for settings
st.sidebar.header("Settings")

# Font size adjustment
font_size = st.sidebar.slider("Select Font Size", min_value=12, max_value=24, value=16)

# Language selection
languages = {
    "English": {"title": "Enter Data", "category": "Category", "value": "Value", "submit": "Submit"},
    "Spanish": {"title": "Introducir Datos", "category": "Categoría", "value": "Valor", "submit": "Enviar"},
    "French": {"title": "Entrer les Données", "category": "Catégorie", "value": "Valeur", "submit": "Soumettre"},
    "Hindi": {"title": "डेटा दर्ज करें", "category": "श्रेणी", "value": "मूल्य", "submit": "जमा करें"}
}
selected_language = st.sidebar.selectbox("Choose Language", options=list(languages.keys()))
lang = languages[selected_language]

# Set custom font size using markdown
st.markdown(
    f"""
    <style>
    .custom-font {{
        font-size: {font_size}px !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Application form
st.markdown(f'<h2 class="custom-font">{lang["title"]}</h2>', unsafe_allow_html=True)


with st.form("data_entry_form"):
    st.markdown(f'<div class="custom-font">{lang["category"]}</div>', unsafe_allow_html=True)
    categories = st.text_input("Enter categories (comma-separated):", key="categories")

    st.markdown(f'<div class="custom-font">{lang["value"]}</div>', unsafe_allow_html=True)
    values = st.text_input("Enter values (comma-separated):", key="values")

    submitted = st.form_submit_button(lang["submit"])

# Generate chart upon form submission
if submitted:
    try:
        # Process input data
        category_list = [c.strip() for c in categories.split(",")]
        value_list = [int(v.strip()) for v in values.split(",")]

        if len(category_list) != len(value_list):
            st.error("The number of categories must match the number of values.")
        else:
            # Create a DataFrame
            data = pd.DataFrame({"Category": category_list, "Values": value_list})

            # Chart with an accessible color palette
            colors = alt.Scale(domain=data["Category"], range=["#D55E00", "#E69F00", "#0072B2", "#009E73"])
            chart = alt.Chart(data).mark_bar().encode(
                x="Category",
                y="Values",
                color=alt.Color("Category", scale=colors)
            ).properties(width=500, height=300)

            # Display the chart
            st.altair_chart(chart, use_container_width=True)

    except ValueError:
        st.error("Please enter valid numerical values for the 'Values' field.")

# Add footer
st.write("---")
st.write(f'<div class="custom-font">This app showcases inclusive design principles for form-based applications.</div>', unsafe_allow_html=True)
