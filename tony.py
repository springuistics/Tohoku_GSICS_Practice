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
    input_data = user_input.get()
    word_count = count_words(input_data)
    sentence_count = count_sentences(input_data)
    MLS = safe_MLS(word_count, sentence_count)
    if word_count < 10:
        return output.config(text="Your number of birds is not enough")
    elif MLS < 6:
        return output.config(text="Please use longer sentences")
    else:
        return output.config(text=f"Your number of words is: {word_count}, and your MLS is: {MLS}")

window = tkinter.Tk()
window.maxsize(800, 400)
window.minsize(800, 400)
window.title("Text Analysis")

main_frame = tkinter.Frame(window)
main_frame.config(width=800, height=400)
main_frame.pack()

user_input = tkinter.StringVar()

my_text = tkinter.Label(main_frame, text="Insert your text below", font=("Helvetica", 16), fg="blue", background="white")
my_text.pack()

entry_frame = tkinter.Frame(main_frame, width=360, height=360)
entry_frame.pack(pady=10)

username = tkinter.Entry(entry_frame, textvariable=user_input)
username.pack()

no = tkinter.Button(main_frame, text="Analyze Text", font=("Helvetica", 12), command=begin)
no.pack()

output = tkinter.Label(main_frame, font=("Helvetica", 12))
output.pack(pady=10)


window.mainloop()
