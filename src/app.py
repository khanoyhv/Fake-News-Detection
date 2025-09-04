# src/app.py

import streamlit as st
import joblib
import numpy as np
import os

# --- Caching the model ---
# This is a key performance optimization for Streamlit.
# It ensures that our model is loaded only ONCE when the app starts,
# not on every user interaction.
@st.cache_resource
def load_model():
    """Loads the saved pipeline object."""
    model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'final_news_pipeline.joblib')
    pipeline = joblib.load(model_path)
    return pipeline

# --- UI Configuration ---
st.set_page_config(
    page_title="Fake News Detector",
    page_icon="📰",
    layout="wide"
)

# Load the pipeline
pipeline = load_model()

# --- App Layout ---
st.title("📰 Fake News Detector")
st.markdown(
    """
    Enter the text of a news article below to classify it as **Real** or **Fake**.
    This model was trained on a dataset of over 44,000 articles.
    """
)

# User input text area
user_text = st.text_area("Enter News Article Text:", height=250, placeholder="Paste your news article here...")

# Classify button
if st.button("Classify News", type="primary"):
    if user_text:
        # The pipeline expects a list or iterable of texts
        prediction = pipeline.predict([user_text])[0]
        prediction_proba = pipeline.predict_proba([user_text])[0]

        # Display the result
        st.subheader("Classification Result:")
        if prediction == 1:
            st.error("Prediction: This looks like FAKE News.", icon="🚨")
        else:
            st.success("Prediction: This looks like REAL News.", icon="✅")

        # Display confidence score
        confidence = np.max(prediction_proba) * 100
        st.metric(label="Model Confidence", value=f"{confidence:.2f}%")

        # Optional: Show detailed probabilities
        st.write("Confidence Scores:")
        st.write(f"- **Real News:** {prediction_proba[0]*100:.2f}%")
        st.write(f"- **Fake News:** {prediction_proba[1]*100:.2f}%")
    else:
        st.warning("Please enter some text to classify.", icon="⚠️")