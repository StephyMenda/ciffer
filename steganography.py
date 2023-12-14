import cv2
import numpy as np
def imprimer(image_path, x, y):
    image = cv2.imread(image_path)
    pixel_value = image[y, x]

    print(f"Valeur des pixels à la position ({x}, {y}): {pixel_value}")

        # Afficher l'image avec un cercle autour du pixel sélectionné
        # cv2.circle(image, (x, y), 5, (0, 255, 0), 2)  # Dessiner un cercle autour du pixel
        #cv2.imshow('Image avec Pixel Sélectionné', image)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

# Utilisation de la fonction
#image_path = "chemin/vers/votre/image.jpg"  # Remplacez cela par le chemin de votre image
#x_position = 100
#y_position = 150
#imprimer(image_path, x_position, y_position)
def binary(texte):
    result = ''.join(format(ord(char), '08b') for char in texte)
    return result
    #une fonction pour convertir un texte en python
def convert_pixels(image_path):
    # Charger l'image à partir du fichier
    image = cv2.imread(image_path)
    image = np.floor_divide(image, 2) * 2
    return image

def encode_message(image_path, message):
    # Charger l'image à partir du fichier
    image = cv2.imread(image_path)
    message_binary=binary(message)
    image_paire=convert_pixels(image_path)
    message_integers = [int( message_binary[i:i+8], 2) for i in range(0, len( message_binary), 8)]
   # Vérifier si la longueur du message est inférieure à la moitié du nombre de pixels dans l'image
    if len(message_integers) * 2 > image.size:
        raise Exception("Le message est trop long pour être encodé dans cette image.")
    # Encoder le message dans l'image en modifiant les bits LSB
    index = 0
    for i in range(image_paire.shape[0]):
        for j in range(image_paire.shape[1]):
            for c in range(image_paire.shape[2]):
                image_paire[i, j, c] += message_integers[index % len(message_integers)] % 2
                index += 1

    # Sauvegarder l'image avec le message encodé
    cv2.imwrite('image_encodee.png', image_paire)

    print("Le message a été encodé avec succès dans l'image.")
image_path = "C:\\Users\\graci\\Documents\\image.jpeg"
message="Le soleil se leve à l'est et se couche à l'ouest"
image = cv2.imread(image_path)
encode_message(image_path,message)
cv2.imshow('Image', image)
#cv2.waitKey(0)
cv2.destroyAllWindows() 
def decode_message(image_encode_path):
    image_encode = cv2.imread(image_encode_path)
    binary_message=""
    index=0
    for i in range(image_encode.shape[0]):
        for j in range(image_encode.shape[1]):
            for c in range(image_encode.shape[2]):
                binary_message += str(image_encode[i, j, c] % 2)
                index += 1

        # Convertir le message binaire en une chaîne de texte
    message_text = ''.join([chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8)])

    print(message_text)       

path="C:\\Users\\graci\\Documents\\image_encodee.png"
decode_message(path)