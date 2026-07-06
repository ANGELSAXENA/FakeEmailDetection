# Fake Email Detection using Naive Bayes

## Project Overview

This project uses the Naive Bayes algorithm to classify SMS messages as **Spam** or **Ham (Not Spam)**. The text messages are converted into numerical features using **CountVectorizer**, and a **Multinomial Naive Bayes** model is trained to perform the classification.

## Dataset

* Dataset: SMS Spam Collection
* Source: Kaggle
* Number of Features: 1 (Message)
* Target Variable: Label (Spam / Ham)

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* CountVectorizer
* Multinomial Naive Bayes
* Joblib
* Jupyter Notebook

## Project Workflow

1. Import Libraries
2. Load Dataset
3. Explore Dataset
4. Data Preprocessing
5. Separate Features and Target
6. Train-Test Split
7. Convert Text into Numerical Features using CountVectorizer
8. Train Multinomial Naive Bayes Model
9. Make Predictions
10. Evaluate Model
11. Save Model and CountVectorizer

## Model Evaluation

The model is evaluated using:

* Accuracy Score
* Confusion Matrix
* Classification Report (Precision, Recall and F1-Score)

## Project Structure

```text
FakeEmailDetection/
│
├── data/
│   └── SMSSpamCollection
│
├── notebooks/
│   └── fake_email_detection.ipynb
│
├── models/
│   ├── naive_bayes_model.pkl
│   └── count_vectorizer.pkl
│
├── images/
├── README.md
├── requirements.txt
└── .gitignore
```

## Author

**Angel Saxena**

GitHub: https://github.com/ANGELSAXENA
