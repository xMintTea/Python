import os
import os.path
from tkinter import *
from tkinter.filedialog import askdirectory
import shutil
from tkinter import ttk

def calc_files(path: str) -> tuple:
    files = []
    dirs = []
    for i in os.listdir(path):
        i = f'{path}/{i}'
        if os.path.isdir(i):
            dirs.append(i)
        else:
            files.append(i)
    
    return (len(files), len(dirs))


def choose_path() -> None:
    global selected_path
    selected_path = askdirectory()

    files, dirs = calc_files(selected_path)

    path_label.config(text=f"Текущий путь: {selected_path}")
    file_count_label.config(text=f'Количество файлов: {files}\nКоличество папок: {dirs}')

    path_label.update()
    file_count_label.update()



def start_sort() -> None:
    global selected_path
    global mode
    if mode == "0":
        mode_one(selected_path)
    else:
        mode_two(selected_path)

def mode_one(path) -> None:
    for i in os.listdir(path):
        if os.path.isfile(f'{path}/{i}'):
            ext = i[i.rindex('.')+1:]
            if os.path.exists(f'{path}/{ext.upper()}'):
                shutil.move(f'{path}/{i}',f'{path}/{ext.upper()}/{i}')
            else:
                os.mkdir(f'{path}/{ext.upper()}')
                shutil.move(f'{path}/{i}',f'{path}/{ext.upper()}/{i}')


def mode_two(path) -> None:
    for check_path, founded_folders, files in os.walk(path):
        for i in range(len(files)):
            if not os.path.exists(f'{path}/{files[i]}'):
                shutil.move(f'{check_path}/{files[i]}',path)
        
        if len(files)+len(founded_folders) == 0:
            os.rmdir(check_path)



    for i in os.listdir(path):
        if os.path.isfile(f'{path}/{i}'):
            ext = i[i.rindex('.')+1:]
            if os.path.exists(f'{path}/{ext.upper()}'):
                shutil.move(f'{path}/{i}',f'{path}/{ext.upper()}/{i}')
            else:
                os.mkdir(f'{path}/{ext.upper()}')
                shutil.move(f'{path}/{i}',f'{path}/{ext.upper()}/{i}')


root = Tk()
root.title('File Sorter')
root.geometry('700x600')

selected_path = 'ВЫБЕРИТЕ ПУТЬ'

path_label = Label(root, text=f"Текущий путь: {selected_path}", font=("Arial",20),fg="#101010", )
path_label.pack()

file_count_label = Label(root, text='Количество файлов: 0\nКоличество папок: 0',font=("Arial",30),fg="#101010")
file_count_label.pack()

mode = StringVar(value='0')
first_mode = ttk.Radiobutton(value='0',variable=mode, text='Сортировать только выбранную папку').pack()
second_mode = ttk.Radiobutton(value='1', variable=mode, text='Сортировать файлы в папках').pack()

selector = Button(root, text="Выбрать путь для сортировки", command=choose_path,font=("Arial",20),fg="#101010")
selector.pack()

sort_button = Button(root, text="Сортировать", command=start_sort, font=("Arial",20),fg="#101010")
sort_button.pack()

root.mainloop()