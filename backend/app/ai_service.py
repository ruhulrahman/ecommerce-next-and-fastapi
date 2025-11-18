import os
import httpx
from dotenv import load_dotenv
import random

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

async def recommend_for_user(user_id: int):
    # Option A: call OpenAI for semantic-based recommendations (example)
    if OPENAI_API_KEY:
        prompt = f"Given a user id {user_id}, suggest 5 product categories the user might like. Format: comma separated categories."
        async with httpx.AsyncClient(timeout=30.0) as client:
            # example using OpenAI ChatCompletions (this is illustrative; adapt to the sdk you use)
            response = await client.post(
                "https://api.openai.com/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {OPENAI_API_KEY}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": "gpt-4o-mini",  # example; pick the model you have access to
                    "messages":[{"role":"user","content":prompt}],
                    "max_tokens":120
                },
            )
            data = response.json()
            # parse the text (very simple)
            text = data["choices"][0]["message"]["content"]
            categories = [c.strip() for c in text.split(",")][:5]
            return categories
    # Option B: fallback toy recommender (local)
    products = ["T-Shirt", "Sneakers", "Headphones", "Backpack", "Watch", "Sunglasses"]
    return random.sample(products, 3)
