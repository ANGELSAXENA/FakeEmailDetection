# 📧 Fake Email Detection using Machine Learning

A Machine Learning web application that predicts whether an email or SMS message is **Spam** or **Genuine (Ham)**.

## 🚀 Live Demo

👉 https://fake-email-detection-angel.streamlit.app/

---

## 📌 Features

- Detects Spam and Genuine messages
- Machine Learning based prediction
- User-friendly Streamlit interface
- Fast and accurate prediction
- Live web deployment

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- CountVectorizer
- Joblib
- Git & GitHub

---

## 🤖 Machine Learning Model

- **Algorithm:** Multinomial Naive Bayes
- **Vectorizer:** CountVectorizer
- **Accuracy:** 98.1%

---

## 📂 Project Structure

```
FakeEmailDetection/
│
├── models/
│   ├── naive_bayes_model.pkl
│   └── count_vectorizer.pkl
│
├── notebook.ipynb
├── app.py
├── requirements.txt
├── README.md
```

---

## ▶️ How to Run Locally

Clone the repository:

```bash
git clone <your-github-repository-link>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📸 Sample Messages

### Spam

```
Congratulations! You have won a FREE iPhone.
Click here to claim your reward.
```

### Genuine

```
Hi, I will reach home by 6 PM.
Please keep the gate open.
```

---

## 👨‍💻 Developer

**Angel Saxena**

---

⭐ If you like this project, don't forget to star the repository.