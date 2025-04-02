# Iris Prediction with Streamlit

This project demonstrates how to predict the species of Iris flowers using machine learning and deploy the model as an interactive web application using Streamlit.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [License](#license)

## Overview

The Iris dataset is a classic dataset in machine learning, consisting of 150 samples of Iris flowers, each with four features: sepal length, sepal width, petal length, and petal width. The goal is to predict the species of the Iris flower based on these features. This project involves building a machine learning model to perform this classification task and deploying it using Streamlit to create an interactive web application.

## Project Structure

The repository contains the following files:

- `flower_pred.py`: The main Python script that loads the Iris dataset, trains a machine learning model, and sets up the Streamlit web application.
- `requirements.txt`: A text file listing the Python packages required to run the project.

## Setup Instructions

To set up and run the project locally, follow these steps:

1. **Clone the Repository**: Use the following command to clone the repository to your local machine:

   ```bash
   git clone https://github.com/dattatejaofficial/Iris-Prediction-with-Streamlit.git
   ```

2. **Navigate to the Project Directory**: Move into the project directory:

   ```bash
   cd Iris-Prediction-with-Streamlit
   ```

3. **Create a Virtual Environment** (optional but recommended): Set up a virtual environment to manage project dependencies:

   ```bash
   python3 -m venv env
   ```

   Activate the virtual environment:

   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. **Install Dependencies**: Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the Streamlit web application:

1. **Ensure the Virtual Environment is Activated**: Make sure your virtual environment is active (refer to the setup instructions above).

2. **Run the Streamlit App**: Execute the following command:

   ```bash
   streamlit run flower_pred.py
   ```

3. **Access the Web Application**: After running the command, Streamlit will provide a local URL (typically `http://localhost:8501`) in the terminal. Open this URL in your web browser to interact with the Iris prediction application.

## Dependencies

The project requires the following Python packages:

- `streamlit`
- `pandas`
- `scikit-learn`
- `numpy`
- `matplotlib`

These dependencies are listed in the `requirements.txt` file. To install them, run:


```bash
pip install -r requirements.txt
```
