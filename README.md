# Custom-Test-Report-Generator-GPT

## Description

Generates accurate and custom-structured unit test documentation based on uploaded user info. User inputs desired test documentation structure through a pdf/docx, uploads test case data, and a description of the test through natural language. Created during a software developer internship at Insulet Corporation for use case of creating test case documentation for software.

## Technologies

- Flask (Backend)
- HTML, CSS (Frontend Styling)
- JavaScript (Client-Side Logic)
- GPT 3.5 (AI Model Integration)
- PyPDF2, python-docx (File Handling)

![Screenshot of my app](/AppScreenshot.png)

## Features

- Document Uploading: Users can upload a document in PDF or DOCX format.
- Interactive Chat: Users can chat with the AI model and receive structured replies.
- Themed Design: A simple and elegant design, with styled chat bubbles.

## Setup & Usage

### Requirements

Make sure you have Flask and the other dependencies installed, as outlined in the `requirements.txt` file.

### PDF Download

Download TestDocTemplate.pdf from the repo or any other template you wish to format your created document with in a pdf format. Save it to a location you will remember later for use.

### Running the Application

1. Clone the repository:

    git clone https://github.com/your-username/OpenAI-Flask-Document-Generator.git

2. Navigate to the project directory:

    cd OpenAI-Flask-Document-Generator

3. Install the required dependencies:

    pip install -r requirements.txt

4. Type your OpenAI key in app.py:

    https://platform.openai.com/account/api-keys

6. Run the Flask application:

    python app.py

7. Open your browser and navigate to `http://localhost:5000/chat_page` to access the chat interface.

## Contributing

Feel free to fork the project and submit pull requests for any enhancements, bug fixes, or other contributions.

## License

This project is licensed under the MIT License. See the `LICENSE.md` file for details.



