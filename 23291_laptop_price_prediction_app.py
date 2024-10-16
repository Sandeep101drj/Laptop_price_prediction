import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Import the model
pipe_rf = pickle.load(open('pipe_rf.pkl', 'rb'))
laptop_dataset = pickle.load(open('laptop_dataset.pkl', 'rb'))

# page title
st.set_page_config(page_title="Laptop Price Predictor", layout="wide")

# CSS for styling
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #f0f2f5;
        padding: 20px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px;
        border: None;
        border-radius: 5px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    h2 {
        color: #2C3E50;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        color: #555;
    }
    .nav {
        position: absolute;
        top: 20px;
        right: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Navigation using radio buttons
page = st.radio("Select a page", ["Home", "About"], horizontal=True, key='page_nav')

# Home Page
if page == "Home":
    # Title and description
    st.title("💻 Sandeep's Laptop Price Predictor")
    st.markdown("Select the specifications of the laptop, and we will predict its price.")

    # Laptop specifications inputs
    st.sidebar.header("📊 Laptop Specifications")
    company = st.sidebar.selectbox('🖥️ Brand', laptop_dataset['Company'].unique())
    type_name = st.sidebar.selectbox('🖥️ Type', laptop_dataset['TypeName'].unique())
    ram = st.sidebar.selectbox('🧮 RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
    weight = st.sidebar.number_input('⚖️ Weight of the Laptop (in kg)', min_value=0.0)
    touchscreen = st.sidebar.selectbox('🖱️ Touchscreen', ['No', 'Yes'])
    ips = st.sidebar.selectbox('🖱️ IPS', ['No', 'Yes'])
    screen_size = st.sidebar.slider('📏 Screen Size (in inches)', 10.0, 18.0, 13.0)
    resolution = st.sidebar.selectbox('🖥️ Screen Resolution', ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'])
    cpu = st.sidebar.selectbox('💻 CPU', laptop_dataset['Cpu brand'].unique())
    hdd = st.sidebar.selectbox('💽 HDD (in GB)', [0, 128, 256, 512, 1024, 2048])
    ssd = st.sidebar.selectbox('💾 SSD (in GB)', [0, 8, 128, 256, 512, 1024])
    gpu = st.sidebar.selectbox('🖥️ GPU', laptop_dataset['Gpu brand'].unique())
    os = st.sidebar.selectbox('📁 OS', laptop_dataset['os'].unique())

    # Prediction button
    if st.sidebar.button('🔮 Predict Price'):
        with st.spinner('Predicting...'):
            # Query preparation
            touchscreen = 1 if touchscreen == 'Yes' else 0
            ips = 1 if ips == 'Yes' else 0
            X_res = int(resolution.split('x')[0])
            Y_res = int(resolution.split('x')[1])
            ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size

            query_df = pd.DataFrame([[company, type_name, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os]],
                                     columns=['Company', 'TypeName', 'Ram', 'Weight', 'Touchscreen', 'Ips', 
                                              'ppi', 'Cpu brand', 'HDD', 'SSD', 'Gpu brand', 'os'])

            # Prediction
            predicted_price = pipe_rf.predict(query_df)

            # Display result
            st.markdown(f"<h2>The predicted price of this configuration is Rs. {int(np.exp(predicted_price[0]))}</h2>", unsafe_allow_html=True)

# About Page
elif page == "About":
    st.title("📚 About This Project")
    st.markdown("""
    # **Laptop Price Prediction**

## **Project Overview**

In today’s digital age, laptops are indispensable tools for both personal and professional use. 
However, the vast array of laptop brands, configurations, and price points often complicates the purchasing process for consumers. 
This project addresses the challenge of understanding laptop pricing dynamics by developing a machine learning model that predicts laptop prices based on various features, 
such as brand, processor type, RAM, storage, and graphics card.

## **Key Features**

- **Predictive Modeling**: A machine learning model that accurately predicts laptop prices based on input features.
- **Interactive Web Application**: An intuitive Streamlit application that allows users to input specific laptop specifications and receive real-time price predictions.
- **Data-Driven Insights**: Users can explore how different features impact laptop pricing, enabling informed purchasing decisions.

## **Project Goals**

The primary goal of this project is to empower consumers with better decision-making tools while providing retailers with valuable insights into market trends and pricing strategies. 
By leveraging machine learning techniques, the project aims to enhance transparency in laptop pricing and simplify the selection process for users.

## **Conclusion**

This project serves as a comprehensive solution for understanding and predicting laptop prices in an increasingly complex market. 
Through the integration of machine learning and user-friendly web applications, we aim to deliver actionable insights that benefit both consumers and retailers alike. 
    """)

# Footer
st.markdown("---")
st.markdown("<div class='footer'>Made by Sandeep Pradhan</div>", unsafe_allow_html=True)
