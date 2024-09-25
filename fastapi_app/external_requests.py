import requests


class SegMindAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://api.segmind.com/v1/fast-flux-schnell"

    def generate_image(self, prompt, steps, seed, aspect_ratio, base64=False):
        data = {
            "prompt": prompt,
            "steps": steps,
            "seed": seed,
            "aspect_ratio": aspect_ratio,
            "base64": base64
        }

        headers = {
            "x-api-key": self.api_key
        }

        response = requests.post(self.url, json=data, headers=headers)

        if response.status_code == 200:
            with open("image.png", "wb") as f:
                f.write(response.content)
            print("Image saved to image.png")
            return response
        else:
            print(f"Error: {response.text}")
            return None