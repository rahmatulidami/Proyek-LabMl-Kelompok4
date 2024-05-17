from flask import Flask, render_template, request
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

app = Flask(__name__, template_folder='templates')

# Load the model
model = tf.keras.models.load_model('text_classification.h5')

# Load the tokenizer and label encoder
with open('tokenizer.pkl', 'rb') as file:
    tokenizer = pickle.load(file)

with open('label_encoder.pkl', 'rb') as file:
    label_encoder = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    comment = request.form['comment']
    sequence = tokenizer.texts_to_sequences([comment])
    X = pad_sequences(sequence, maxlen=100)
    prediction = model.predict(X)
    predicted_label = label_encoder.inverse_transform([tf.argmax(prediction, axis=1).numpy()[0]])[0]
    return render_template('index.html', comment_display=comment, prediction_text='Predicted Emotion: {}'.format(predicted_label), comment="")

if __name__ == '__main__':
    app.run(debug=True)