# Health Tracker

## 💡 Inspiration
Our inspiration was to create an all-in-one health platform where people can ask for the blood of a particular blood group when needed, can self-diagnose some common diseases, read health blogs and also create/join chat rooms and interact with other random people online aiming at improving their mental health.

## 💻 What it does
- Users can check if they are infected with any kind of heart disease, diabetes,  thyroid or not. 
- They can also check blood donation.
- Get notified when blood is available.
- get reports of the disease prediction.
- Chatroom, for sharing your thoughts with the world

## ⚙️How we built it

- ML: Python, Skikit-Learn
- Frontend: HTML, CSS, JS
- Backend: Django
- Database: CockroachDB
- Authentication: Auth0
- Sending an email once the blood is available and sending the reports of disease prediction: Twilio API

## Use of CockroachDB

- We have used CockroachDB as a primary database because it is an easy-to-use, open-source and indestructible SQL database.

## 🔑 Auth0

- We have used Auth0 for secure user authentication

## Twilio

- People can request blood from their nearest hospital and they will get a message on their registered email-id once blood is available which is implemented using Twilio.

## 🧠 Challenges we ran into

- Inputting so much of the data for self-diagnosis and also making this process engaging and interesting was a big challenge for us that we were able to overcome.

## 🏅 Accomplishments that we're proud of

## 📖 What we learned

We learned how to integrate ML models directly without creating an API with Django and collaboration.

## 🚀 What's next for Health Tracker

Improving the accuracy of the model.