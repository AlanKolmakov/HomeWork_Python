from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import json
import os.path


# класс Paint
class Paint(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.filename = "data.json"
        self.data_old = {}
        self.data = []
        self.entry = None
        self.entry2 = None
        self.txt = None
        self.status = None
        self.flag = False
        self.setUI()

    def append_data(self):
        self.data_old.update({self.entry.get(): self.entry2.get()})
        self.txt.delete(1.0, END)
        self.txt.insert(END, str(self.data_old))
        self.entry.delete(0, END)
        self.entry2.delete(0, END)

    def set_directory(self):
        self.status = Label(self, text=f"Текущая директория: {self.filename}", font="Arial 10")
        self.status.grid(row=9)

    def show_file(self):
        with open(self.filename, "r") as f:
            content = f.read()
            self.txt.delete(1.0, END)
            self.txt.insert(END, content)

    def open_as(self):
        op = askopenfilename()
        print(op)
        f = open(op, "r")
        content = f.read()
        self.txt.delete(1.0, END)
        self.txt.insert(END, content)
        self.filename = op
        self.set_directory()

    def save_as(self):
        sa = asksaveasfilename()
        content = self.txt.get(1.0, END)
        f = open(sa, "w")
        f.write(content)
        f.close()

    def _save(self):
        if self.flag:
            with open(self.filename, "w") as f:
                json.dump(self.txt.get(1.0, "end-1c"), f, indent=4, encoding='utf-8')
                self.flag = False
        else:
            self.data.append(self.data_old)
            with open(self.filename, "a") as f:
                json.dump(self.data, f, indent=4, ensure_ascii=False)
            self.data = []
            self.data_old = {}

    def show(self):
        self.txt.delete(1.0, END)
        self.txt.insert(END, str(self.data_old))

    def manual_change(self):
        self.flag = True

    def setUI(self):
        # Устанавливаем название окна
        self.parent.title("HomeWork")
        # Размещаем активные элементы на родительском окне
        self.pack(fill=BOTH, expand=1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(8, weight=1)

        self.entry = Entry(self, width=20, bd=3)
        self.entry.grid(row=1, column=4, padx=5, sticky='w')
        self.entry2 = Entry(self, width=20, bd=3)
        self.entry2.grid(row=2, column=4, padx=5, sticky='w')
        self.txt = Text(self, width=20, font="Arial 14", wrap=WORD)
        self.txt.grid(row=8, column=0, columnspan=5, padx=5, pady=5, sticky=E + W + S + N)
        if os.path.isfile(self.filename):
            pass
        else:
            with open(self.filename, "w") as f:
                pass
        self.status = Label(self, text=f"Текущая директория: {self.filename}", font="Arial 10")
        self.status.grid(row=9)

        Label(self, text="Выбор действия: ").grid(row=0, column=0, padx=6, sticky='w')
        Label(self, text="Введите страну: ").grid(row=1, column=3, sticky='e')
        Label(self, text="Введите столицу: ").grid(row=2, column=3, sticky='e')

        Button(self, text="Открыть файл", width=20, command=self.open_as).\
            grid(row=1, column=0, padx=10, pady=2, sticky='w')
        Button(self, text="Сохранить как", width=20, command=self.save_as).\
            grid(row=2, column=0, padx=10, pady=2, sticky='w')
        Button(self, text="Добавить данные", width=17, command=self.append_data).\
            grid(row=3, column=4, padx=5, pady=2, sticky='w')
        Button(self, text="Редактирование данных", width=20, command=self.manual_change).\
            grid(row=3, column=0, padx=10, pady=2, sticky='w')
        Button(self, text="Сохранение данных", width=17, command=self._save).\
            grid(row=4, column=4, padx=5, pady=2, sticky='w')
        Button(self, text="Показать текущие данные", width=20, command=self.show).\
            grid(row=4, column=0, padx=10, pady=2, sticky='w')
        Button(self, text="Показать данные файла", width=20, command=self.show_file).\
            grid(row=5, column=0, padx=10, pady=2, sticky='w')


# выход из программы
def close_win():
    if askyesno("Выход", "Вы уверены?"):
        root.destroy()


# вывод справки
def about():
    showinfo("Домашняя работа от 12. 02. 2022")


# функция для создания главного окна
def main():
    global root
    root = Tk()
    root.geometry("800x400+300+300")
    Paint(root)
    m = Menu(root)
    root.config(menu=m)

    fm = Menu(m)
    m.add_cascade(label="Файл", menu=fm)
    fm.add_command(label="Выход", command=close_win)
    hm = Menu(m)
    m.add_cascade(label="Справка", menu=hm)
    hm.add_command(label="О программе", command=about)
    root.mainloop()


if __name__ == "__main__":
    main()