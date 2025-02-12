import os

#första funktionen att läsa filen/path
def read_file(path):  
    lst = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            lst.append(line.strip())
    return lst


def get_words(row):
    words = []
    word= ""
    



    a_z = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
    



    # Istället för "isalpha" så använder jag en lista med bokstäverna
    # Detta på grund av att tecken som finns ex. i det kinesiska alfabetet
    # blir "True" på "isalpha"
    for r in row:
        for c in r:
            if c not in a_z:
                c == " "
        
    for r in row:
        for c in r:
            if c in a_z:
                word += c.lower()
            elif c == " ":
                if word == "" or len(word) == 1:
                    word = ""
                    continue
                words.append(word)
                word = ""
             
    return words


def save_words(file_path, words):  # Funktion för att skriva över på en textfil

    with open(file_path, "w") as file:
        for word in words:
            file.writelines(words)
    print("Saved {} words in file {}".format(len(words), file_path))
    


en_new_path = "/Users/XPS/Desktop/1DV501/assignment_3/eng_news_100K-sentences.txt"
holy_grail_path = "/Users/XPS/Desktop/1DV501/assignment_3/holy_grail.txt"
ex = "/Users/XPS/Desktop/1DV501/assignment_3/ex.txt"

#get1 = get_words(read_file(en_new_path))
#get2 = get_words(read_file(holy_grail_path))

#save_words("outpath.txt",get1)
#save_words("outpath2.txt",get2)
row = read_file(holy_grail_path)
save_words("outpath2.txt",get_words(row))
#¤rows = read_file(en_new_path)
#save_words("outpath2.txt", rows)