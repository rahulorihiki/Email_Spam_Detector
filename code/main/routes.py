from flask import render_template,request,url_for
from main import app
from flask import render_template
import nltk 
import pandas as pd
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
from io import BytesIO
import requests
import os
from dotenv import load_dotenv

load_dotenv() # take environment variables from .env.

nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')
pr_stem = nltk.PorterStemmer()

def clean_text(text):
    text = "".join([word.lower() for word in text if word not in string.punctuation])
    tokens = re.split('\W' , text)
    text = [pr_stem.stem(word) for word in tokens if word not in stopwords]
    return text



email_data = pd.read_csv("SMSSpamCollection.tsv" , sep="\t" , header=None)
email_data.columns = ["output" , "email_message"]
tfid_vect = TfidfVectorizer(analyzer=clean_text)
x_tfid = tfid_vect.fit_transform(email_data["email_message"])

mfile2 = "../spam-model-final.joblib"
rfc = joblib.load(mfile2)

def spam_or_not(text):
    inputsm = [text]
    data = tfid_vect.transform(inputsm)
    predictions = rfc.predict(data)
    return predictions[0]

@app.route("/" , methods = ['GET' , 'POST'])
def home():
    result = "xxx"
    if request.method == 'POST':
        data = request.form["email_data"]
        result = spam_or_not(data)
        return render_template("index.html" , result = result)
    return render_template("index.html" , result = result)
    

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/get-mode")
def get_mode():
    return os.environ.get("MODE")

