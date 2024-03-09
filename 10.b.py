import tkinter as tk
from tkinter import simpledialog
from googletrans import Translator
import random

def get_translation(word, dest_language):
    translator = Translator()
    translation = translator.translate(word, dest=dest_language).text
    return translation

def compare_languages():
    word = entry_word_compare.get().strip().lower()
    lang1 = entry_lang1_compare.get().strip().lower()
    lang2 = entry_lang2_compare.get().strip().lower()

    supported_languages = ['en', 'hi', 'bn', 'te', 'mr', 'ta', 'ur', 'gu', 'kn', 'or',
                           'fr', 'de', 'es', 'it', 'nl', 'pt', 'ru', 'zh-cn', 'ja']
    if lang1 not in supported_languages or lang2 not in supported_languages:
        result_label_compare.config(text="Unsupported language. Please choose from the supported languages.", fg="red")
        return

    translation1 = get_translation(word, lang1)
    translation2 = get_translation(word, lang2)

    result_label_compare.config(text=f"In {lang1.upper()}, '{word}' is called: {translation1}\n"
                                     f"In {lang2.upper()}, '{word}' is called: {translation2}", fg="green")

def translate():
    word = entry_word_translate.get().strip().lower()
    dest_language = entry_lang_translate.get().strip().lower()

    supported_languages = ['en', 'hi', 'bn', 'te', 'mr', 'ta', 'ur', 'gu', 'kn', 'or',
                           'fr', 'de', 'es', 'it', 'nl', 'pt', 'ru', 'zh-cn', 'ja']
    if dest_language not in supported_languages:
        result_label_translate.config(text="Unsupported language. Please choose from the supported languages.", fg="red")
        return

    translation = get_translation(word, dest_language)
    result_label_translate.config(text=f"The translation of '{word}' to {dest_language.upper()} is: {translation}", fg="blue")

def french_vocabulary_quiz():
    vocabulary = {
        "apple": "pomme",
        "banana": "banane",
        "cat": "chat",
        "dog": "chien",
        "house": "maison",
        "car": "voiture",
        "book": "livre",
        "computer": "ordinateur",
        "friend": "ami",
        "school": "école",
        # Add more words as needed
    }

    score = 0
    num_questions = 5
    quiz_results = []

    for _ in range(num_questions):
        word, translation = random.choice(list(vocabulary.items()))
        user_response = simpledialog.askstring("Input", f"What is the French translation of '{word}'?", parent=root)
        if user_response and user_response.strip().lower() == translation.lower():
            score += 1
            user_answer = "Correct"
        else:
            user_answer = "Incorrect"
        quiz_results.append((word, translation, user_answer))

    quiz_report = "\n".join([f"{word}: Correct answer - {translation}, Your response - {response}"
                             for word, translation, response in quiz_results])

    result_label_quiz.config(text=f"Quiz Results:\n{quiz_report}\n\nYou scored {score}/{num_questions}", fg="white")

def main():
    global root, entry_word_translate, entry_lang_translate, entry_word_compare, entry_lang1_compare, entry_lang2_compare
    global result_label_translate, result_label_compare, result_label_quiz

    root = tk.Tk()
    root.title("Multilingual Language Tool")
    root.geometry("600x600")
    root.configure(bg="black")

    label_intro = tk.Label(root, text="Welcome to the Multilingual Language Tool!", bg="black", fg="white", font=("Arial", 16, "bold"))
    label_intro.pack(pady=(10, 20))

    # Translation Section
    label_translate = tk.Label(root, text="Translation", bg="black", fg="white", font=("Arial", 14, "bold"))
    label_translate.pack(pady=(0, 10))

    label_word_translate = tk.Label(root, text="Enter the English word:", bg="black", fg="white")
    label_word_translate.pack()
    entry_word_translate = tk.Entry(root, width=50)
    entry_word_translate.pack()

    label_dest_lang_translate = tk.Label(root, text="Enter the destination language code:", bg="black", fg="white")
    label_dest_lang_translate.pack()
    entry_lang_translate = tk.Entry(root)
    entry_lang_translate.pack()

    translate_button = tk.Button(root, text="Translate", command=translate)
    translate_button.pack(pady=(10, 20))

    result_label_translate = tk.Label(root, text="", bg="black", fg="white")
    result_label_translate.pack()

    # Comparison Section
    label_compare = tk.Label(root, text="Compare Languages", bg="black", fg="white", font=("Arial", 14, "bold"))
    label_compare.pack(pady=(20, 10))

    label_word_compare = tk.Label(root, text="Enter the English word:", bg="black", fg="white")
    label_word_compare.pack()
    entry_word_compare = tk.Entry(root)
    entry_word_compare.pack()

    label_lang1_compare = tk.Label(root, text="Enter the first language code:", bg="black", fg="white")
    label_lang1_compare.pack()
    entry_lang1_compare = tk.Entry(root)
    entry_lang1_compare.pack()

    label_lang2_compare = tk.Label(root, text="Enter the second language code:", bg="black", fg="white")
    label_lang2_compare.pack()
    entry_lang2_compare = tk.Entry(root)
    entry_lang2_compare.pack()

    compare_button = tk.Button(root, text="Compare", command=compare_languages)
    compare_button.pack(pady=(10, 20))

    result_label_compare = tk.Label(root, text="", bg="black", fg="white")
    result_label_compare.pack()

    # Quiz Section
    label_quiz = tk.Label(root, text="French Vocabulary Quiz", bg="black", fg="white", font=("Arial", 14, "bold"))
    label_quiz.pack(pady=(20, 10))

    quiz_button = tk.Button(root, text="Take Quiz", command=french_vocabulary_quiz)
    quiz_button.pack(pady=(0, 10))

    result_label_quiz = tk.Label(root, text="", bg="black", fg="white")
    result_label_quiz.pack()

    button_exit = tk.Button(root, text="Exit", command=root.destroy)
    button_exit.pack(pady=(20, 0))

    root.mainloop()

if __name__ == "__main__":
    main()