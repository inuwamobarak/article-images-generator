# Handles making predictions or inference with prompt template
from foundation import llm
# from constrain import language_translator
from external_requests import SegMindAPI


class Inference:

    @staticmethod
    async def generate_article(text: object) -> object:
        """

        :rtype: object
        """
        prompt = f"""Based on the users text, identify the language of communication:
                {text}
                """

        article_text = llm(
            prompt=prompt
        )
        return article_text

    @staticmethod
    async def language_translator(text: object, target_language: object) -> object:
        """
        Translates a given text to a target language.
        """
        prompt = f"""Please translate this text to the target language:
                    Text: {text}
                    Target: Language: {target_language}
                """

        output = llm(
            prompt=prompt,
            grammar=None  # language_translator
        )
        return output

    @staticmethod
    async def sentence_generator(number_of_sentence: object, text: object) -> object:
        """

        :param number_of_sentence:
        :param text:
        :return:
        """
        prompt = f"""Generate {number_of_sentence}'s with the the given word:
                    {text}
                """

        output = llm(
            prompt=prompt,
            grammar=None
        )
        return output

    def generate_image_with_prompt(self, api_key, prompt, steps, seed, aspect_ratio, base64):
        api_key = "SG_8273f7aa361a8a79"
        segmind_api = SegMindAPI(api_key)

        prompt = "A wallpaper image of sports car with 'Flux' written on it, motion blur, side view, long shot"
        steps = 4
        seed = 1184522
        aspect_ratio = "1:1"
        base64 = False

        response = segmind_api.generate_image(prompt, steps, seed, aspect_ratio, base64)
        return response

# response = Inference.generate_image()
# print(response)