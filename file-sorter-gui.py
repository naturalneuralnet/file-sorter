import customtkinter

import tkinter as tk

from tkinter import font as tkFont

from tkinter.messagebox import showerror, showwarning, showinfo

import os, shutil

# Think I can just turn this into an exe and use it that way?

# No need to make it into an installer?

  

# https://www.youtube.com/watch?v=iM3kjbbKHQU

# set color scheme

customtkinter.set_appearance_mode("dark")

  

customtkinter.set_default_color_theme("green")

  

root = customtkinter.CTk()

root.maxsize(700, 650)

root.title("File Sorter")

# root.config(bg="black")

# options = {"bg": "black"}

def file_sorter():

    path = folder_name.get()

   
    if not path:

       

        label4 = customtkinter.CTkLabel(master=frame, text="Please enter a file path!", font=("Courier", 14), text_color="red")

        label4.grid(row=5, column=0, pady=12, padx=10)

    else:

        print(path)

        path = path + "/"

        file_name = os.listdir(path)

       
        isEpub = epub_check.get()

        isPDF = pdf_check.get()

        isPNG = png_check.get()

        isJPG = jpg_check.get()

        isExe = exe_check.get()

  

        folder_names = []

        if isEpub:

            folder_names.append("epub files")

        elif isPDF:

            folder_names.append("pdf files")

        elif isPNG:

            folder_names.append("png files")

        elif isJPG:

            folder_names.append("jpg files") 

        elif isExe:

            folder_names.append("exe files")

  
  
  
 # are there folders already?

        # check if the folders for different files exist if not create them

    for name in range(len(folder_names)):

        if not os.path.exists(path + folder_names[name]):

            os.mkdir((path + folder_names[name]))

       
  

# # then move those files to the correct folder


        moved_types = []

        for file in file_name:

            if ".png" in file and not os.path.exists(path + "png files/" + file) and isPNG:

                shutil.move(path + file, path + "png files/")

                moved_types.append("png files")

            elif ".jpg" in file and not os.path.exists(path + "jpg files/" + file) and isJPG:

                shutil.move(path + file, path + "jpg files/")

                moved_types.append("jpg files")

            elif ".pdf" in file and not os.path.exists(path + "pdf files/" + file) and isPDF:

                shutil.move(path + file, path + "pdf files/")

                moved_types.append("pdf files")

            elif ".epub" in file and not os.path.exists(path + "epub files/" + file) and isEpub:

                shutil.move(path + file, path + "epub files/")

                moved_types.append("epub files")

            elif ".exe" in file and not os.path.exists(path + "exe files/" + file) and isExe:

                shutil.move(path + file, path + "exe files/")

                moved_types.append("exe files")

        else:

            print("There are files in this path that were not moved!")

            print(moved_types)

            for types in moved_types:

                    print(f"Only {types} were sorted.")

                    label5 = customtkinter.CTkLabel(master=frame, text=f"Only {types} sorted!", text_color="white", font=("Courier", 14))

                    label5.grid(row=5, column=0, pady=12, padx=10)

        label5 = customtkinter.CTkLabel(master=frame, text=f"Files in {path} sorted!", text_color="white",font=("Courier", 14))
        
        label5.grid(row=5, column=0, pady=12, padx=10)

       

  
  

frame = customtkinter.CTkFrame(master=root, width=600, height=600)

frame.grid(row=0, column=0, padx=10, pady=10)

  

label= customtkinter.CTkLabel(master=frame, text="File Sorter", font=("Courier", 24) )

label.grid(row=1, column=0, pady=12, padx=10)

  

label2= customtkinter.CTkLabel(master=frame, text="Enter the full path of the folder you want sorted", font=("Courier", 14))

label2.grid(row=2, column=0, pady=12, padx=10)

  


  

folder_name = customtkinter.CTkEntry(width=140, master=frame)

folder_name.grid(row=3, column=0, pady=12, padx=10)

path = folder_name.get()

  
  

label3= customtkinter.CTkLabel(master=frame, text="Check which file types you wish to sort", font=("Courier", 14))

label3.grid(row=4, column=0, pady=12, padx=10)

  

checkbox_frame = customtkinter.CTkFrame(master=frame, width=300, height=300)

checkbox_frame.grid(row=6, column=0, padx=10, pady=10)

  

check_font = customtkinter.CTkFont(family='Courier', size=13, )

epub_check = customtkinter.CTkCheckBox(master=checkbox_frame, text=".epub?", font=check_font)

epub_check.grid(row=7, column=0, pady=1, padx=3 ,sticky='w' +'e' +'n' + 's')

pdf_check = customtkinter.CTkCheckBox(master=checkbox_frame, text=".pdf?", font=check_font)

pdf_check.grid(row=7, column=1, pady=1, padx=3, sticky='w' +'e' +'n' + 's')

png_check = customtkinter.CTkCheckBox(master=checkbox_frame, text=".png?", font=check_font)

png_check.grid(row=8, column=0, pady=1, padx=3, sticky='w' +'e' +'n' + 's')

zip_check = customtkinter.CTkCheckBox(master=checkbox_frame, text=".zip?", font=check_font)

zip_check.grid(row=8, column=1, pady=1, padx=3, sticky='w' +'e' +'n' + 's')

jpg_check = customtkinter.CTkCheckBox(master=checkbox_frame, text=".jpg?" ,font=check_font)

jpg_check.grid(row=9, column=0, pady=1, padx=3, sticky='w' +'e' +'n' + 's')

exe_check = customtkinter.CTkCheckBox(master=checkbox_frame, text=".exe?", font=check_font)

exe_check.grid(row=9, column=1, pady=1, padx=3, sticky='w' +'e' +'n' + 's')

  

sort_button = customtkinter.CTkButton(master=frame, text="Sort", command=file_sorter, font=check_font)

sort_button.grid(row=10, column=0, pady=10, padx=10, sticky='w' +'e' +'n' + 's')

  

root.mainloop()

  

