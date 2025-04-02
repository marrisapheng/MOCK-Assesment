import tkinter as tk

def check():
    correct = 0
    incorrect = 0
    
    if answer1.get().strip() == "1914":
        correct += 1
    else:
        incorrect += 1
    
    if answer2.get().strip().lower() == "dallas":
        correct += 1
    else:
        incorrect += 1
    
    if answer3.get().strip().lower() == "mongol":
        correct += 1
    else:
        incorrect += 1
    
    if answer4.get().strip().lower() == "new zealand":
        correct += 1
    else:
        incorrect += 1
    
    if answer5.get().strip().lower() == "egypt":
        correct += 1
    else:
        incorrect += 1
    
    result_label.config(text=f"Correct: {correct}\nIncorrect: {incorrect}")

def quiz():
    global answer1, answer2, answer3, answer4, answer5, result_label
    
    #question
    question1 = tk.Label(root, text="In which year did World War 1 start?")
    question2 = tk.Label(root, text="Where was John F. Kennedy assassinated?")
    question3 = tk.Label(root, text="Which empire was ruled by Genghis Khan?")
    question4 = tk.Label(root, text="Which country was first to grant women the right to vote?")
    question5 = tk.Label(root, text="What ancient civilization is known for its pyramids?")
    
    #answer
    answer1 = tk.Entry(root)
    answer2 = tk.Entry(root)
    answer3 = tk.Entry(root)
    answer4 = tk.Entry(root)
    answer5 = tk.Entry(root)
    
    #submit
    submit_button = tk.Button(root, text="Submit Answers", command=check)
    
    #result
    result_label = tk.Label(root, text="")
    
    #pack
    question1.pack()
    answer1.pack()
    question2.pack()
    answer2.pack()
    question3.pack()
    answer3.pack()
    question4.pack()
    answer4.pack()
    question5.pack()
    answer5.pack()
    submit_button.pack()
    result_label.pack()

# Initialize main window
root = tk.Tk()
root.title("History Quiz")
root.geometry("400x500")

#start button
start_button = tk.Button(root, text="Start Quiz", command=quiz)
start_button.pack()

root.mainloop()
