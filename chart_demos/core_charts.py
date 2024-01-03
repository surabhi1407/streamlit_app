import streamlit as st
import pandas as pd
import numpy as np

st.divider()
#
# #Bar chart
# st.write('Bar chart')
# bar_data = {'Categories': ['A', 'B', 'C'], 'Values': [10, 20, 30]}
# df = pd.DataFrame(bar_data)
# st.bar_chart(df, x="Categories", y="Values")
#
# st.divider()
# #
# #Line chart
# st.write('Line chart')
# line_data = pd.DataFrame({'Date': pd.date_range(start='1/1/2020', periods=30), 'Value': np.random.randn(30).cumsum()})
# st.line_chart(line_data.set_index('Date'))
#
# st.divider()

# #Area chart
# st.write('Area chart')
# area_data = pd.DataFrame({'Time': range(1, 11), 'Value': np.random.randn(10).cumsum()})
# st.area_chart(area_data.set_index('Time'))
#
# st.divider()

# #Scatter chart
# st.write('Scatter chart')
# data = pd.DataFrame(np.random.randn(100, 2), columns=['A', 'B'])
# st.scatter_chart(data)
#
# st.divider()
#
#Map chart
st.write('Map chart')
data = pd.DataFrame({'lat': [37.77, 38.91], 'lon': [-122.41, -77.04]})
st.map(data)

