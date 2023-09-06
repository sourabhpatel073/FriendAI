# FriendAI
<h3>
  Incorporating a blend of Angular, Django, Python, PostgreSQL, HTML, and CSS, Friend AI has been designed to provide a dynamic and user-centric experience. Through the integration of OpenAI's GPT functions, this project offers powerful AI-driven features tailored to enhance user interactions and bring clarity to complex documents.
</h3>
Features
<ul>
    <li><strong>PDF Context Processing:</strong> Enables users to upload PDFs. Post upload, the system processes and establishes a context to enhance subsequent AI interactions.</li>
    <li><strong>AI-Powered Q&A:</strong> With the context set, users can raise queries pertaining to the uploaded PDF. The system leverages ChatGPT functions to deliver pinpoint answers.</li>

<li><strong>Customizable AI Interactions:</strong> 
    <ul>
        <li>Dynamic Tone Setting: Users can customize the conversational tone (friendly, professional, etc.) for AI.</li>
        <li>Language Preferences: Decide the language in which AI interactions take place.</li>
    </ul>
</li>

<li><strong>Dynamic Image Generation:</strong> Beyond text, Friend AI provides visual interactions. Users can generate images based on provided descriptions.</li>

<li><strong>User Account Management:</strong>
    <ul>
        <li>User Authentication: Features to register, login, and secure user data.</li>
        <li>Profile Management: Users can edit and update their profiles at will.</li>
    </ul>
</li>
Tech Stack
<ul>
    <li><strong>Backend:</strong> Django. (Mention your Django endpoints here)</li>
    <li><strong>Frontend:</strong> Angular integrated with HTML and CSS, ensuring a smooth and intuitive user interface.</li>
    <li><strong>Database:</strong> PostgreSQL, a robust solution for data storage and management.</li>
    <li><strong>AI Capabilities:</strong> Powered by OpenAI's GPT, with added support from Langchain for nuanced language processing.</li>
</ul>

Backend: Django
Endpoints:

<ul>
    <li><strong>Chat Operations:</strong>
        <ul>
            <li>`chat/`: Retrieve all chats</li>
            <li>`chat/create/`: Create a new chat</li>
            <li>`chat/<int:pk>/`: Retrieve a specific chat</li>
            <li>`chat/delete/<int:pk>/`: Delete a specific chat</li>
        </ul>
    </li>
    <li><strong>User Profile Operations:</strong>
        <ul>
            <li>`user_register/`: Register a new user</li>
            <li>`user_login/`: User login</li>
            <li>`user/edit/<int:user_id>/`: Edit a user profile</li>
            <li>`get_profile/<int:user_id>/`: Get a user's profile</li>
        </ul>
    </li>
    <li><strong>PDF Operations:</strong> `upload_pdfs/`: Upload PDFs</li>
    <li><strong>Q&A Operations:</strong>
        <ul>
            <li>`ask_question/`: Ask a question based on an uploaded PDF</li>
            <li>`ask/`: General ask endpoint</li>
        </ul>
    </li>
    <li><strong>Image Generation:</strong> `generate-image/`: Generate an image based on a description</li>
</ul>
Frontend: Angular
Integrated with HTML and CSS, ensuring a smooth and intuitive user interface.

Database: PostgreSQL
A robust solution for data storage and management.

AI Capabilities:
Powered by OpenAI's GPT, with added support from Langchain for nuanced language processing.
