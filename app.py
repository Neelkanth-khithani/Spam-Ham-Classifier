import streamlit as st
import joblib
import urllib.request

model_url = 'https://raw.githubusercontent.com/Neelkanth-khithani/Spam-Ham-Classifier/main/spam-ham'
model_filename = 'spam-ham'

urllib.request.urlretrieve(model_url, model_filename)

model = joblib.load(model_filename)

st.title('spam-ham classifier')
ip = st.text_input('Enter the message')
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
