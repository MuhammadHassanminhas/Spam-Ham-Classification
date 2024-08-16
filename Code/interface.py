import sys
sys.path.append("C:\\Users\\muham\\OneDrive\\Desktop\\Spam FIlter")
import streamlit as st
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
import pickle
tfidf = pickle.load(open('vectorizer.pkl' , 'rb'))
model = pickle.load(open('model.pkl' , 'rb'))

def processing(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        y.append(stemmer.stem(i))
    return ' '.join(y)

text = input('Enter your text : ')

transformed_text = processing(text)
# print(model(transformed_text))
vector_input = tfidf.transform([transformed_text])
result = model.predict(vector_input)[0]
if result==1:
    print('spam')
elif result==0:
    print('not spam')
