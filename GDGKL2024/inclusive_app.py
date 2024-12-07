import streamlit as st
import pandas as pd
import altair as alt

# Tabs for separating sections
tab1, tab2 = st.tabs([ "Static Dynamic Chart Gen","Inclusive Dynamic Chart Gen"])

# Tab 1: Static Chart App
with tab1:
    st.title("Static Dynamic Chart Gen")
    st.write("This form-based application demonstrates a simpler format without custom options.")

    # Application form
    with st.form("static_data_entry_form"):
        st.subheader("Enter Data")
        categories = st.text_input("Enter categories (comma-separated):", key="static_categories")
        values = st.text_input("Enter values (comma-separated):", key="static_values")

        # Submit button
        submitted_static = st.form_submit_button("Submit")

    # Generate chart upon form submission
    if submitted_static:
        try:
            # Process input data
            category_list = [c.strip() for c in categories.split(",")]
            value_list = [int(v.strip()) for v in values.split(",")]

            if len(category_list) != len(value_list):
                st.error("The number of categories must match the number of values.")
            else:
                # Create a DataFrame
                data = pd.DataFrame({"Category": category_list, "Values": value_list})

                # Define a fixed color palette
                colors = alt.Scale(domain=data["Category"].tolist(), range=["#FF5733", "#33FF57", "#3357FF", "#F3FF33"])

                # Build the chart
                chart = alt.Chart(data).mark_bar().encode(
                    x="Category",
                    y="Values",
                    color=alt.Color("Category", scale=colors)
                ).properties(width=500, height=300)

                # Display the chart
                st.altair_chart(chart, use_container_width=True)

        except ValueError:
            st.error("Please enter valid numerical values for the 'Values' field.")


# Tab 2: Customizable Chart App
with tab2:
    st.title("Inclusive Dynamic Chart Gen")
    st.write("This app demonstrates inclusivity through customizable forms and dynamic visualizations.")

    # Sidebar for settings
    st.sidebar.header("Settings")

    # Font size adjustment
    font_size = st.sidebar.slider("Select Font Size", min_value=12, max_value=24, value=16)

    # Language selection
    languages = {
        "English": {"title": "Enter Data", "category": "Category", "value": "Value", "submit": "Submit",
                    "category_placeholder": "Enter categories (comma-separated):",
                    "value_placeholder": "Enter values (comma-separated):"},
        "Spanish": {"title": "Introducir Datos", "category": "Categoría", "value": "Valor", "submit": "Enviar",
                    "category_placeholder": "Ingrese categorías (separadas por comas):",
                    "value_placeholder": "Ingrese valores (separados por comas):"},
        "French": {"title": "Entrer les Données", "category": "Catégorie", "value": "Valeur", "submit": "Soumettre",
                   "category_placeholder": "Entrez les catégories (séparées par des virgules):",
                   "value_placeholder": "Entrez les valeurs (séparées par des virgules):"},
        "Hindi": {"title": "डेटा दर्ज करें", "category": "श्रेणी", "value": "मूल्य", "submit": "जमा करें",
                  "category_placeholder": "श्रेणियाँ दर्ज करें (अल्पविराम से अलग करें):",
                  "value_placeholder": "मान दर्ज करें (अल्पविराम से अलग करें):"},
        "Malay": {"title": "Masukkan Data", "category": "Kategori", "value": "Nilai", "submit": "Hantar",
                  "category_placeholder": "Masukkan kategori (dipisahkan dengan koma):",
                  "value_placeholder": "Masukkan nilai (dipisahkan dengan koma):"},
        "Chinese": {"title": "输入数据", "category": "类别", "value": "值", "submit": "提交",
                    "category_placeholder": "输入类别（用逗号分隔）:",
                    "value_placeholder": "输入值（用逗号分隔）:"}
    }
    selected_language = st.sidebar.selectbox("Choose Language", options=list(languages.keys()))
    lang = languages[selected_language]

    # Toggle for color-blind-friendly mode
    color_blind_mode = st.sidebar.checkbox("Enable Color-Blind-Friendly Palette", value=False)

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
        categories = st.text_input(lang["category_placeholder"], key="categories")

        st.markdown(f'<div class="custom-font">{lang["value"]}</div>', unsafe_allow_html=True)
        values = st.text_input(lang["value_placeholder"], key="values")

        # Submit button with localized label
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

                # Fix the domain for Altair scale (must be a list)
                domain = data["Category"].tolist()

                # Define color palette based on toggle
                if color_blind_mode:
                    color_palette = ["#D55E00", "#E69F00", "#0072B2", "#009E73"]
                else:
                    color_palette = ["#FF5733", "#33FF57", "#3357FF", "#F3FF33"]

                # Create a color scale with the selected palette
                colors = alt.Scale(domain=domain, range=color_palette)

                # Build the chart
                chart = alt.Chart(data).mark_bar().encode(
                    x="Category",
                    y="Values",
                    color=alt.Color("Category", scale=colors)
                ).properties(width=500, height=300)

                # Display the chart
                st.altair_chart(chart, use_container_width=True)

        except ValueError:
            st.error("Please enter valid numerical values for the 'Values' field.")

