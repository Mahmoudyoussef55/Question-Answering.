from fastapi import FastAPI, HTTPException
from typing import Dict, List
from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering
from fastapi.responses import StreamingResponse
import datasets

# Creating an instance of the FastAPI class
app = FastAPI()

# Load the pre-trained model and tokenizer
model_name = "deepset/roberta-base-squad2"
qa_pipeline = pipeline("question-answering", model=model_name, tokenizer=model_name)

# Endpoint for answering a single question
@app.post("/answer")
def get_answer(data: Dict):
    # Extracting context and question from the request data
    context = data["context"]
    question = data["question"]
    
    # Using the question-answering pipeline to get the answer
    answer = qa_pipeline(question=question, context=context)
    
    # Returning the answer in JSON format
    return {"answer": answer["answer"]}

# Endpoint for batch question-answering
@app.post("/batch-answer")
def get_batch_answers(dataset: List[Dict]):
    # Initializing empty lists for answers and CSV data
    answers = []
    csv_data = "question,original_answer,generated_answer\n"
    
    # Iterating over each item in the dataset
    for item in dataset:
        # Extracting context, question, and original answer (if provided)
        context = item["context"]
        question = item["question"]
        original_answer = item.get("answer", "")
        
        # Using the question-answering pipeline to get the generated answer
        generated_answer = qa_pipeline(question=question, context=context)["answer"]
        
        # Appending the results to the answers list
        answers.append({
            "question": question,
            "original_answer": original_answer,
            "generated_answer": generated_answer,
        })
        
        # Adding the data to the CSV string
        csv_data += f"{question},{original_answer},{generated_answer}\n"
    
    # Setting up response headers for streaming CSV file
    response = StreamingResponse(iter([csv_data]), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=generated_answers.csv"
    
    # Returning the streaming response
    return response