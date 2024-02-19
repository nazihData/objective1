import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# Function to create circle gauge chart
def circle_gauge(value, title):
    # Define colorscale based on completion percentage
    if value < 50:
        color = '#ff6347'  # red
    elif value < 75:
        color = '#ffd700'  # yellow
    else:
        color = '#32cd32'  # green

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': title},
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={'axis': {'range': [0, 100]}, 'bar': {'color': color}}
    ))
    return fig

def main():
    st.set_page_config(page_title="KPI Follow Up")

    # Page Title
    st.markdown("<h1 style='text-align: center; font-size: 45px;'>Overview Objectives Process</h1>", unsafe_allow_html=True)

    # File uploader for uploading data file
    uploaded_file = st.file_uploader("Upload Data File", type=['csv', 'xlsx'])

    if uploaded_file is not None:
        # Load data from the uploaded file
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith('.xlsx'):
                df = pd.read_excel(uploaded_file)
            else:
                st.error("Unsupported file format. Please upload a CSV or Excel file.")
                return
        except Exception as e:
            st.error(f"Error occurred while loading the file: {str(e)}")
            return

        # Check if DataFrame contains expected columns
        expected_columns = ['Sector', 'Percentage']
        if not all(col in df.columns for col in expected_columns):
            st.error(f"Data file must contain columns: {', '.join(expected_columns)}")
            return

        # Dropdown to select sector
        sector_name = st.selectbox("Select Sector", df['Sector'])

        # Get the value for the selected sector
        value = df[df['Sector'] == sector_name]['Percentage'].values[0]

        # Display circle gauge
        st.markdown(f"## {sector_name} Completion Percentage")
        st.plotly_chart(circle_gauge(value, sector_name))

if __name__ == "__main__":
    main()
