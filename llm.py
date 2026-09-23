import ollama

from config import MODEL
from retriever import retrieve_context
from prompts import (
    SYSTEM_PROMPT, 
    build_prompt, 
    build_few_shot_prompt,
    build_context_prompt
)



def analyze_customer_message(customer_message: str, prompt_mode: str):

    if prompt_mode == "few_shot":
        base_prompt = build_few_shot_prompt(customer_message)

    else:
        base_prompt = build_prompt(customer_message)

    context = retrieve_context(customer_message)

    user_prompt = build_context_prompt(
        base_prompt,
        context,
    )

    response = ollama.chat(
        model = MODEL,
        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": user_prompt
            },
        ],
    )

    return response.message.content