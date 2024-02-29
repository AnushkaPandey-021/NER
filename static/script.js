document.addEventListener('DOMContentLoaded', function() {
    var generateButton = document.getElementById('generate_button');
    generateButton.addEventListener('click', function() {
        var inputText = document.getElementById('input_text').value;
        
        // Send the input text to the server for NER processing
        fetch('/process_text', {
            method: 'POST',
            body: JSON.stringify({ input_text: inputText }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            // Update the NER visualization section
            document.getElementById('ner_visualization').innerHTML = data.ner_visualization;
        })
        .catch(error => console.error('Error:', error));
    });
});
