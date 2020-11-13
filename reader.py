def main():
    filename = ("WhatsApp Chat with Imperiumin Susipeli.txt") # Korvaa omalla whatsapp group exportillasi
    kirjasto =  "*ääni"
    alt = "*Ääni"
    user = input("[DD/MM/YY]: ") # esim. 12/29/99, tai pelkällä vuosiluvulla /20.
    rfile = open(filename , mode="r")
    for line in rfile:
        if kirjasto in line:
            if user in line:
                with open("Äänet.txt", "a") as tiedosto: 
                    tiedosto.write(line)
        elif alt in line:   # Tää tulee korvata lisäämälä kirjasto and alt ylempään iffiin.
            if user in line:
                with open("Äänet.txt", "a") as tiedosto:
                    tiedosto.write(line)
main()