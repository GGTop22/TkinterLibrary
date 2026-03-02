import tkinter as tk
from datetime import datetime, date
from tkinter import messagebox
import json
import requests


class Library:
    def __init__(self, root):
        self.root = root
        self.root.title("Library System")
        self.root.geometry("500x900")

        tk.Label(root, text="Управление библиотекой", font=("Arial", 16)).pack(pady=10)

        tk.Label(root, text="Номер книги:").pack()
        self.example_id_entry = tk.Entry(root, width=30)
        self.example_id_entry.pack()

        tk.Label(root, text="Название книги:").pack()
        self.title_entry = tk.Entry(root, width=30)
        self.title_entry.pack()

        tk.Label(root, text="ID читателя:").pack()
        self.reader_id_entry = tk.Entry(root, width=30)
        self.reader_id_entry.pack()

        tk.Label(root, text="Дата выдачи (YYYY-MM-DD):").pack()
        self.takeout_date_entry = tk.Entry(root, width=30)
        self.takeout_date_entry.pack()

        tk.Label(root, text="Дата возврата (YYYY-MM-DD):").pack()
        self.return_date_entry = tk.Entry(root, width=30)
        self.return_date_entry.pack()

        self.status_label = tk.Label(root, text="Статус: ДОСТУПНА", fg="green", font=("Arial", 12))
        self.status_label.pack(pady=10)

        tk.Button(root, text="Выдать", command=self.give_book, width=15).pack(pady=5)
        tk.Button(root, text="Вернуть", command=self.return_book, width=15).pack(pady=5)

        tk.Label(root, text=" Управление читателями", font=("Arial", 14)).pack(pady=10)

        tk.Label(root, text="ID читателя:").pack()
        self.reader_id_manage_entry = tk.Entry(root, width=30)
        self.reader_id_manage_entry.pack()

        tk.Label(root, text="Имя читателя:").pack()
        self.reader_name_entry = tk.Entry(root, width=30)
        self.reader_name_entry.pack()

        # tk.Button(root, text="Создать читателя", command=self.create_reader, width=20).pack(pady=3)
        # tk.Button(root, text="Редактировать читателя", command=self.update_reader, width=20).pack(pady=3)
        # tk.Button(root, text="Удалить читателя", command=self.delete_reader, width=20).pack(pady=3)
        # tk.Button(root, text="Найти читателя", command=self.get_reader, width=20).pack(pady=3)

        tk.Label(root, text="ID Читателя").pack()
        self.nchit_entry = tk.Entry(root, width=30)
        self.nchit_entry.pack()
        tk.Button(root, text="Инфо", command=self.show_info, width=15).pack(pady=5)

        tk.Label(root, text="Ответ сервера (JSON):", font=("Arial", 12)).pack(pady=5)

        frame = tk.Frame(root)
        frame.pack(pady=5, fill="both", expand=True)

        self.json_text = tk.Text(frame, height=12, wrap="word")
        self.json_text.pack(side="left", fill="both", expand=True)

    def give_book(self):
        takeout_date = self.takeout_date_entry.get()
        return_date = self.return_date_entry.get()
        example_id = self.example_id_entry.get()
        reader_id = self.reader_id_entry.get()
        title = self.title_entry.get()
        if not takeout_date:
            takeout_date = str(datetime.now().date())
        url = 'http://127.0.0.1:5000/book_schedule'
        payload = {'takeout_date': takeout_date, 'return_date': return_date, 'ex_id': example_id,
                   'reader_id': reader_id, 'title': title}
        r = requests.post(url, json=payload)
        self.json_text.insert(tk.INSERT, r.json())

        # if takeout_date and not return_date:
        #     self.status_label.config(text="Статус: ВЫДАНА", fg="orange")
        #     messagebox.showinfo("Успех", "Книга успешно выдана")
        # else:
        #     messagebox.showerror("Ошибка", "Для выдачи должна быть указана только дата выдачи")

    def return_book(self):
        takeout_date = self.takeout_date_entry.get()
        return_date = self.return_date_entry.get()
        example_id = self.example_id_entry.get()
        reader_id = self.reader_id_entry.get()
        title = self.title_entry.get()
        url = 'http://127.0.0.1:5000/book_schedule'
        payload = {'takeout_date': takeout_date, 'return_date': return_date, 'ex_id': example_id,
                   'reader_id': reader_id, 'title': title}
        r = requests.put(url, json=payload)
        self.json_text.insert(tk.INSERT, r.json())
        # if takeout_date and return_date:
        #     self.status_label.config(text="Статус: ВОЗВРАЩЕНА", fg="green")
        #     messagebox.showinfo("Успех", "Книга возвращена")
        # else:
        #     messagebox.showerror("Ошибка", "Для возврата должны быть указаны обе даты")

    # def create_reader(self):
    #     reader_id = self.reader_id_manage_entry.get()
    #     name = self.reader_name_entry.get()
    #
    #     url = 'http://127.0.0.1:5000/reader'
    #     payload = {
    #         "reader_id": reader_id,
    #         "name": name,
    #
    #     }
    #
    #     r = requests.post(url, json=payload)
    #     self.json_text.insert(tk.INSERT, json.dumps(r.json()))
    #
    # def update_reader(self):
    #     reader_id = self.reader_id_manage_entry.get()
    #     name = self.reader_name_entry.get()
    #
    #     url = f'http://127.0.0.1:5000/reader/{reader_id}'
    #     payload = {
    #         "name": name,
    #
    #     }
    #
    #     r = requests.put(url, json=payload)
    #     self.json_text.insert(tk.INSERT, json.dumps(r.json()))


    def show_info(self):
        nchit = self.nchit_entry.get()
        url = 'http://127.0.0.1:5000/book_schedule'
        r = requests.get(url + "/" + nchit)
        self.json_text.insert(tk.INSERT, r.json())


if __name__ == "__main__":
    root = tk.Tk()
    app = Library(root)
    root.mainloop()
