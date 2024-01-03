import streamlit as st
import pandas as pd
import random
from collections import Counter

# Sample product data
products = ['Phone', 'Laptop', 'Headphones', 'Camera', 'Smartwatch', 'Tablet', 'Charger', 'Keyboard', 'Mouse', 'Speaker']

# Dummy historical purchase records
purchase_data = [
    ['Phone', 'Charger', 'Headphones'],
    ['Laptop', 'Mouse', 'Keyboard'],
    ['Smartwatch', 'Phone'],
    ['Tablet', 'Charger'],
    ['Camera', 'Laptop'],
    # ... more records ...
]

# Convert to DataFrame
df_purchase = pd.DataFrame(purchase_data, columns=['Item1', 'Item2', 'Item3'])

def get_recommendations(selected_products, df, num_recommendations=3):
    """Generate recommendations based on historical data."""
    # Flatten all items in the dataset
    all_items = df.values.flatten()

    # Count the frequency of each item being bought
    item_freq = Counter(all_items)

    # Remove selected products from the frequency counter
    for product in selected_products:
        del item_freq[product]

    # Get the most common items
    common_items = item_freq.most_common(num_recommendations)
    return [item[0] for item in common_items]

# Streamlit application layout
st.title('Product Recommendation System')
st.write('Select one or more products to see intelligent recommendations.')

# User selects multiple products
selected_products = st.multiselect('Choose products:', products, default=None)

# Generate recommendations if any product is selected
if selected_products:
    recommendations = get_recommendations(selected_products, df_purchase)

    # Create DataFrame for recommendations
    likelihoods = [random.randint(50, 99) for _ in recommendations]  # Mock likelihood percentages
    df_recommendations = pd.DataFrame({'Recommended Product': recommendations, 'Likelihood of Purchase (%)': likelihoods})

    st.write('Recommended Products:')
    st.dataframe(df_recommendations)
else:
    st.write('Please select at least one product to see recommendations.')
