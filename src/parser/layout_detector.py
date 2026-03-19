def detect_layout(ocr_results: list) -> str:
    texts = {text for _, text, _ in ocr_results}

    if "Quick translation" in texts:
        return "yandex_new"
    elif "Yandex Translate" in texts and "Related words" in texts:
        return "yandex_old"
    elif "Yandex Translate" not in texts:
        return "google"
    
    return "unknown"