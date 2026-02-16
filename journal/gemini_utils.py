import google.genai as genai
from django.conf import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)
for m in client.models.list():
    print(m.name)
model = "gemini-2.5-flash" # free + fast

def analyze_mood(entry_text: str) -> str:
    prompt = f"""
    Analyze the mood of this journal entry and return only one of the following:
    [happy, neutral, sad, excited, anxious, angry, calm, confused, tired, stressed].

    Journal entry:
    {entry_text}
    """

    response = client.models.generate_content(model=model, contents=prompt)
    mood = response.text.strip().lower()

    # Basic safety net
    valid_moods = {"happy", "neutral", "sad", "excited", "anxious", "angry", "calm", "confused", "tired", "stressed"}
    if mood not in valid_moods:
        return "neutral"
    return mood
