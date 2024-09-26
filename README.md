# Article Image Generation API

This crash project fetches an article e.g Wikipedia article, processes the article text to extract a summary, and then generates an image based on the summary using the **SegMindAPI** [Segmind SD model](https://www.segmind.com/models/sdxl1.0-txt2img) The application consists of three main components:

1. **ArticleProcessor**: Handles fetching, parsing, and summarizing the article.
2. **SegMindAPI**: Generates an image based on the article summary via the SegMind image generation API.
3. **BlipProcessor**: Transformer model for adding captions to the generated images.
## Features

   - Fetch the Wikipedia article from the provided URL.
   - Extract and preprocess the article text.
   - Generate a summary of the article based on word frequency.
   - Generate an image from the summary using the **SegMindAPI**.
   - Add image caption to the generated image

---
### Similar products:
[Socialbu](https://socialbu.com/tools/generate-blog-image)

[Junia](https://www.junia.ai/tools/blog-images)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/article-image-gen.git
   cd article-image-gen
   ```

2. **Install Required Python Packages:**

   You can install the necessary packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. **Download NLTK Resources:**

   The NLTK library requires some additional data, which you can download using the following commands:

   ```python
   import nltk
   nltk.download('stopwords')
   nltk.download('wordnet')
   nltk.download('punkt')
   nltk.download('averaged_perceptron_tagger')
   ```
---

## Usage

**Set Up API Key:**

   You'll need to provide your **SegMind API** key to generate images. Set your API key when instantiating the `SegMindAPI` class:

   ```python
   api_key = "your_api_key_here"
   segmind_api = SegMindAPI(api_key)
   ```

## Example

For example, running the script on the article [History of Poland (1945-1989)](https://en.wikipedia.org/wiki/History_of_Poland_(1945%E2%80%931989)) will produce a summary and save an image based on that summary.

---

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


## Future Enhancements

- Add support for more advanced summarization techniques to proper prompt.
- Add support for generating article from scratch based on keywords.
- Improve error handling and logging.
- Expand image generation features to allow more customization of the generated images.
