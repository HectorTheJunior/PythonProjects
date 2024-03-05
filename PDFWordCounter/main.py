import re
from collections import Counter
from PyPDF2 import PdfReader


def text_from_pdf(pdf_file: str) -> list[str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PdfReader(pdf, strict=False)

        print("Pages: ", len(reader.pages))
        print("-" * 12)  # divider

        pdf_text: list[str] = [page.extract_text() for page in reader.pages]
        return pdf_text


def word_count(text_list: list[str]) -> Counter:
    words: list[str] = []
    for text in text_list:
        split_text: list[str] = re.split(r"\s+|[,;?!.-]\s+", text.lower())

        words += [word for word in split_text if word]
    print(f"Amount of words: {len(words)}")
    print("-" * 10)

    return Counter(words)


def main():
    given_text: list[str] = text_from_pdf('believer.pdf')
    counter: Counter = word_count(text_list=given_text)
    for page in given_text:
        print(page)
    print("-" * 10)
    print("Most common words in text: ")
    print()
    for word, mentions in counter.most_common(5):
        print(f'{word:10}: {mentions} times')


main()
