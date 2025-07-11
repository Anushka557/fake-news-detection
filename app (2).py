import streamlit as st
import pickle


model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title(" Fake News Detector")

user_input = st.text_area("Enter the news text below:")

if st.button("Detect"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        vector = vectorizer.transform([user_input])
        result = model.predict(vector)[0]
        if result == 1:
            st.success(" This appears to be **Real News**.")
        else:
            st.error("This appears to be **Fake News**.")
