# Laptop Price Prediction ML Project

## Introduction
This project aims to predict the prices of laptops based on various features using machine learning techniques. By analyzing the impact of different specifications on laptop prices, we can provide valuable insights for potential buyers and retailers.

Dataset included in the repository.

## Overview
The laptop price prediction model leverages multiple machine learning algorithms, including Linear Regression, Ridge Regression, Lasso Regression, K-Nearest Neighbors, Decision Trees, Support Vector Machines, Ensemble Models (AdaBoost, Gradient Boosting, XGBoost, and Voting Regressor), and Random Forest. The dataset contains various features related to laptops, such as brand, processor type, RAM, storage, operating system, and more.

## Objective
The primary objective of this project is to build a robust predictive model that can accurately forecast laptop prices. This involves:
- Data preprocessing and feature engineering
- Exploratory data analysis (EDA) to understand trends and correlations
- Implementation of various regression algorithms
- Hyperparameter tuning to optimize model performance
- To develop an interactive application using Streamlit that allows users to predict laptop prices by entering specific features.

## Description
The project is structured as follows:
1. **Data Preprocessing**: The dataset is cleaned and processed by removing unnecessary columns and handling categorical variables through one-hot encoding.
2. **Exploratory Data Analysis (EDA)**: Insights into price variations based on features are visualized, and correlation matrices are generated to understand relationships between features.
3. **Model Training**: Multiple regression algorithms are trained on the dataset, with train-test splits ensuring a fair evaluation of model performance.
4. **Performance Evaluation**: Each model is assessed using metrics such as R² Score and Mean Absolute Error (MAE).
5. **Hyperparameter Tuning**: Grid search is employed to fine-tune model parameters for improved accuracy.

## Analysis
Despite implementing various models and hyperparameter tuning, improvements in performance metrics were limited. The Random Forest model exhibited the best performance among the tested algorithms, achieving a satisfactory balance between complexity and accuracy. Visualizations from the EDA phase provided crucial insights into price distributions and feature relationships, highlighting areas for potential feature engineering or selection.

## Conclusion
This project successfully demonstrated the application of various regression techniques to predict laptop prices, with Random Forest emerging as the top-performing model. The interactive application developed using Streamlit provides users with an intuitive interface for making predictions based on user-defined inputs. This tool not only enhances user engagement but also facilitates informed purchasing decisions in the competitive laptop market.


