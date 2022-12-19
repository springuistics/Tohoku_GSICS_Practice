import tkinter

def count_words(data):
    string_analysis = data.split(" ")
    word_count = len(string_analysis)
    return word_count

def count_sentences(data):
    periods = data.count(".")
    exclamation = data.count('!')
    question = data.count('?')
    number_of_sentences = periods + exclamation + question
    return number_of_sentences

def safe_MLS(x, y):
    if x == 0:
        return 0
    if y == 0:
        return x
    else:
        return x/y

def begin():
    input_data = user_update