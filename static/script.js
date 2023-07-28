document.getElementById('chat-form').addEventListener('submit', function(e) {
    e.preventDefault();

    var form = document.getElementById('chat-form');
    var fileInput = document.getElementById('file-input');
    var messageInput = document.getElementById('message-input').value;
    var chatbox = document.getElementById('chatbox');

    var formData = new FormData();
    formData.append('file', fileInput.files[0]);
    formData.append('message', messageInput);

    fetch('/chat', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {   
        // Display user's message
        var userMessageDiv = document.createElement('div');
        userMessageDiv.textContent = 'You: ' + messageInput;
        chatbox.appendChild(userMessageDiv);

        // Display bot's reply as a document
        var botReply = data.message;

        // Clear the chatbox
        chatbox.innerHTML = '';

        // Format bot's reply into a document
        formatDocument(botReply, chatbox);

        // Scroll to the bottom of the chatbox
        chatbox.scrollTop = chatbox.scrollHeight;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

// Function to format the bot's reply as a document
function formatDocument(reply, container) {
    var sections = reply.split('\n\n'); // Split reply into sections

    sections.forEach(section => {
        var lines = section.split('\n');
        var sectionDiv = document.createElement('div');

        lines.forEach(line => {
            if (line.startsWith('# ')) {
                // Heading
                var heading = document.createElement('h2');
                heading.textContent = line.substring(2); // Remove the '# ' prefix
                sectionDiv.appendChild(heading);
            } else if (line.startsWith('* ')) {
                // Bullet point
                var bullet = document.createElement('li');
                bullet.textContent = line.substring(2); // Remove the '* ' prefix

                var list = document.createElement('ul');
                list.appendChild(bullet);

                sectionDiv.appendChild(list);
            } else {
                // Paragraph
                var paragraph = document.createElement('p');
                paragraph.textContent = line;
                sectionDiv.appendChild(paragraph);
            }
        });

        container.appendChild(sectionDiv);
    });
}
