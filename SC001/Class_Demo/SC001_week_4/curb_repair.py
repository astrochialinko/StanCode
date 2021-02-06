"""
File: curb_repair.py
Name: Chia-Lin Ko
-------------------------------
This program shows how to detect red pixels
of curb and change them into gray scale, making
the curb area be considered as an available parking space!
"""


from simpleimage import SimpleImage


#THRESHOLD = 1.3

def main():
    img = SimpleImage("images/curb.png")
    img.show()

    for pixel in img:
        avg_pixel = (pixel.red + pixel.green + pixel.blue)// 3
        if pixel.red > avg_pixel and pixel.green < avg_pixel:
            pixel.red = avg_pixel
            pixel.green = avg_pixel
            pixel.blue = avg_pixel
    img.show()





if __name__ == '__main__':
    main()
