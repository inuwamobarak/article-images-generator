# Handles loading base models

# high-level API
from llama_cpp import Llama
from.utils import PROMPT, LLAMA2_MODEL


class FoundationModel:
    def __init__(self, model_path=LLAMA2_MODEL, n_gpu_layers=-1, seed=1337, n_ctx=2048):
        self.model = Llama(
            model_path=model_path,
            n_gpu_layers=n_gpu_layers,
            seed=seed,
            n_ctx=n_ctx
        )

    def generate_completion(self, prompt=PROMPT, max_tokens=2048, stop=None, echo=True):
        if stop is None:
            stop = ["Q:", "\n"]
        return self.model(
            prompt=prompt,
            max_tokens=max_tokens,
            stop=stop,
            echo=echo
        )

    def create_completion(self, **kwargs):
        return self.model.create_completion(**kwargs)