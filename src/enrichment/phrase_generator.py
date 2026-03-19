from groq import Groq
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / ".env")

client = Groq()

def generate_examples(source: str, translation: str, n: int = 2) -> str:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": f"""Give me {1} short example sentences and translation to it using the word "{source}" \
            (translation: "{translation}"). \
            Format: just the sentences, one per line, no numbering."""}
        ],
        max_tokens=200
    )
    return response.choices[0].message.content