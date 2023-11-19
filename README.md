# Question-Answering.
# Arabot

Arabot is a FastAPI project for question-answering using the deepset/roberta-base-squad2 model.

## Installation

Use the following command to install the project:

```bash
poetry install

Usage
Running the API

Make sure to activate your virtual environment and then run the following command to start the FastAPI application:

bash

uvicorn your_module_name:app --reload

Replace your_module_name with the actual name of the Python module containing your FastAPI app instance.

The API will be available at http://127.0.0.1:8000.
Endpoints
Single Question Answering

    Endpoint: /answer
    Method: POST
    Request Payload:

    json

{
  "context": "The context of the question.",
  "question": "The question to be answered."
}

Response:

json

    {
      "answer": "The answer to the question."
    }

Batch Question Answering

    Endpoint: /batch-answer
    Method: POST
    Request Payload:

    json

    [
      {
        "context": "Context 1",
        "question": "Question 1"
      },
      {
        "context": "Context 2",
        "question": "Question 2"
      },
      ...
    ]

    Response: Downloadable CSV file containing original and generated answers.

License

This project is licensed under the MIT License - see the LICENSE file for details.

csharp


Feel free to copy and paste this into your README.md file on GitHub.
