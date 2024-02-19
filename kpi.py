import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
#from streamlit_card import card
import base64
from io import StringIO, BytesIO
import datetime, calendar
from datetime import datetime, timedelta
import plotly.graph_objects as go



st.set_page_config(page_title = "KPI follow up")

df = pd.read_excel("C:/Users/Surface/Desktop/df.xlsx")
st.markdown("<h1 style='text-align: center; font-size: 45px;'>Overview Objectives Process</h1>", unsafe_allow_html=True)


# Dropdown to select sector

def circle_gauge(value, title):
    # Define colorscale based on completion percentage
    if value < 50:
        color = '#ff6347'  # red
    elif value < 75:
        color = '#ffd700'  # yellow
    else:
        color = '#32cd32'  # green

    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = value,
        title = {'text': title},
        domain = {'x': [0, 1], 'y': [0, 1]},
        gauge = {'axis': {'range': [0, 100]}, 'bar': {'color': color}}
    ))
    return fig

def main():
    sector_name = st.selectbox("Select Sector", df['Sector'])
    
    value = df[df['Sector'] == sector_name]['Percentage'].values[0]
    
    # Display circle gauge
    st.plotly_chart(circle_gauge(value, sector_name))

if __name__ == "__main__":
    main()












