import streamlit as st
import streamlit as st

# タイトルの表示
st.title('My Streamlit App')

# テキストの表示
st.write('Here is our first attempt at using Streamlit to create a web app.')

# データフレームの表示
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charles'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Paris', 'London']}
df = pd.DataFrame(data)
st.write(df)

# チャートの表示
chart_data = pd.DataFrame(
     [[1, 2], [3, 4]],
     columns=['x', 'y'])
st.line_chart(chart_data)
