<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Groq AI Tutor Chatbot</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
            margin: 0;
        }

        .chat-container {
            width: 400px;
            background-color: white;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 5px;
            overflow: hidden;
        }

        .chat-box {
            height: 400px;
            padding: 20px;
            overflow-y: auto;
            border-bottom: 1px solid #ccc;
        }

        .input-box {
            display: flex;
        }

        #user-input {
            flex: 1;
            padding: 10px;
            border: none;
            border-top: 1px solid #ccc;
        }

        button {
            padding: 10px;
            border: none;
            background-color: #007bff;
            color: white;
            cursor: pointer;
            border-top: 1px solid #ccc;
        }

        button:hover {
            background-color: #0056b3;
        }

        .user-message {
            text-align: right;
            background-color: #e6f7ff;
            margin: 10px 0;
            padding: 10px;
            border-radius: 5px;
            max-width: 80%;
            margin-left: auto;
        }

        .bot-message {
            text-align: left;
            background-color: #fff5e6;
            margin: 10px 0;
            padding: 10px;
            border-radius: 5px;
            max-width: 80%;
        }
    </style>
</head>
<body>
    <div class="chat-container">
        <div class="chat-box" id="chat-box"></div>
        <div class="input-box">
            <input type="text" id="user-input" placeholder="Ask me about AI...">
            <button onclick="sendMessage()">Send</button>
        </div>
    </div>
    <script>
        function sendMessage() {
            const userInput = document.getElementById('user-input').value;
            if (userInput.trim() === '') return;

            // Display user message
            const chatBox = document.getElementById('chat-box');
            const userMessage = document.createElement('div');
            userMessage.className = 'user-message';
            userMessage.innerText = userInput;
            chatBox.appendChild(userMessage);

            // Send user message to the server
            fetch('/ask', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ question: userInput }),
            })
            .then(response => response.json())
            .then(data => {
                // Display bot response
                const botMessage = document.createElement('div');
                botMessage.className = 'bot-message';
                botMessage.innerText = data.answer;
                chatBox.appendChild(botMessage);

                // Scroll to the bottom
                chatBox.scrollTop = chatBox.scrollHeight;
            });

            // Clear input box
            document.getElementById('user-input').value = '';
        }
    </script>
</body>
</html>

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from groq import Groq

app = Flask(__name__)
CORS(app)  # Allow CORS for all domains

# Initialize the Groq client
client = Groq(api_key=os.environ.get("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"))

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question')

    # Create chat completion with Groq API
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "You are an AI tutor which has a degree from Stanford University. You have worked with top companies in the field of AI and now you are training new students to break into AI engineering. Your students are from every level from zero knowledge to professional software developers therefore it is your job to ensure the perfect and unique roadmap for every person based on their knowledge. The style of this education is based on Q&A meaning the user will ask you first a question, then you will answer."
            },
            {
                "role": "user",
                "content": question
            }
        ],
        model="llama3-8b-8192",
    )

    response = chat_completion.choices[0].message.content

    return jsonify({'answer': response})

if __name__ == '__main__':
    app.run(debug=True)
## I have done the project by getting help with Chat GPT and by prompt engineering
## Unfortunately I did not test my code if it will work or not because my computer does not support pip install, I have tried to install it but it did not worked, so agian I asked Chat GPT to help me if it is correct or not.