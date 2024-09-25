from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from PIL import Image
import base64

from article_processor import TextSummarizer
from external_requests import SegMindAPI
from pydantic import BaseModel
from transformers import BlipProcessor, BlipForConditionalGeneration

app = FastAPI()
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


class ImageRequest(BaseModel):
    # text: str = None
    url: str = None
    num_sentences: int
    steps: int
    seed: int
    aspect_ratio: str



@app.post("/generate_image")
async def generate_image(image_request: ImageRequest):
    try:
        api_key = "SG_8273f7aa361a8a79"
        api = SegMindAPI(api_key)
        summarizer = TextSummarizer(image_request.url, image_request.num_sentences)
        summary = summarizer.summarize()
        response = api.generate_image(summary, image_request.steps, image_request.seed, image_request.aspect_ratio, False)
        if response is not None:
            return FileResponse("image.png", media_type="image/png")
        else:
            raise HTTPException(status_code=500, detail="Error generating image")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generate_image_caption")
async def generate_image(image_request: ImageRequest):
    try:
        api_key = "SG_8273f7aa361a8a79"
        api = SegMindAPI(api_key)
        summarizer = TextSummarizer(image_request.url, image_request.num_sentences)
        summary = summarizer.summarize()
        response = api.generate_image(summary, image_request.steps, image_request.seed, image_request.aspect_ratio,
                                      False)
        if response is not None:
            image = Image.open("image.png")
            inputs = processor(image, text="a cover photo of", return_tensors="pt")
            out = model.generate(**inputs)
            caption = processor.decode(out[0], skip_special_tokens=True)
            with open("image.png", "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
            return {"image": encoded_image, "caption": caption}
        else:
            raise HTTPException(status_code=500, detail="Error generating image")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))