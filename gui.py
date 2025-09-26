from tkinter import *
import tkinter as tk
from tkinter import filedialog
import embed_img.get_text as get_text 
import embed_img.img_to_binary as img_to_binary
import embed_img.embed as embed
import embed_img.save_img as save_img
import dislodge_img.convert_to_dislodge as convert_to_dislodge
import dislodge_img.uncover_binary as uncover_binary
import dislodge_img.convert_bin_to_text as convert_bin_to_text
import encrypt_and_decrypt
import embed_img.PSNR as PSNR

secret_key = "PYTHONRULES"
# Creates Class og StegApp to Call from main.py
class StegApp:
    # Initalizes the class StegApp; Sets up inital root, container and packs the container into our root GUI
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.root.title("Steganography Machine!")
        self.root.geometry("1000x400")

        self.file_path_var = tk.StringVar()
        self.file_path_var.set("No File Selected.")

        # Create container to hold all frames
        container = tk.Frame(root)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        # Creates a loop to make different instances of each frame class, which allows us to use different
        # functions from the main StegApp class using self.controller.{function}()
        # as well as initalize each class of a page, so we can switch the them using a button
        for F in (HomePage, chooseEncodePage, textEncodePage, fileEmbedPage, DislodgePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("HomePage")
    # Switches which frame is shown in our parent container
    def show_frame(self, page_name):
        self.file_path_var.set("No File Selected.")
        frame = self.frames[page_name]
        frame.tkraise()
    # Designed to open a filedialog from Tkinter to ask user where their file is to either encode/dislodge message
    def get_png_path(self):
        file_path = filedialog.askopenfilename(
            title="Select an Image",
            initialdir = "./images", 
            filetypes=[("PNG Files", "*.png")]
        )

        if file_path:
            self.file_path_var.set(file_path)
        
    
# Class for our HomePage when we first start our GUI window
class HomePage(tk.Frame):
    # Intializes the HomePage by packing buttons and labels; as well as intializing the controller and parent class
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Steganography Machine!")
        label.pack()
        embed_button = tk.Button(self, text="Embed Secret Message into PNG!",
                                 command=lambda:controller.show_frame("chooseEncodePage"))

        dislodge_button = tk.Button(self, text="Dislodge Secret Message from PNG!", 
                                    command=lambda: self.controller.show_frame("DislodgePage"))
        
        embed_button.pack()
        dislodge_button.pack()


#Class for our EncodeChoosePage
class chooseEncodePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        back_button = tk.Button(self, text="Back", command= lambda: self.controller.show_frame("HomePage"))
        back_button.pack(side = tk.TOP, anchor = tk.W)

        label = tk.Label(self, text="Choose The Type of File You Want to Embed")
        label.pack(pady=10, padx=10)

        text_button = tk.Button(self, text="Embed Text", command=lambda: self.controller.show_frame("textEncodePage"))
        
        PDF_button = tk.Button(self, text='Embed a PDF File', command=lambda: self.controller.show_frame("fileEmbedPage"))

        text_button.pack()
        PDF_button.pack() 


# Class for our textEncodePage
class textEncodePage(tk.Frame):
    # Intializes the textEncodePage by packing buttons, labels and a text box; as well as intializing the controller and parent class
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        back_button = tk.Button(self, text="Back", command=self.go_back)
        back_button.pack(side=tk.TOP, anchor=tk.W)

        label = tk.Label(self, text="Text Encoding Page")
        label.pack(pady=10, padx=10)
        choose_image_button = tk.Button(self, text="Choose the image you want to encode!", command = self.controller.get_png_path
        choose_image_button.pack()            

        choose_file_button = tk.Button(self, text="Choose File!", command=self.controller.get_png_path)
        choose_file_button.pack()

        
        self.file_label = tk.Label(self, textvariable=self.controller.file_path_var)
        self.file_label.pack()

        self.text_box = tk.Text(self, width = 40, height = 2)
        self.text_box.pack()
        self.text_box.insert(tk.END, "Write Your Hidden Message Here!")

        self.go_button = tk.Button(self, text="Go!", command=self.embed_secret)
        self.go_button.pack()

        self.done_label = tk.Label(self, text="Embedding Complete! Returning to HomePage")
        self.no_image_selected = tk.Label(self, text="No Image Selected!")
        self.psnr_val = ""
        

    def embed_secret(self):
        '''
        Does our embedding of our message into a PNG, does a bunc of funtions calls like we 
        would in our main file
        Inputs: N/A
        Outputs: N/A
        '''
        if self.controller.file_path_var.get() == "No File Selected.":
            self.no_image_selected.pack()
        else:
            self.no_image_selected.pack_forget()
            text = self.text_box.get("1.0", tk.END)
            text = encrypt_and_decrypt.XOR_cipher(text, secret_key)
            original_img_path = self.controller.file_path_var.get()
            text_bin, text_length = get_text.convert_text_to_binary(text)
            num_of_rows, img_bin = img_to_binary.convert_img_to_binary(original_img_path, text_length)   
            img_bin = embed.embed_message(text_bin, img_bin)
            img_output_path = save_img.save_img(original_img_path, img_bin)

            self.psnr_val = PSNR.get_psnr(original_img_path, img_output_path)
            self.psnr_val = f"PSNR Value of: {round(self.psnr_val, 2)}%"

            self.PSNR_lab = tk.Label(self, text=self.psnr_val)
            
            self.PSNR_lab.pack()
            self.done_label.pack()
            self.after(3000, self.finish_embedding)

    
    def finish_embedding(self):
        '''
        Finishes Embedding after waiting a specified amount of time using self.after()
        Inputs: N/A
        Outputs: N/A 
        '''
        self.done_label.pack_forget()
        self.PSNR_lab.pack_forget()
        self.controller.show_frame("HomePage")

    def go_back(self):
        self.controller.show_frame("chooseEncodePage")
        self.no_image_selected.pack_forget()


class fileEmbedPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.no_file_selected = tk.Label(self, text="No File Selected!!")

        back_button = tk.Button(self, text = "Back", command=self.go_back)
        back_button.pack(side=tk.TOP, anchor=tk.W)

        label = tk.Label(self, text="Embed a File! -> Supported files: *.pdf")
        label.pack(pady=10, padx=10)

        choose_file_button = tk.Button(self, text="Choose a File to Embed", command=self.choose_file)
        choose_file_button.pack()
        self.embed_file_path = tk.StringVar()
        self.embed_file_path.set("No File Selected.")
        fileLabel = tk.Label(self, textvariable=self.embed_file_path)
        fileLabel.pack()

        go_button = tk.Button(self, text="Go!", command=self.fileEmbed)
        go_button.pack()

    
    def choose_file(self):
        file_path = filedialog.askopenfilename(
            title="Select a File",
            initialdir = "./", 
            filetypes=[("PDF Files", "*.pdf")]
        )

        if file_path:
            self.embed_file_path.set(file_path)


    def fileEmbed(self):
        if self.embed_file_path.get() == "No File Selected.":
            self.no_file_selected.pack()
        else:
            self.embed_file_path.pack_forget()
    def go_back(self):
        self.no_file_selected.pack_forget()
        self.controller.show_frame("chooseEncodePage")


#Class for DislodgePage
class DislodgePage(tk.Frame):
    # Intializes the DislodgePage by packing buttons and labels; as well as intializing the controller and parent class
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.dislodged_message = tk.StringVar()
        
        back_button = tk.Button(self, text="Back", command=self.go_back)
        back_button.pack(side=tk.TOP, anchor=tk.W)

        label = tk.Label(self, text="Dislodge Page")
        label.pack()
        
        choose_file_button = tk.Button(self, text="Choose File!", command=self.controller.get_png_path)
        choose_file_button.pack()

        
        file_label = tk.Label(self, textvariable=self.controller.file_path_var)
        file_label.pack()
        
        go_button = tk.Button(self, text="Go!", command=self.dislodge_secret)
        go_button.pack()

        self.no_image_selected = tk.Label(self, text="No Image Selected!")

        self.decoded_message_label = tk.Label(self, textvariable=self.dislodged_message)
        self.decoded_message_label.pack_forget()

    def dislodge_secret(self):
        '''
        Begins our dislodging sequence that we would see in our main file, by calling 
        multiple different functions
        Inputs: N/A
        Outputs: dislodged_message
        '''
        if self.controller.file_path_var.get() == "No File Selected.":
            self.no_image_selected.pack()
        else:
            self.no_image_selected.pack_forget()
            dislodge_path = self.controller.file_path_var.get()
            img_bin_decode = convert_to_dislodge.convert_img_to_binary(dislodge_path)
            bin_text = uncover_binary.uncover_info(img_bin_decode)
            decoded_message = convert_bin_to_text.convert_to_text(bin_text)
            decoded_message = encrypt_and_decrypt.XOR_cipher(decoded_message, secret_key)

            self.dislodged_message.set(f"Decoded Message: {decoded_message}")
            self.decoded_message_label.pack()

    
    def go_back(self):
        self.controller.show_frame("HomePage")
        self.no_image_selected.pack_forget()