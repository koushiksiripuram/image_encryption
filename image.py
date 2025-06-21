import tkinter as tk
from tkinter import filedialog
from PIL import Image
from rsa import encryption, decryption
import csv

def is_csv(file_path):
    return file_path.lower().endswith('.csv')

def is_image(file_path):
    return file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(title="Select an Image")
choice = int(input("Enter 1 to encrypt and 2 to decrypt: "))

if choice == 1:
    if not is_image(file_path):
        exit()
    image = Image.open(file_path)
    image = image.convert('RGB')
    pixels = image.load()
    width, height = image.size
    with open("encrypted_pixels.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["x", "y", "r", "g", "b"])
        encrypted_image = Image.new('RGB', (width, height))
        encrypted_pixels = encrypted_image.load()
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                r_enc = encryption(r)
                g_enc = encryption(g)
                b_enc = encryption(b)
                writer.writerow([x, y, r_enc, g_enc, b_enc])
                encrypted_pixels[x, y] = (r_enc % 256, g_enc % 256, b_enc % 256)
        encrypted_image.save("encrypted_image.jpg")
        encrypted_image.show()
    print("successfully encrypted")

elif choice == 2:
    encrypted_pixels = []
    with open("encrypted_pixels.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            x = int(row[0])
            y = int(row[1])
            r = int(row[2])
            g = int(row[3])
            b = int(row[4])
            encrypted_pixels.append((x, y, r, g, b))

    image_width = max(x for x, y, r, g, b in encrypted_pixels) + 1
    image_height = max(y for x, y, r, g, b in encrypted_pixels) + 1
    new_im = Image.new('RGB', (image_width, image_height))
    pixels = new_im.load()
    for x, y, r, g, b in encrypted_pixels:
        r_dec = decryption(r)
        g_dec = decryption(g)
        b_dec = decryption(b)
        pixels[x, y] = (r_dec, g_dec, b_dec)
    print("decrypted")
    new_im.save("decrypted_image.jpg")
    new_im.show()