from parser.layout_detector import detect_layout

def parse_yandex_new(ocr_results: list) -> dict:
    pars = {"source": "", "translation": ""}
    STOP_WORDS = {"Examples", "Dictionary", "Related words", "Declensions and", "Ask Al Translator"}
    y_sep = None
            
    for bbox, text, confidence in ocr_results:
        if text in ("Quick translation", "Dictionary") and confidence > 0.85:
            y_sep = bbox[0][1]
            break

    if y_sep is None:
        return pars

    y_best = -1
    y_best_trans = float("inf")
    for bbox, text, confidence in ocr_results:
        y = bbox[0][1]
        if y < y_sep and confidence > 0.9:
            if y > y_best and text not in STOP_WORDS and any(c.isalpha() for c in text):
                y_best = y
                pars["source"] = text
        elif y > y_sep and confidence > 0.9:
            y_trans = bbox[0][1]
            if y_trans < y_best_trans and text not in STOP_WORDS and any(c.isalpha() for c in text):
                y_best_trans = y_trans
                pars["translation"] = text
                
    return pars

def parse_yandex_old(ocr_results: list) -> dict:
    pars = {"source": "", "translation": ""}
    STOP_WORDS = {"Examples", "Dictionary", "Related words", "Declensions and", "Ask Al Translator"}
    y_sep = None

    for bbox, text, confidence in ocr_results:
        if text in ("Examples", "Dictionary", "Related words") and confidence > 0.95:
            y_sep = bbox[0][1]
            break

    if y_sep is None:
        return pars
        
    y_best_1 = y_best_2 = -1
    for bbox, text, confidence in ocr_results:
        y = bbox[0][1]
        if y < y_sep and text not in STOP_WORDS and any(c.isalpha() for c in text):
            if y > y_best_1:
                y_best_2 = y_best_1
                pars["source"] = pars["translation"]
                y_best_1 = y
                pars["translation"] = text
            elif y > y_best_2:
                y_best_2 = y
                pars["source"] = text

    return pars

def parse_translation(ocr_results: list) -> dict:
    layout = detect_layout(ocr_results)
    
    if layout == "yandex_new":
        return parse_yandex_new(ocr_results)
    elif layout == "yandex_old":
        return parse_yandex_old(ocr_results)
    else:
        return {"source": "", "translation": ""}