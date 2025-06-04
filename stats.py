def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def number_of_words(text_as_string):
    word_count = len(text_as_string.split())
    return word_count

def number_of_chars(path_to_file):
    text_dict = {}
    keys_text = set(get_book_text(path_to_file).lower())
    for key in keys_text:
        text_dict[key] = get_book_text(path_to_file).lower().count(key)
    return text_dict

def sort_on(dict):
    return dict["num"]

def sort_chars_dict(text_dict):
    text_list = []
    for key in text_dict:
        text_list.append({'char':key, 'num':text_dict[key]})
    text_list.sort(reverse=True, key=sort_on)
    return text_list