from PIL import Image

imageDecomprimee = Image.open("./person1_comprimee.jpg")
imageDecomprimee.show()
imageDecomprimee.save("image1_decompressee.jpg")