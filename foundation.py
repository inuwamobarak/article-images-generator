# Handles loading base models

# high-level API
from llama_cpp import Llama
from utils import PROMPT, LLAMA2_MODEL


llm = Llama(
    model_path=LLAMA2_MODEL,
    n_gpu_layers=-1, # Uncomment to use GPU acceleration
    # seed=1337, # Uncomment to set a specific seed LLAMA_DEFAULT_SEED
    n_ctx=2048 # Uncomment to increase the context window
)


llm(
    prompt=PROMPT,  # "Q: Name the planets in the solar system? A: ",  # Prompt
    max_tokens=None,  # Generate up to n tokens, set to None to generate up to the end of the context window
    # stop=["Q:", "\n"],  # Stop generating just before the model would generate a new question
    echo=True  # Echo the prompt back in the output
)  # Generate a completion, can also call create_completion
