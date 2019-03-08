__author__ = 'aganiger'


def length_of_last_word(word):
    words = word.split(" ")
    if len(words) == 0:
        return 0
    return len(words[-1])


def length_of_all_words(word):
    words = word.split(" ")
    if len(words) == 0:
        print("No words in sentence");
    for word in words:
        print("%s : %d" % (word, len(word)))


print(length_of_last_word("My name is Ajit"))
length_of_all_words("My name is Ajit")


def findlength(string):
    words = string.split(" ")
    for word in words:
        print("%s, %d" % (word, len(word)))


findlength("My name is Ajit");
