# FriendAI
<h3>
  Incorporating a blend of Angular, Django, Python, PostgreSQL, HTML, and CSS, Friend AI has been designed to provide a dynamic and user-centric experience. Through the integration of OpenAI's GPT functions,Prompts and Langchain this project offers powerful AI-driven features tailored to enhance user interactions a nd bring clarity to complex documents.
  
![Screenshot 2023-09-06 225326](https://github.com/sourabhpatel073/FriendAI/assets/112695694/09ea7365-8229-43d3-a82d-ba00f2718151)

</h3>
Features

![Screenshot 2023-09-06 225926](https://github.com/sourabhpatel073/FriendAI/assets/112695694/e947a720-a840-452c-bb60-2db12bb820a2)

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
    <li><strong>Backend:</strong> Django. </li>
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

  ![Screenshot 2023-09-07 004446](https://github.com/sourabhpatel073/FriendAI/assets/112695694/9c996f32-913b-467c-8a28-fe30d7463505)

Database: PostgreSQL
A robust solution for data storage and management.
![Screenshot 2023-09-06 225849](https://github.com/sourabhpatel073/FriendAI/assets/112695694/afe64639-99c5-48ee-a575-bd01d323fc66)

AI Capabilities:
Powered by OpenAI's GPT, with added support from Langchain for nuanced language processing.
![Screenshot 2023-09-06 225959](https://github.com/sourabhpatel073/FriendAI/assets/112695694/2d0441e1-2db3-48ae-ae11-ac8e770a6e97)
