# Question-Answering.
# Arabot

Arabot is a FastAPI project for question-answering using the deepset/roberta-base-squad2 model.

### Usage
* Clone the repository:
   bash ``` git clone https://github.com/your-mahmoudyoussef55/Question-Answering.git ```

* Create a virtual environment:
bash ``` conda activate -n project python ```
* Install requirments.
bash ``` poetry install ```

Running the API
Make sure to activate your virtual environment and then run the following command to start the FastAPI application:

bash ``` uvicorn your_module_name:app --reload ```

Replace your_module_name with the actual name of the Python module containing your FastAPI app instance.

* The API will be available at http://127.0.0.1:8000.
* Endpoints

## Testing with Postman:
1-Open Postman and create a new request.
2-Set the request type to POST.
3-Enter the URL: http://127.0.0.1:8000/answer for single question answering or http://127.0.0.1:8000/batch-answer for batch question answering.
4-Set the request body to JSON format:

#### <font color="red"> Single Question Answering

* Endpoint: /answer
* Method: POST
* Request Payload:

json ```
   {
  "context": "The context of the question.",
  "question": "The question to be answered."
} ```

##### Response:

 json
 {
      "answer": "The answer to the question."
}   



#### <font color="red"> Batch Question Answering

* Endpoint: /batch-answer
* Method: POST
* Request Payload:

    json
   ``` 
      [{
        "context": "Context 1",
        "question": "Question 1"
      },
      {
        "context": "Context 2",
        "question": "Question 2"
      },
      ... ]```


* Response: Downloadable CSV file containing original and generated answers.

## License

- This project is licensed under the MIT License - see the LICENSE file for details.


Feel free to copy and paste this into your README.md file on GitHub.
