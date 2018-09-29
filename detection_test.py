from PIL import Image
img = Image.open("test.jpg")
area = (350,5,100,500)
croptest = img.crop(area)
img.show()
croptest.show()