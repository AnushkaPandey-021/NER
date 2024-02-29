from flask import Flask, render_template, request, jsonify
import spacy
from spacy import displacy

app = Flask(__name__)
nlp = spacy.load('en_core_web_sm')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_text', methods=['POST'])
def process_text():
    input_text = request.json['input_text']
    
    # Perform NER processing
    doc = nlp(input_text)
    ner_tags = [(ent.text, ent.label_) for ent in doc.ents]

    # Customize colors for different entity types
    colors = {'PERSON': '#ff6347', 'ORG': '#4682b4', 'GPE': '#32cd32'}
    
    # Render the visualization with custom colors
    html = displacy.render(doc, style='ent', options={'colors': colors})

    return jsonify({'ner_tags': ner_tags, 'ner_visualization': html})

if __name__ == '__main__':
    app.run(debug=True)
