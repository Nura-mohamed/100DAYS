from flask import Flask, render_template, request, jsonify
from googletrans import Translator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']
    target_language = request.form['target_language']
    
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    
    return jsonify({'translated_text': translated.text})

if __name__ == '__main__':
    app.run()
