import os
import shutil
from tkinter import *
from tkinter import messagebox, filedialog

class Functionality:
    def open_file():
        file_name = filedialog.askopenfilename()
        os.startfile(file_name)

    def delete_file():
        file_name = filedialog.askopenfilename()
        os.remove(file_name)
        messagebox.showinfo('delete file', file_name + ' delete successfully')

    def rename_file():
        global filename, file_name, rename_file_frame, path

        file_name = filedialog.askopenfilename()
        path = os.path.abspath(file_name)
        rename_file_frame = Frame(root)
        rename_file_frame.grid(row = 6, column = 2)
        Label(rename_file_frame, text = 'Enter the file name').grid(row = 0, column = 1, padx = 10, pady = 10)
        filename = Entry(rename_file_frame)
        filename.grid(row = 1, column = 1, padx = 10, pady = 10)
        Button(rename_file_frame, text = 'Rename file', command = Functionality.change_name).grid(row = 2, column = 1, padx = 10, pady = 10)
        Button(rename_file_frame, text = 'Cancel', command = rename_file_frame.destroy).grid(row = 2, column = 2)
        rename_file_frame.mainloop()

    def change_name():
        new_name = filename.get()
        directory = os.path.dirname(path)
        renamed = os.path.join(directory, new_name + os.path.splitext(file_name)[1])
        os.rename(path, renamed)
        rename_file_frame.destroy()
        messagebox.showinfo('rename file', file_name + ' rename successfully')

    def delete_folder():
        folder_name = filedialog.askdirectory()
        os.rmdir(folder_name)
        messagebox.showinfo('confirmation', 'Folder deleted!')

    def create_folder():
        global name_entry, dir, create_file_frame

        dir = filedialog.askdirectory()
        create_file_frame = Frame(root)
        create_file_frame.grid(row=6,column=0)
        Label(create_file_frame, text = 'Enter the folder name').grid(row = 0, column = 0, padx = 10, pady = 10)
        name_entry = Entry(create_file_frame, bd = 4,width = 25, relief = SUNKEN)
        name_entry.grid(row = 1, column = 0, padx = 10, pady = 10)
        Button(create_file_frame, text = 'create folder', font = 'bold', fg = 'white', command = Functionality.make_folder).grid(row = 2, column = 0, padx = 10, pady = 10)
        Button(create_file_frame, text = 'cancel', font = 'bold', fg = 'white', command=create_file_frame.destroy).grid(row = 2, column = 1)
        create_file_frame.mainloop()

    def make_folder():
        name = name_entry.get()
        os.chdir(dir)
        os.makedirs(name)
        create_file_frame.destroy()
        messagebox.showinfo('create folder', ' folder created successfully')

    def rename_folder():
        global dir, folder_name, rename_file_frame, path
        dir = filedialog.askdirectory()
        path = os.path.abspath(dir)
        rename_file_frame = Frame(root)
        rename_file_frame.grid(row = 6, column = 2)
        Label(rename_file_frame, text = 'Enter the folder name').grid(row = 0, column = 1, padx = 10, pady = 10)
        folder_name = Entry(rename_file_frame)
        folder_name.grid(row = 1, column = 1, padx = 10, pady = 10)
        Button(rename_file_frame, text = 'Rename folder', command = Functionality.change_folder).grid(row = 2, column = 1, padx = 10, pady = 10)
        Button(rename_file_frame, text = 'Cancel', command = rename_file_frame.destroy).grid(row = 2, column = 2)
        rename_file_frame.mainloop()

    def change_folder():
        newName = folder_name.get()
        dir = os.path.dirname(path)
        renamed = os.path.join(dir,newName)
        os.rename(path, renamed)
        rename_file_frame.destroy()
        messagebox.showinfo('rename folder', path + ' renamed successfully')

def create_button(root, text, command, width, font, row, column, pady, padx):
    return Button(root, text = text, command = command, width = width, font = font).grid(row = row, column = column, pady = pady, padx = padx)

if __name__ == '__main__':
    root = Tk()
    root.title('File manager')

    lbl_heading = Label(root, text = 'File Manager', font = ('bold', 18)).grid(row = 1, column = 1, pady = 20, padx = 20)
    
    open_btn = create_button(root, 'Open File', Functionality.open_file, 15, ('bold', 14), 2, 0, 20, 20)
    delete_btn = create_button(root, 'Delete File', Functionality.delete_file, 15, ('bold', 14), 2, 1, 20, 20)
    rename_btn = create_button(root, 'Rename File', Functionality.rename_file, 15, ('bold', 14), 2, 2, 20, 20)
    create_folder_btn = create_button(root, 'Create Folder', Functionality.create_folder, 15, ('bold', 14), 3, 0, 20, 20)
    delete_folder_btn = create_button(root, 'Delete Folder', Functionality.delete_folder, 15, ('bold', 14), 3, 1, 20, 20)
    rename_folder_btn = create_button(root, 'Rename Folder', Functionality.rename_folder, 15, ('bold', 14), 3, 2, 20, 20)
    exit_btn = create_button(root, 'Exit', root.destroy, 12, ('bold', 14), 4, 1, 20, 20)

    root.mainloop()