# Color Detection App

This is a Python-based **Color Detection Tool** that allows users to upload an image, click on any pixel within the image, and get information about the closest color match from a predefined CSV file containing RGB values and color names.

## Features
- **Image Upload**: Upload any image file (JPG, PNG) using a GUI built with Tkinter.
- **Color Detection**: Click on any pixel in the image, and the app will display the color name and RGB values.
- **CSV-Based Color Matching**: The tool matches the clicked pixel's color to the closest predefined color in the CSV file (`color_srgb.csv`).
- **Responsive Design**: Automatically resizes the image for the app window, while maintaining the ability to detect the original pixel's color.

## Demo
Here's how the application looks and functions:
- Upload an image:
  - Click on any part of the image to detect its color.
  - View the color name and its corresponding RGB values.

## Technologies Used
- **Python**: Core language for the project.
- **OpenCV**: For image loading, processing, and color detection.
- **Pandas**: To load and parse the CSV file containing color data.
- **Tkinter**: To build the graphical user interface (GUI).
- **Pillow**: For converting images to a format suitable for Tkinter.

## Installation

### Prerequisites
Ensure you have Python 3.x installed. You can download it from [Python's official site](https://www.python.org/).

### 1. Clone the Repository
You can clone this project by running the following command in your terminal or command prompt:

```bash
git clone https://github.com/Yogita88-Sharma/Color-Detection-System.git

