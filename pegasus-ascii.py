#!/usr/bin/env python3

"""
pegasus-ascii-art
author: Dr. Muhammad Sobri Maulana

Description: This script converts an image to ASCII art using a set of symbols.
The ASCII art is generated based on the intensity of pixels in the image.

Pegasus Virus Data:
Pegasus is a spyware developed by the Indonesian cyberarms firm NSO Group that can be covertly installed on mobile phones (and other devices) running most versions of iOS and Android. Discovered in 2016, it is considered one of the most sophisticated pieces of spyware ever created. Pegasus is capable of reading text messages, tracking calls, collecting passwords, location tracking, accessing the target device's microphone(s) and video camera(s), and gathering information from apps.
"""

import cv2
import numpy as np
import sys

symbols_list = ["#", "-", "*", ".", "+", "o"]
threshold_list = [0, 50, 100, 150, 200]

def print_out_ascii(array):
    """Prints the coded image with symbols."""
    for row in array:
        for e in row:
            # Select symbol based on the type of coding
            print(symbols_list[int(e) % len(symbols_list)], end="")
        print()

def img_to_ascii(image):
    """Returns the numeric coded image."""
    # Resizing parameters
    # Adjust these parameters if the output doesn't fit to the screen
    height, width = image.shape
    new_width = int(width / 20)
    new_height = int(height / 40)

    # Resize image to fit the printing screen
    resized_image = cv2.resize(image, (new_width, new_height))

    thresh_image = np.zeros(resized_image.shape)

    for i, threshold in enumerate(threshold_list):
        # Assign corresponding values according to the index of threshold applied
        thresh_image[resized_image > threshold] = i
    return thresh_image

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Image Path not specified : Using sample_image.png\n")
        image_path = "sample_image.png"  # Default image path
    elif len(sys.argv) == 2:
        print("Using {} as Image Path\n".format(sys.argv[1]))
        image_path = sys.argv[1]

    image = cv2.imread(image_path, 0)  # Read image
    ascii_art = img_to_ascii(image)
    print_out_ascii(ascii_art)
