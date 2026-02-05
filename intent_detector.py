def detect_intent(text):
    text = text.lower()

    if any(word in text for word in ["scheme", "yojana", "kisan"]):
        return "government"
    if any(word in text for word in ["health", "hospital", "doctor"]):
        return "healthcare"
    if any(word in text for word in ["crop", "rice", "agriculture"]):
        return "agriculture"

    return "general"