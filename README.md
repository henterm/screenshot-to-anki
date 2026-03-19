# Screenshot to Anki

Automatically convert translator app screenshots into Anki flashcards using OCR.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)

## What it does

1. Scans a folder of screenshots from Yandex Translate
2. Extracts source word and translation using OCR (EasyOCR)
3. Generates example sentences using LLM (Groq / LLaMA)
4. Exports ready-to-import Anki flashcards (.apkg)

## Pipeline
```
Screenshots → Preprocessing (OpenCV) → OCR (EasyOCR) → Layout Analysis → LLM Examples → Anki (.apkg)
```

## Installation
```bash
git clone https://github.com/henterm/screenshot-to-anki.git
cd screenshot-to-anki
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root:
```
GROQ_API_KEY=your_key_here
```

Get a free API key at https://console.groq.com

## Usage
```bash
streamlit run src/app.py
```

1. Enter the path to your screenshots folder
2. Click **Scan**
3. Review the extracted word pairs
4. Download the `.apkg` file and open it in Anki

## Supported layouts

| App | Layout | Status |
|-----|--------|--------|
| Yandex Translate (new) | White UI with Quick translation button | Done |
| Yandex Translate (old) | Yellow UI | Done |
| Google Translate | — | In progress |

## Tech stack

- **OpenCV + Pillow** — image preprocessing
- **EasyOCR** — text recognition
- **genanki** — Anki deck generation
- **Groq API (LLaMA 3.3)** — example sentence generation
- **Streamlit** — web UI

## Future Work

- Google Translate layout support
- Full language learning pipeline — personalized study plan based on user's reading materials, frequency analysis, spaced repetition optimization
- Mobile-friendly interface