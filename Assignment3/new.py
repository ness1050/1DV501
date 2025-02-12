import os


def read_file(path_file):

    l_count = 0

    with open (path_file, "r", encoding = "utf-8") as file:
        for line in file:
            l_count = l_count + 1
            content = file.readlines()
        return content

def get_words(row: list):
    final_row = []
    row = row.split(' ')
    row = [element.strip() for element in row]
    row = [element for element in row if element.isascii() and not element.isdigit()]

    for element in row:
        # Make sure each element either has apostrophe or is alphanumeric
        for ch in ['//', '`', '|', '*', '_', '{', '}', '[', ']', '(', ')', '>', '#', '+', '-', '.', ',', '!', '$', '/'',' '']:
            if ch in element:
                # If character in element replace it with nothing.
                element = element.replace(ch, '')
        # Make element lowercase
        element = element.lower()
        # Make sure element is not empty, or a digit.
        if element != '' and not element.isdigit():
            final_row.append(element)

    #final_row = [element for element in row if element != '']
    # final_row = ' '.join(final_row)
    return final_row

def save_words(file_path, words):  # Funktion för att skriva över på en textfil

    with open(file_path, "w", encoding="utf-8") as file:
        word_ = file.writelines(words)
    print("Saved {} words in file {}".format(len(words), file_path))
    return word_


eng_file = "/Users/XPS/Desktop/1DV501/assignment_3/large_texts.txt/eng_news_100K-sentences.txt "
holy_grail = "/Users/XPS/Desktop/1DV501/assignment_3/large_texts.txt/holy_grail.txt"

find_first =  get_words(read_file(eng_file))
find_second = get_words(read_file(holy_grail))

save_words("/outpath.txt", find_first)
save_words("/outpath2.txt", find_second)