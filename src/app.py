import streamlit as st
from scanner.preprocessor import preprocess
from scanner.ocr_engine import extract_text
from scanner.gallery_scanner import scan_gallery
from parser.translator_parser import parse_translation
from anki.card_generator import generate_deck
from enrichment.phrase_generator import generate_examples

st.title("Screenshot to Anki")
folder = st.text_input("Folder path")

if st.button("Scan"):
    files = scan_gallery(folder)
    pairs = []
    progress = st.progress(0)
    for i, f in enumerate(files):
        img = preprocess(f)
        ocr = extract_text(img)
        result = parse_translation(ocr)
        if result["source"] and result["translation"] and result["source"] != result["translation"]:
            result["examples"] = generate_examples(result["source"], result["translation"])
            pairs.append(result)
        progress.progress((i + 1) / len(files))

    st.dataframe(pairs)

    generate_deck(pairs, "vocabulary.apkg")

    with open("vocabulary.apkg", "rb") as f:
        st.download_button(
            label="Download .apkg",
            data=open("vocabulary.apkg", "rb").read(),
            file_name="vocabulary.apkg"
        )