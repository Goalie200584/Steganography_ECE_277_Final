from tkinter import *
import tkinter as tk
from tkinter import filedialog

#Creates Class og StegApp to Call from main.py
class StegApp:
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.root.title("Steganography Machine!")
        self.root.geometry("500x300")

        self.file_path_var = tk.StringVar()
        self.file_path_var.set("No File Selected.")

        #Create container to hold all frames
        container = tk.Frame(root)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, EncodePage, DislodgePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def get_png_path(self):
        file_path = filedialog.askopenfilename(
            title="Select an Image",
            initialdir = "./", 
            filetypes=[("PNG Files", "*.png")]
        )

        if file_path:
            self.file_path_var.set(file_path)
        
    

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Steganography Machine!")
        label.pack()
        embed_button = tk.Button(self, text="Embed Secret Message into PNG!",
                                 command=lambda:controller.show_frame("EncodePage"))

        dislodge_button = tk.Button(self, text="Dislodge Secret Message from PNG!", 
                                    command=lambda: self.controller.show_frame("DislodgePage"))
        
        embed_button.pack()
        dislodge_button.pack()



class EncodePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Encode Page")
        label.pack(pady=10, padx=10)

        choose_file_button = tk.Button(self, text="Choose File!", command=self.controller.get_png_path)
        choose_file_button.pack()

        self.controller.file_path_var.set("No File Selected.")
        self.file_label = tk.Label(self, text=self.controller.file_path_var)
        self.file_label.pack()

        go_button = tk.Button(self, text="Go!", command=self.embed_secret)
        go_button.pack()

    def embed_secret(self):
        if self.file_path_var == "No file selected.":
            pass
        else:
            pass

class DislodgePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Dislodge Page")
        label.pack()

        choose_file_button = tk.Button(self, text="Choose File!", command=self.controller.get_png_path)
        choose_file_button.pack()

        self.controller.file_path_var.set("No File Selected.")
        file_label = tk.Label(self, text=self.controller.file_path_var)
        file_label.pack()
        
        go_button = tk.Button(self, text="Go!", command=self.dislodge_secret)
        go_button.pack()

    def dislodge_secret(self):
        if self.file_path_var == "No file selected.":
            pass
        else:
            pass
