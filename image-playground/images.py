from PIL import Image, ImageFilter

img = Image.open('./Pokedex/profil.jpeg')
img.thumbnail((640, 764))
img.save('thumbnail.jpg')


print(img.size)