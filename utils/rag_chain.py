from google import genai
from config import GOOGLE_API_KEY

client = genai.Client(api_key=GOOGLE_API_KEY)

def generate_answer(query, context, chat_history):

    # ✅ Limit history (avoid confusion)
    chat_history = chat_history[-6:]

    history_text = ""
    for role, msg in chat_history:
        history_text += f"{role}: {msg}\n"

    prompt = f"""
You are a retail domain assistant.

STRICT RULES:
- Answer ONLY from the provided context
- If answer not found, say "Not available in document"
- Give precise answers (especially numbers like days, price, policy)

Previous Conversation:
{history_text}

Context:
{context}

Question:
{query}

Answer:
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "temperature": 0.2  # ✅ more precise answers
        }
    )

    return response.text
