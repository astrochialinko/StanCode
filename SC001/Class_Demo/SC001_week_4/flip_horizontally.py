"""
File: flip_horizontally.py
Name: 
------------------------------------
This program shows how to create an empty SimpleImage
as well as making a mirrored image of poppy.png by
inserting old pixels into the blank new canvas
"""


from simpleimage import SimpleImage


def main():
    img = SimpleImage("images/poppy.png")
    img.show()

    new_img = SimpleImage.blank(img.width*2, img.height)
    for x in range(img.width):
        for y in range(img.height):

            # Original Image
            img_pixel = img.get_pixel(x, y)
            # New Image
            new_img_pixel1 = new_img.get_pixel(x, y)
            new_img_pixel2 = new_img.get_pixel(new_img.width-1-x, y)

            new_img_pixel1.red = img_pixel.red
            new_img_pixel1.green = img_pixel.green
            new_img_pixel1.blue = img_pixel.blue

            new_img_pixel2.red = img_pixel.red
            new_img_pixel2.green = img_pixel.green
            new_img_pixel2.blue = img_pixel.blue

    new_img.show()

if __name__ == '__main__':
    main()
