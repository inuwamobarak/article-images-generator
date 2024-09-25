
## Setup

1. **Install Dependencies:**
`pip install -r requirements.txt`
2. **Run the FastAPI Server:**
`uvicorn api_endpoints:app --host 0.0.0.0 --port 8000`

## Usage
1. **You can make a POST request to the `/generate_image` endpoint with a JSON body containing the URL, number of sentences, steps, seed, and aspect ratio.**
2. **The endpoint will return a JSON response with the generated image data.**
3. **Find the endpoint here: http://127.0.0.1:8000/docs**
4. **Test Payload: {"url": "https://en.wikipedia.org/wiki/History_of_Poland_(1945%E2%80%931989)", "num_sentences": 5, "steps": 4, "seed": 1184522, "aspect_ratio": "1:1"}**

'''
your_project/
├── fastapi_app/
│   ├── app.py
│   ├── requirements.txt
│   ├── article_processor.py
│   ├── external_requests.py
│   └── ... (other FastAPI files)
├── streamlit_app/
│   ├── streamlit_app.py
│   ├── requirements.txt
│   └── ... (other Streamlit files)
├── nginx/
│   └── nginx.conf
├── docker-compose.yml
└── README.md
'''
