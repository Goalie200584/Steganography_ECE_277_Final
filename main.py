import embed_img.get_text as get_text 
import embed_img.img_to_binary as img_to_binary
import embed_img.embed as embed
import embed_img.save_img as save_img
import dislodge_img.convert_to_dislodge as convert_to_dislodge
import dislodge_img.uncover_binary as uncover_binary
import dislodge_img.convert_bin_to_text as convert_bin_to_text
from gui import StegApp
import tkinter as tk
if __name__ == "__main__":
    root = tk.Tk()
    app = StegApp(root)
    root.mainloop()



