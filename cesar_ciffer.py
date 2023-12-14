import string
def chiffrementcesar(texte_de_base, clef):
    caract_crypter=[]
    for caract in texte_de_base:
        '''
        on teste si le caratere est un alphanumerique en utilisant la fonction isalnum, 
        si oui on le chiffre en utilisant la clef
        sinon on copie le caractere tel qu'il est dans la liste des caracteres cripter, 
        l'espace n'est pas considerer comme un caracter alpha numerique
        '''
        if caract.isalnum():
            index = (string.printable.index(caract) + clef) % len(string.printable)
            carac = string.printable[index]
            caract_crypter.append(carac)
        else:
            caract_crypter.append(caract)
    texte_chiffrer="".join(caract_crypter)
    return texte_chiffrer


def dechiffrementcesar( text, clef):
     return chiffrementcesar(text, -clef)
