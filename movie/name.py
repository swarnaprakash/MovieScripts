import os
import re

def is_year(word):
    if word and word.isdigit():
        year = int(word)
        if 1900 <= year <= 2100:
            return True
    return False

def is_junk_word(word):
    this_dir, this_filename = os.path.split(__file__)
    data_dir = os.path.join(this_dir, "data")
    junk_words_path = os.path.join(data_dir, "junk_words")
    with open(junk_words_path, 'r') as junk_words:
        return any(junk_word.strip() == word for junk_word in junk_words)

def is_valid(word):
    return word and not is_junk_word(word) and not is_year(word)

def split(file_path):
    base_name = os.path.basename(file_path)
    parts = re.split('[^a-zA-Z0-9]+', base_name, 0, re.IGNORECASE)
    return parts

def extract_name(file_path):
    valid_parts = filter(is_valid, split(file_path))
    movie_name = ' '.join(valid_parts)
    return movie_name

def extract_year(file_path):
    year_list = filter(is_year, split(file_path))

    if year_list:
        # Year is most likely to occur at the end
        return year_list[-1]
    else:
        return None

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="Path to the file or folder representing the movie")
    args = parser.parse_args()

    file_path = args.file_path
    print extract_name(file_path)
