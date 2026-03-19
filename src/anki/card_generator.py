import genanki

MODEL_ID = 1362751240
DECK_ID = 1582876399

model = genanki.Model(
    MODEL_ID,
    'Translation Card',
    fields=[
        {'name': 'source'},
        {'name': 'translation'},
        {'name': 'examples'}
    ],
    templates=[
        {
            'name': 'Card',
            'qfmt': '{{source}}',
            'afmt': '{{translation}}<br><br><i>{{examples}}</i>'
        }
    ]
)

def generate_deck(pairs: list[dict], output_path: str) -> None:
    deck = genanki.Deck(DECK_ID, "MyVocabulary")
    for pair in pairs:
        note = genanki.Note(model=model, fields=[pair["source"], pair["translation"], pair.get("examples", "")])
        deck.add_note(note)
    genanki.Package(deck).write_to_file(output_path)