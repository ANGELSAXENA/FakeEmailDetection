import streamlit as st
import joblib

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="Fake Email Detection",
    page_icon="📧",
    layout="centered"
)

# ---------------- Load Model ----------------
model = joblib.load("models/naive_bayes_model.pkl")
vectorizer = joblib.load("models/count_vectorizer.pkl")

# ---------------- Sidebar ----------------
st.sidebar.title("📧 Fake Email Detection")

st.sidebar.markdown("### 📌 About")
st.sidebar.write(
    "This application uses a Machine Learning model to classify email or SMS messages as **Spam** or **Genuine (Ham)**."
)

st.sidebar.markdown("### 🤖 Model")
st.sidebar.write("**Algorithm:** Multinomial Naive Bayes")

st.sidebar.markdown("### 📊 Performance")
st.sidebar.write("**Accuracy:** 98.1%")

st.sidebar.markdown("### 🛠️ Technologies Used")
st.sidebar.write("""
- Python
- Streamlit
- Scikit-learn
- CountVectorizer
- Joblib
""")

st.sidebar.markdown("### 💡 Did You Know?")
st.sidebar.info(
    "Spam detection helps protect users from phishing attacks, scams, and unwanted emails."
)

st.sidebar.markdown("---")
st.sidebar.write("👨‍💻 **Developer:** Angel Saxena")

# ---------------- Main Page ----------------
st.title("📧 Fake Email Detection using Machine Learning")

st.info(
    "💡 Enter an email or SMS message below and click **Predict** to check whether it is Spam or Genuine."
)

st.write(
    """
This web application uses a trained **Machine Learning model** to detect whether a message is **Spam** or **Ham (Genuine)**.
"""
)

# ---------------- Example Messages ----------------
st.markdown("### 📝 Example Messages")

col1, col2 = st.columns(2)

with col1:
    st.code(
        "Congratulations! You have won a FREE iPhone. Click here to claim your reward."
    )

with col2:
    st.code(
        "Hi, I will reach home by 6 PM. Please keep the gate open."
    )

# ---------------- Input ----------------
message = st.text_area(
    "📩 Enter Email or SMS Message",
    height=180,
    placeholder="Type your message here..."
)

# ---------------- Prediction ----------------
if st.button("🔍 Predict"):

    if message.strip() == "":
        st.warning("⚠️ Please enter a message.")

    else:

        transformed = vectorizer.transform([message])

        prediction = model.predict(transformed)

        st.divider()
        st.subheader("📢 Prediction Result")

        if prediction[0] == "spam":
            st.error("🚨 This message is classified as **SPAM**.")
            st.write(
                "⚠️ Avoid clicking suspicious links or sharing personal information."
            )
        else:
            st.success("✅ This message is classified as **GENUINE (HAM)**.")
            st.write("👍 The message appears to be safe.")

# ---------------- Footer ----------------
st.markdown("---")
st.caption("👨‍💻 Developed by Angel Saxena")
st.caption("📧 Fake Email Detection using Machine Learning")
st.caption("🚀 Powered by Streamlit")