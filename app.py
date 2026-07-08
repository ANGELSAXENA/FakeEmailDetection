import streamlit as st
import joblib

# Page settings
st.set_page_config(
    page_title="Fake Email Detection",
    page_icon="📧",
    layout="centered"
)

# Load model and vectorizer
model = joblib.load("models/naive_bayes_model.pkl")
vectorizer = joblib.load("models/count_vectorizer.pkl")

st.title("📧 Fake Email Detection")
st.write("This application predicts whether an email or SMS message is **Spam** or **Ham (Genuine)**.")

message = st.text_area(
    "Enter your message below:",
    height=180,
    placeholder="Example: Congratulations! You have won a ₹10,000 prize..."
)

if st.button("🔍 Predict"):

    if message.strip() == "":
        st.warning("⚠️ Please enter a message.")
    else:
        transformed = vectorizer.transform([message])
        prediction = model.predict(transformed)

        st.subheader("Prediction")

        if prediction[0] == "spam":
            st.error("🚨 This message is **SPAM**")
        else:
            st.success("✅ This message is **GENUINE (HAM)**")

st.markdown("---")
st.caption("Developed by Angel Saxena")