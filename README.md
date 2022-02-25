# django-graphene-tutorial


Start virtual environment:

`source env/bin/activate`

Run server:

`python manage.py runserver`

Navigate to admin: http://localhost:8000/admin/ <br>
And to Graphiql: [graphiql](http://localhost:8000/graphql#query=query%20%7B%0A%20%20allQuestions%20%7B%0A%20%20%20%20title%0A%20%20%7D%0A%20%20anAnswer(id%3A7)%7B%0A%20%20%20%20answerText%0A%20%20%7D%0A%20%20allAnswersToQuestionX(questionId%3A4)%7B%0A%20%20%20%20answerText%0A%20%20%7D%0A%7D%0A)

