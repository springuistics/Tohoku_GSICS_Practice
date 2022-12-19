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
    if word_count <= 10:
        output.config(text=f"This is not enough words")
    elif MLS <= 6:
        output.config(text=f"Use longer sentences")
    elif MLS >= 10:
        output.config(text=f"Your number of words is: {word_count}, and your MLS is: {MLS}")

window = tkinter.Tk()
window.maxsize(800, 400)
window.minsize(800, 400)

#img = PhotoImage(file="Vick.PNG")
#label = Label(ws, image=img)
#label.place(x=0, y=0)
#label.pack()

user_input = tkinter.StringVar()

my_text = tkinter.Label(window, text="Insert my text below", font=('Segoe Script', 25, 'bold', 'italic'), fg="red")
my_text.pack()

username = tkinter.Entry(window, textvariable=user_input, width=60)
username.pack()

no = tkinter.Button(window, text="Analyze Text", font=('Georgia', 15, 'italic'), command=begin)
no.pack()

output = tkinter.Label(window, font=20)
output.pack()


window.mainloop()

