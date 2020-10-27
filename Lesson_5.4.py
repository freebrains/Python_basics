"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
Create (without using a program) a text file with the following contents:
One-1
Two — 2
Three — 3
Four — 4
You need to write a program that opens the file for reading and reads the data
line by line. In this case, English numerals should be replaced with Russian ones.
The new block of lines must be written to a new text file.
"""



translate_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open(r"D:\Big_Data\Back_Up\Lesson_5.4_rus.txt", 'a') as translate:
    with open(r"D:\Big_Data\Back_Up\Lesson_5.4.txt") as english:
        for line in english:
            new_line = line.split(" - ")
            new_line[0] = translate_dict.get(new_line[0])
            translate.writelines(new_line[0] + ' - ' + new_line[1])
