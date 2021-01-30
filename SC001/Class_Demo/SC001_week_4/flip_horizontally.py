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


if __name__ == '__main__':
    main()
