"""
File: img_processing_2.py
Name:
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

    half_dark_img = left_half_darken('images/stop.png')
    half_dark_img.show()

    # gray_scale_img = gray_scale('images/stop.png')
    # gray_scale_img.show()


def left_half_darken(filename):
    """
    :param filename: str, the file path of the original image
    :return img: The image with half horizontal area darken
    """
    pass


def gray_scale(filename):
    """
    :param filename: str, the file path of the
                          original colored image
    :return: Gray scaled image
    """
    pass


if __name__ == '__main__':
    main()
