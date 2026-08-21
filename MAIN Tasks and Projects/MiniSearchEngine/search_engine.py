import os
import re


DOCUMENT_FOLDER = "documents"


def clean_word(word):
    """
    Remove punctuation and convert word to lowercase.
    """
    return re.sub(r"[^a-zA-Z0-9]", "", word.lower())


def get_words_from_file(filename):
    """
    Read a file and return cleaned words.
    """

    try:

        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        words = text.split()

        cleaned_words = []

        for word in words:

            word = clean_word(word)

            if word:
                cleaned_words.append(word)

        return cleaned_words

    except Exception as e:

        print(f"Error reading {filename}: {e}")

        return []


def search_file(filename, search_word):
    """
    Count how many times search_word appears in a file.
    """

    words = get_words_from_file(filename)

    search_word = clean_word(search_word)

    count = words.count(search_word)

    return count


def search_documents(search_word):

    results = []

    if not os.path.exists(DOCUMENT_FOLDER):

        print(
            f"Folder '{DOCUMENT_FOLDER}' does not exist."
        )

        return results

    for filename in os.listdir(DOCUMENT_FOLDER):

        if filename.endswith(".txt"):

            filepath = os.path.join(
                DOCUMENT_FOLDER,
                filename
            )

            count = search_file(
                filepath,
                search_word
            )

            if count > 0:

                results.append(
                    {
                        "filename": filename,
                        "count": count
                    }
                )

    # Sort by number of matches
    results.sort(
        key=lambda result: result["count"],
        reverse=True
    )

    return results


def display_results(results, search_word):

    print("\n========== SEARCH RESULTS ==========")

    if not results:

        print(
            f"No results found for '{search_word}'."
        )

        return

    for rank, result in enumerate(results, start=1):

        print(
            f"{rank}. "
            f"{result['filename']} "
            f"→ {result['count']} matches"
        )


def main():

    print("========== MINI SEARCH ENGINE ==========")

    while True:

        search_word = input(
            "\nEnter word to search "
            "(or 'exit'): "
        ).strip()

        if search_word.lower() == "exit":

            print("Search engine closed.")

            break

        if not search_word:

            print("Please enter a search word.")

            continue

        results = search_documents(
            search_word
        )

        display_results(
            results,
            search_word
        )


main()