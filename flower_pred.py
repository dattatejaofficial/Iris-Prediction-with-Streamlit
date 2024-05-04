import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""

<h1> Simple Iris Flower Prediction App. </h1>

This app predicts the <b>Iris Flower</b> type! 

""",unsafe_allow_html=True)

st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider(label='Sepal Length',min_value=4.3,max_value=7.9,value=5.4)

    sepal_width = st.sidebar.slider(label='Sepal Width',min_value=2.0,max_value=4.4,value=3.4)

    petal_length = st.sidebar.slider(label='Petal Length',min_value=1.0,max_value=6.9,value=1.3)

    petal_width = st.sidebar.slider(label='Petal Width',min_value=0.1,max_value=2.5,value=0.2)

    data = {
        'sepal_length':sepal_length,
        'sepal_width':sepal_width,
        'petal_length':petal_length,
        'petal_width':petal_width
    }

    features = pd.DataFrame(data,index=[0])

    return features

df=user_input_features()

st.subheader('User input parameters')
st.write(df)

iris = datasets.load_iris()
X=iris.data
y=iris.target

clf = RandomForestClassifier(random_state=6)
clf.fit(X,y)

pred = clf.predict(df)
pred_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index numbers')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[pred])

st.subheader('Prediction Probability')
st.write(pred_proba)