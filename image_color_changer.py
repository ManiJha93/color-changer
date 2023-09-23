import tkinter as tk
from PIL import Image, ImageDraw

class AdvancedColorChangerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("LED Uncle Color Changer")

        # Header
        self.header_frame = tk.Frame(self.root, bg="blue")
        self.header_label = tk.Label(self.header_frame, text="LED Uncle Color Changer", font=("Arial", 24))
        self.header_label.pack()
        self.header_frame.pack(fill="x")

        # Upload image
        self.upload_button = tk.Button(self.root, text="Upload Image", command=self.upload_image)
        self.upload_button.grid(row=1, column=0)

        # Select object
        self.select_object_button = tk.Button(self.root, text="Select Object", command=self.select_object)
        self.select_object_button.grid(row=1, column=1)

        # Color bar
        self.color_bar = tk.Scale(self.root, from_=0, to=255, orient=tk.HORIZONTAL)
        self.color_bar.grid(row=2, column=0, columnspan=2)

        # Download image
        self.download_button = tk.Button(self.root, text="Download Image", command=self.download_image)
        self.download_button.grid(row=3, column=0)

        # Image canvas
        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.grid(row=1, column=2, rowspan=3)

        # Current image
        self.current_image = None

        # Selected object
        self.selected_object = None

        # Color to change object to
        self.new_color = (0, 0, 0)

        # Footer
        self.footer_frame = tk.Frame(self.root, bg="blue")
        self.contact_now_button = tk.Button(self.footer_frame, text="Contact Now", command=self.contact_now)
        self.contact_now_button.pack()
        self.footer_frame.pack(fill="x")

        # Contact information
        self.contact_information = """
Address: 101-A, Second Floor, Shiv Kutir, Hari Nagar Ashram, Delhi 110014
Mobile: 011 26342933
Mail: info@leduncle.com
"""

        self.root.mainloop()

    def upload_image(self):
        # Get the image file path
        image_file_path = tk.filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png")])

        # Load the image
        self.current_image = Image.open(image_file_path)

        # Display the image on the canvas
        self.canvas.delete("all")
        self.canvas.image = tk.PhotoImage(self.current_image)
        self.canvas.create_image(0, 0, image=self.canvas.image, anchor="nw")

        # Enable the select object button
        self.select_object_button.config(state="normal")

    def select_object(self):
        # Get the coordinates of the selected object
        self.selected_object = self.canvas.get_rectangle()

    def change_color(self):
        # Get the new color from the color bar
        self.new_color = (self.color_bar.get(), self.color_bar.get(), self.color_bar.get())

        # Create a copy of the current image
        new_image = self.current_image.copy()

        # Draw a rectangle over the selected object with the new color
        draw = ImageDraw.Draw(new_image)
        draw.rectangle(self.selected_object, fill=self.new_color)

        # Display the new image on the canvas
        self.canvas.delete("all")
        self.canvas.image = tk.PhotoImage(new_image)
        self.canvas.create_image(0, 0,)
