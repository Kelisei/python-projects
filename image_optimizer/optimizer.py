from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from ttkbootstrap import Style
from tkinter import ttk

def optimize_image(input_path, output_path, max_resolution=(3840, 2160)):
    """
    Optimize the image by resizing it if necessary and saving it as a webp file.

    Args:
        input_path (str): Path to the input image file.
        output_path (str): Path to save the optimized image.
        max_resolution (tuple): Maximum resolution for the image.
    """
    with Image.open(input_path) as img:
        if img.width > max_resolution[0] or img.height > max_resolution[1]:
            img.thumbnail(max_resolution)
        img.save(output_path, 'webp', quality=85)

def process_images(input_directory, output_directory):
    """
    Process all images in the input directory and save the optimized images to the output directory.

    Args:
        input_directory (str): Path to the directory containing input images.
        output_directory (str): Path to the directory to save optimized images.
    """
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    for filename in os.listdir(input_directory):
        if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'tiff')):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, os.path.splitext(filename)[0] + '.webp')
            optimize_image(input_path, output_path)
            print(f"Processed {filename}")

def select_input_directory():
    """
    Open a dialog to select the input directory and update the input directory entry.
    """
    input_directory = filedialog.askdirectory()
    if input_directory:
        input_dir_entry.delete(0, tk.END)
        input_dir_entry.insert(0, input_directory)

def select_output_directory():
    """
    Open a dialog to select the output directory and update the output directory entry.
    """
    output_directory = filedialog.askdirectory()
    if output_directory:
        output_dir_entry.delete(0, tk.END)
        output_dir_entry.insert(0, output_directory)

def start_optimization():
    """
    Start the image optimization process by processing images from the input directory
    and saving them to the output directory.
    """
    input_directory = input_dir_entry.get()
    output_directory = output_dir_entry.get()
    
    if not input_directory or not output_directory:
        messagebox.showerror("Error", "Please select both input and output directories.")
        return
    
    process_images(input_directory, output_directory)
    messagebox.showinfo("Info", "Image optimization completed.")

root = tk.Tk()
root.title("Image Optimizer")
root.resizable(False, False)

style = Style(theme='darkly')

style.configure("TLabel", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12))

ttk.Label(root, text="Input Directory:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
input_dir_entry = ttk.Entry(root, width=50)
input_dir_entry.grid(row=0, column=1, padx=10, pady=10)
ttk.Button(root, text="Browse", command=select_input_directory).grid(row=0, column=2, padx=10, pady=10)

ttk.Label(root, text="Output Directory:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
output_dir_entry = ttk.Entry(root, width=50)
output_dir_entry.grid(row=1, column=1, padx=10, pady=10)
ttk.Button(root, text="Browse", command=select_output_directory).grid(row=1, column=2, padx=10, pady=10)

ttk.Button(root, text="Start Optimization", command=start_optimization).grid(row=2, column=0, columnspan=3, pady=20)

root.mainloop()