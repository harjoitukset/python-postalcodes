# Esimerkkisuoritus:
#
# Kirjoita postitoimipaikka: Porvoo
# Postinumerot: 06100, 06101, 06150, 06151, 06200, 06400, 06401, 06450, 06500
import json


with open('postcode_map_light.json') as f:
    tiedoston_sisalto = f.read()

postinumerot = json.loads(tiedoston_sisalto)


# def postitoimipaikat(postinumerot):


etsittava = input("kirjoita postitoimipaikka: ")
listassa = False
postinrot = ""


for postinro, postitoimipaikat in postinumerot.items():
    if etsittava.upper() == str(postitoimipaikat):
        postinrot += postinro + ","
        listassa = True
        postinrot += " "
if len(postinrot) > 1:
    print(f"postinrumerot : {postinrot[:-2]}")
if listassa == False:
    print("tuntematon postitoimipaikka")
