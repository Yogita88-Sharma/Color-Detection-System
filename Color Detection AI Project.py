#!/usr/bin/env python
# coding: utf-8

# # COLOR DETECTION 🌟

# In[2]:


import cv2
import pandas as pd
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

# Initialize Tkinter Window
root = Tk()
root.title('Color Detection App')
root.geometry("800x600")

# Global variables
df = None
img = None
img_resized = None
original_img_width = 0
original_img_height = 0

# Function to calculate the closest color name from the dataset
def get_color_name(R, G, B):
    global df
    minimum = float('inf')
    cname = ''
    
    print(f"Finding closest color for: R={R}, G={G}, B={B}")
    
    for i in range(len(df)):
        d = abs(R - df.loc[i, "R"]) + abs(G - df.loc[i, "G"]) + abs(B - df.loc[i, "B"])
        if d < minimum:
            minimum = d
            cname = df.loc[i, "Name"]
    
    print(f"Closest color: {cname}")
    return cname

# Function to open and load the CSV file with color data
def open_csv_file():
    global df
    try:
        csv_path = filedialog.askopenfilename(title="Select a CSV file", filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")))
        if csv_path:
            # Load the CSV file
            df = pd.read_csv(csv_path)

            # Parse the RGB values from the RGB column
            df[['R', 'G', 'B']] = df['RGB'].str.extract(r'rgb\((\d+),\s*(\d+),\s*(\d+)\)').astype(int)

            # Debugging: Check if the dataframe is correctly loaded
            print(df.head())  # Print first few rows of the dataframe
            
            if df is not None and not df.empty:
                label_csv.config(text=f"CSV Loaded: {csv_path.split('/')[-1]}")
                print(f"CSV Loaded successfully: {csv_path}")
            else:
                label_csv.config(text="Error: CSV file is empty or not loaded properly")
        else:
            label_csv.config(text="No CSV file selected")
    except Exception as e:
        label_csv.config(text="Error loading CSV")
        print(f"Error loading CSV: {e}")

# Function to open and display the image
def open_image():
    global img, img_resized, img_path, tk_img, original_img_width, original_img_height
    try:
        img_path = filedialog.askopenfilename(title="Select an Image", filetypes=(("Image Files", "*.jpg;*.png"), ("All Files", "*.*")))
        if img_path:
            # Open image using OpenCV
            img = cv2.imread(img_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Store original image dimensions
            original_img_height, original_img_width, _ = img.shape

            # Resize for display in Tkinter
            img_resized = cv2.resize(img, (600, 400))
            tk_img = ImageTk.PhotoImage(image=Image.fromarray(img_resized))
            
            # Display the image on the canvas
            canvas.create_image(0, 0, anchor=NW, image=tk_img)
            canvas.image = tk_img
            label_image.config(text=f"Image Loaded: {img_path.split('/')[-1]}")
        else:
            label_image.config(text="No Image file selected")
    except Exception as e:
        label_image.config(text="Error loading image")
        print(f"Error loading image: {e}")

# Function to display color information on click
def show_color(event):
    global img, img_resized, original_img_width, original_img_height
    if img_resized is not None:
        try:
            # Get the clicked position on the resized image
            x_resized, y_resized = event.x, event.y

            # Map the resized coordinates back to the original image size
            x_original = int(x_resized * original_img_width / 600)  # 600 is the canvas width
            y_original = int(y_resized * original_img_height / 400)  # 400 is the canvas height

            # Get the color of the clicked pixel in the original image
            r, g, b = img[y_original, x_original]

            # Debugging: Print the clicked pixel coordinates and RGB values
            print(f"Clicked Coordinates: ({x_original}, {y_original})")
            print(f"RGB Values at Clicked Position: ({r}, {g}, {b})")

            # Get the color name
            color_name = get_color_name(r, g, b)

            # Display the color name and RGB values
            color_info = f'Color: {color_name}  RGB: ({r}, {g}, {b})'
            label_color.config(text=color_info, bg='#%02x%02x%02x' % (r, g, b))
        except Exception as e:
            print(f"Error detecting color: {e}")

# Create buttons for opening CSV and image files
open_csv_btn = Button(root, text="Open Color CSV", command=open_csv_file)
open_csv_btn.pack(side=TOP, pady=10)

label_csv = Label(root, text="No CSV Loaded", font=('Arial', 12), width=60, height=1)
label_csv.pack(side=TOP)

open_image_btn = Button(root, text="Open Image", command=open_image)
open_image_btn.pack(side=TOP, pady=10)

label_image = Label(root, text="No Image Loaded", font=('Arial', 12), width=60, height=1)
label_image.pack(side=TOP)

# Create a label to display the color info
label_color = Label(root, text="Color Information", font=('Arial', 15), width=60, height=2)
label_color.pack(side=BOTTOM, pady=10)

# Create a canvas to display the image (ensure this is done before image handling)
canvas = Canvas(root, width=600, height=400)
canvas.pack()

# Bind the mouse click event to the canvas
canvas.bind("<Button-1>", show_color)

# Start the Tkinter event loop
root.mainloop()


# In[1]:


pip install opencv-python pandas


# In[3]:


pip install opencv-python pandas numpy pillow

