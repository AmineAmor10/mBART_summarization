import json
import re
import time
import unicodedata

import plac
import tensorflow_datasets as tfds

spaces = re.compile(r"\s+")


def clean(text):
    text = (
        text.replace("_START_SECTION_", " ")
        .replace("_START_PARAGRAPH_", " ")
        .replace("_NEWLINE_", " ")
    )
    text = unicodedata.normalize("NFC", text)
    return spaces.sub(" ", text).strip()


# Add first sentence of every paragraph to the intro (summary)
def get_extended_intro(intro, text):
    li = text.split("_START_PARAGRAPH_")
    extended_intro = []
    for paragraph in li:
        paragraph = clean(paragraph)
        paragraph_li = paragraph.split(". ")
        first_sent = paragraph_li[0] + "."
        extended_intro.append(first_sent)
    # To add the second line of each paragraph as well
    #         if len(paragraph_li) > 1:
    #             second_sent = paragraph_li[1] + "."
    #             extended_intro.append(second_sent)

    extension = " ".join(extended_intro)
    long_intro = intro + " " + extension
    return long_intro


def main():
    language = "fr"

    for split, group, limit in (
        ("train", "train", 10000000),
        ("validation", "valid", 2000),
        ("test", "test", 2000),
    ):
        i = 0
        data = []

        for ex in tfds.load(f"wiki40b/{language}", split=split):
            parts = (
                ex["text"]
                .numpy()
                .decode("utf-8")
                .split("_START_ARTICLE_", 1)[1]
                .split("_START_SECTION_", 1)
            )
            
            if len(parts) != 2:
                continue
                
            intro, text = parts
            intro_paragraphs = intro.split("_START_PARAGRAPH_", 1)
            
            if len(intro_paragraphs) < 2:
                continue
                
            intro = clean(intro_paragraphs[1])
            text = text.split("_START_PARAGRAPH_", 1)[1]
            intro = get_extended_intro(intro, text)
            intro_size = len(intro.split(" "))

            text = clean(text)
            text_size = len(text.split(" "))

            
            if intro_size < 80 or text_size < 1000:
                continue

            data.append(
                {
                    "text": text,
                    "summary": intro,
                }
            )

            i += 1
            if i > limit:
                break

        with open(f"long_wiki_fr/{group}.json", "w") as f:
            for json_obj in data:
                json.dump(json_obj, f, sort_keys=False, indent=None, ensure_ascii=False)
                f.write("\n")


if __name__ == "__main__":
    start_time = time.time()
    plac.call(main)
    print(f"--- {time.time() - start_time} seconds ---")

