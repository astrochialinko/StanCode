"""
File: img_processing_2.py
Name: Chia-Lin Ko
-------------------------------
This file contains 2 image processing algorithms:
(1.) left_half_darken
(2.) gray_scale
"""


from simpleimage import SimpleImage


def main():
    """
    This file contains 2 image processing algorithms:
    left_half_darken and gray_scale
    """
    img = SimpleImage('images/stop.png')
    img.show()

    # half_dark_img = left_half_darken('images/stop.png')
    # half_dark_img.show()

    gray_scale_img = gray_scale('images/stop.png')
    gray_scale_img.show()


def left_half_darken(filename):
    """
    :param filename: str, the file path of the original image
    :return img: The image with half horizontal area darken
    """
    img = SimpleImage('images/stop.png')
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.get_pixel(x, y)
            if (x < img.width/2):
                pixel.red   //= 2
                pixel.green //= 2
                pixel.blue  //= 2
            else:
                pixel.red *= 2
                pixel.green *= 2
                pixel.blue *= 2
    return img


def gray_scale(filename):
    """
    :param filename: str, the file path of the
                          original colored image
    :return: Gray scaled image
    """
    gray_img = SimpleImage('images/stop.png')
    for pixel in gray_img:
        pixel = img.get_pixel(x, y)
        avg_pixel = (pixel.red + pixel.green + pixel.blue)// 3
        pixel.red = avg_pixel
        pixel.green = avg_pixel
        pixel.blue = avg_pixel

    return gray_img



if __name__ == '__main__':
    main()
