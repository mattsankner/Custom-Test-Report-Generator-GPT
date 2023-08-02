from flask import request, Flask, jsonify, render_template
import openai
import os
import PyPDF2

#create a new flask web server
app = Flask(__name__, static_url_path='', static_folder='static')

# OpenAI API key providing
openai.api_key = 'YOUR_API_KEY_HERE'

#a route to the home page of the server, returning hello world
@app.route('/')
def home():
    return 'Go to the chat page at /chat_page!'

@app.route('/chat_page')
def chat_page():
    return render_template('index.html')

#serving the stylesheet for testing purposes
@app.route('/style.css')
def serve_stylesheet():
    return app.send_static_file('style.css')

#a route to the chat endpoint of the server, set to respond to HTTP POST requests
@app.route('/chat', methods=['POST'])
def chat():
    # extract the file from the request
    file = request.files['file']

    # save the file temporarily
    filename = "tempfile" + os.path.splitext(file.filename)[1]
    file.save(filename)

    # read the file using the appropriate library based on file type
    if file.filename.endswith('.docx'):
        doc = python_docx.Document(filename)
        text = " ".join([paragraph.text for paragraph in doc.paragraphs])
    elif file.filename.endswith('.pdf'):
        pdf_file_obj = open(filename, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
        text = " ".join([pdf_reader.pages[page_num].extract_text() for page_num in range(len(pdf_reader.pages))])
    else:
        text = ""

    # remove the temporary file
    os.remove(filename)

    # extract the message from the request
    message = request.form['message']

     # concatenate the extracted document text and the user's prompt
    total_input = text + " " + message

    # Make a request to the OpenAI API with the user's message as the prompt
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": "You are a detailed and structured assistant. You generate test documents for software engineers based on rules in pdf files given to you."},
            {"role": "user", "content": total_input},
        ]
    )

    #Extracting Response
    response_message = response['choices'][0]['message']['content']

    # Return the model's response as a JSON object
    return jsonify({"message": response_message.strip()})


# A python conditional that only runs the app if this file is being run directly

if __name__ == "__main__":
    app.run(debug=True)
