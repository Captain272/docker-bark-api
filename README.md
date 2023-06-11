# Bark FastAPI Docker Container

This guide will walk you through the process of creating a Docker container for the Bark repository and using FastAPI to create an API endpoint.

## Prerequisites

- Docker
- Python 3.9 or higher
- Git

## Steps

1. **Clone the Bark repository:**
git clone https://github.com/suno-ai/bark.git
 


2. **Create a new directory for your FastAPI application and navigate to it:**
mkdir bark_fastapi
cd bark_fastapi
 


3. **Create a virtual environment and activate it:**
python3 -m venv venv
source venv/bin/activate
 


4. **Install FastAPI and other required packages:**
pip install fastapi uvicorn bark
 


5. **Create a new file called `main.py` and add the following code:**

```python
   from fastapi import FastAPI
   from pydantic import BaseModel
   from bark import Bark

   app = FastAPI()
   bark = Bark()

   class Prompt(BaseModel):
       text: str

   @app.post("/generate")
   async def generate(prompt: Prompt):
       response = bark.generate(prompt.text)
       return {"response": response}```


6. Test your FastAPI application by running:
 

   uvicorn main:app --reload
Create a Dockerfile in the bark_fastapi directory with the following content:
 

   FROM python:3.9

   WORKDIR /app

     requirements.txt requirements.txt
   RUN pip install -r requirements.txt

 

   CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

Create a requirements.txt file in the bark_fastapi directory with the following content:
 

   fastapi
   uvicorn
   bark
Build the Docker image:
 

   docker build -t bark_fastapi .
Run the Docker container:
 

    docker run -p 8000:8000 bark_fastapi
Now, you have a fully-functional Docker API that receives a prompt as a request, passes it on to the Bark repository for processing, and returns the result as a response. The API is accessible at http://localhost:8000/generate.
