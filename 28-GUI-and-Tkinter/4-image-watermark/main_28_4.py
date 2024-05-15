from tkinter import Tk, Label, Button, filedialog
from PIL import Image
from datetime import datetime

# CONSTANTS:
IMG_ORIGINALS = "images_originals/"
IMG_EXPORTED = "images_exported/"

# Tkinter basic
window = Tk()
window.title("Watermark by @aldolammel")
window.minsize(width=500, height=300)
font_labels = ("Arial", 12, "bold")

# Label
label_select_img = Label(text="Image to include the watermarker", font=font_labels)
label_select_img.pack()  # 'pack()' method set the new component on screen


# Button
def image_selector():
    # Opening the image file with PIL method + Tkinter method (returns an object called 'img_original'):
    with Image.open(filedialog.askopenfilename()) as img_original:
        # Setting a filename based on date and time:
        str_file_name = datetime.now().strftime("%Y%m%d-%H%M%S")
        # save the original image:
        img_original.save(IMG_ORIGINALS + str_file_name + ".jpg")
        # Creating a new blank image based on the original image size:
        img_new = Image.new("RGBA", img_original.size)
        # Merging the images:
        img_new.paste(img_original)
        img_new.paste(Image.open(IMG_ORIGINALS + "_watermark.png"), (50, 50))
        # save the new image (only PNG):
        img_new.save(IMG_EXPORTED + str_file_name + ".png")


bt = Button(text="Open an image file", command=image_selector)  # button creation
bt.pack()

window.mainloop()  # keep the Tkinter window on screen
