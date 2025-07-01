import requests
import json

def build_structured_prompt(customer_query: str) -> str:
    return f"""
You are a helpful assistant designed to extract structured intent from customer queries.

Your task is to:
1. Identify the **intent** (like `get_invoice_data`, `get_travel_details`)
2. Extract key **entities** (e.g., invoice number, travel date)

Return only valid JSON in this format:
{{
  "intent": "<intent_name>",
  "entities": {{
    "key1": "value1"
  }}
}}

Now process this customer query:
"{customer_query}"
"""

def query_tachyon_llm_structured(customer_query: str) -> dict:
    prompt = build_structured_prompt(customer_query)

    url = "https://tachyon-studio..net/playground_document"
    headers = {
        "Content-Type": "application/json",
        "Origin": "https://tachyon-studio.c.net",
    }
    cookies = {
        "higgs_session": "YOUR_SESSION_COOKIE_HERE"
    }

    payload = {"prompt": prompt}

    try:
        response = requests.post(url, headers=headers, cookies=cookies, json=payload)
        response.raise_for_status()
        return json.loads(response.text)
    except Exception as e:
        print("Tachyon Error:", e)
        return {"intent": "unknown", "entities": {}}
