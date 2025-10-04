import requests
import os
import logging

async def analyze_code(code_snippet, model="deepseek-coder:6.7b"):
    url = "http://localhost:11434/api/generate"

    prompt = ""
    prompt_path = os.path.join(os.path.dirname(__file__), "..", "prompts", "prompt.txt")
    with open(prompt_path, "r", encoding="utf-8") as f:
        prompt = f.read()
    prompt += f"\n\n{code_snippet}"
    
    logging.info(f"Готовый промпт: {prompt}")

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=payload)
    return response.json()["response"]
