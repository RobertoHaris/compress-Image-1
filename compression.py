from PIL import Image

imageLue = Image.open("./person_1.jpg")

largeur, hauteur = imageLue.size
nouvelle_largeur = largeur // 2
nouvelle_hauteur = hauteur // 2
imageRedimensionnee = imageLue.resize((nouvelle_largeur, nouvelle_hauteur))

qualite = 50
imageComprimee = imageRedimensionnee.convert("RGB")
imageComprimee.save("person1_comprimee.jpg", quality=qualite)