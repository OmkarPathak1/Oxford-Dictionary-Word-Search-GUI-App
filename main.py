import tkinter as tk
from tkinter import scrolledtext

# Define constants
WORD_LIST_FILE = "Word Finder/words.txt"

# Load word list from file
with open(WORD_LIST_FILE, "r") as file:
    word_list = file.read().splitlines()
# Define GUI window
root = tk.Tk()
root.title("Word Search")
root.geometry("400x600")
root.configure(bg="#FFFFFF")  # Set background color

# Define GUI widgets
label = tk.Label(root, text="Enter letters to search for:", font=("Arial", 14), bg="#FFFFFF")
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), bd=0, bg="#F1F1F1", relief=tk.GROOVE)
entry.pack(ipady=5, padx=20, pady=10)
entry.focus()

# Add a checkbox for searching for letters in order
check_var = tk.IntVar()
check_button = tk.Checkbutton(root, text="Sequential Order", variable=check_var, font=("Arial", 12),
                              bg="#FFFFFF")
check_button.pack(pady=10)

results_label = tk.Label(root, text="Search results:", font=("Arial", 14), bg="#FFFFFF")
results_label.pack(pady=10)

# Add a scrolled-text widget for the search results
results_text = scrolledtext.ScrolledText(root, width=40, height=10, font=("Arial", 12), wrap=tk.WORD, bd=0,
                                         bg="#F1F1F1", relief=tk.GROOVE)
results_text.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)


def search_words():
    letters = entry.get().lower()
    if check_var.get() == 1:
        matching_words = [word for word in word_list if letters in word.lower()]
    else:
        matching_words = [word for word in word_list if all(char in word.lower() for char in letters)]
    return matching_words


def display_results():
    results = search_words()
    if not results:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "No words found.")
    else:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "\n".join(results))


def on_return():
    display_results()


button = tk.Button(root, text="Search", font=("Arial", 14), bg="#4CAF50", fg="#000000", bd=0, relief=tk.FLAT,
                   command=display_results)
button.pack(pady=10)
entry.bind('<Return>', on_return)
root.mainloop()
