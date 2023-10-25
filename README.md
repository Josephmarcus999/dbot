# dbot
An LLM-powered chatbot with the added context of the dbt knowledge base.

## An experiment
This is currently a basic CLI prototype that has been supplied with the knowledge of the dbt Developer Hub (docs, guides, etc) and uses this to add context to questions asked by users.

## How does it work?
It stores embeddings of the material on the Developer Hub (chunked by markdown heading sections) in a vector database, and finds documents similar to the question that is asked. It then prepends as much of that context onto the prompt as it can fit in ChatGPT's context window.

### To run:

1. run `uvicorn app:api --reload --host 0.0.0.0 --port 8000` from dbot directory
2. run  curl -X POST "http://localhost:8000/ask" -H "accept: application/json" -H "Content-Type: application/json" -d '{"question":"What is dbt?"}' 
