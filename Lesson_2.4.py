"""
Пользователь вводит строку из нескольких слов, разделённых
пробелами. Вывести каждое слово с новой строки. Строки
необходимо пронумеровать. Если в слово длинное, выводить
только первые 10 букв в слове.
The user enters a string of several words separated by spaces.
Print each word from a new line. The lines must be numbered.
If the word is long, print only the first 10 letters in the
word.
"""


y_words = input("Enter any words divided with space - ")
word_list = list(y_words.split())
for i in range(len(word_list)):
    if len(word_list[i]) > 10:
        print(i + 1, "-", word_list[i][:10])
        continue
    print(i + 1, "-", word_list[i])
