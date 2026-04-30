import json

def extract_items(text):
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
    Extract construction materials and quantities from this text:

    {text}

    Return ONLY valid JSON:
    {{
      "items": [
        {{"name": "", "quantity": number}}
      ]
    }}
    """

    data = {
        "model": "gpt-4.1-mini",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    try:
        content = result["choices"][0]["message"]["content"]

        # 🔥 CLEAN AI RESPONSE
        content = content.replace("```json", "").replace("```", "").strip()

        # 🔥 CONVERT STRING → REAL JSON
        parsed = json.loads(content)

        return parsed

    except Exception as e:
        return {
            "error": str(e),
            "raw": result
        }