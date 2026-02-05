from intent_detector import detect_intent
from knowledge_base import DATA

def lambda_handler(event, context=None):
    user_query = event.get("query", "")
    print("User Query:", user_query)

    intent = detect_intent(user_query)
    print("Detected Intent:", intent)

    domain_data = DATA.get(intent, {})

    for key in domain_data:
        if key in user_query.lower():
            return {"response": domain_data[key]}

    return {"response": "Please visit the nearest government office for verified information."}


if __name__ == "__main__":
    event = {"query": "pm kisan scheme"}
    result = lambda_handler(event)
    print("Final Output:", result)