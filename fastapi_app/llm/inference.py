# Handles making predictions or inference with prompt template
import asyncio

from.foundation import FoundationModel

basemodel = FoundationModel()


class LlmInference:

    @staticmethod
    def generate_article(text: object) -> object:
        """

        :rtype: object
        """
        text="What is life?"

        prompt = f"""You are an expert article generator. Based on the text below, generate a detailed aticle that is \
            well structured and covers the topic efficiently: \
            Some description: {text}
        """

        article_text = basemodel.generate_completion(
            prompt=prompt
        )
        return article_text


# inference = LlmInference()
# article = inference.generate_article(text="What is life?")
# print(article)


