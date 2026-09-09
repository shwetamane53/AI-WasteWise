from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Location of knowledge base
KB_FILE = Path(__file__).parent / "waste_info.txt"


def load_knowledge_base():

    with open(KB_FILE, "r", encoding="utf-8") as file:
        text = file.read()

    # Split the knowledge base using waste-category headings
    headings = [
        "PLASTIC WASTE",
        "BATTERY WASTE",
        "E-WASTE",
        "ORGANIC WASTE",
        "PAPER WASTE",
        "TEXTILE WASTE"
    ]

    documents = []

    for i, heading in enumerate(headings):

        start = text.find(heading)

        if start == -1:
            continue

        if i + 1 < len(headings):
            end = text.find(headings[i + 1])

            if end == -1:
                section = text[start:]
            else:
                section = text[start:end]
        else:
            section = text[start:]

        documents.append(section.strip())

    return documents


# Load documents
documents = load_knowledge_base()


# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer(
    stop_words="english"
)

document_vectors = vectorizer.fit_transform(documents)


def retrieve_information(query, top_k=1):

    query_vector = vectorizer.transform([query])

    similarities = cosine_similarity(
        query_vector,
        document_vectors
    ).flatten()

    top_indices = similarities.argsort()[-top_k:][::-1]

    results = []

    for index in top_indices:

        if similarities[index] > 0:
            results.append(documents[index])

    return results
