import json
import os
from os.path import exists
import shutil


#REGLAGES IMPORTANTS

# Variables de réglages
addon_name = "EA_Soundboard"
sounds_folder = "Sounds"

# Variables d'imports
import_folder = "import"
player_sound_folder = "player"
sound_500m = "500m"
sound_1000m = "1000m"
sound_1500m = "1500m"
sound_2000m = "2000m"
sound_2500m = "2500m"
sound_3000m = "3000m"
sound_5000m = "5000m"
sound_10000m = "10000m"

# Variables d'exports
export_folder = "generated"
nom_export_player_cpp = "conf-generated-player.cpp"
nom_profile_json = "profile-conf.json"


def generator():
    # Vérification si le dossier d'import existe
    if os.path.exists(import_folder + "\\") == False:
        os.mkdir(import_folder + "\\")
    if os.path.exists(import_folder + "\\" + player_sound_folder + "\\") == False:
        os.mkdir(import_folder + "\\" + player_sound_folder + "\\")

    # Vérification si le dossier d'export existe
    if os.path.exists(export_folder + "\\") == False:
        os.mkdir(export_folder + "\\")

    # Suppression du fichier cpp est déjà existant
    if exists(export_folder + "\\" + nom_export_player_cpp):
        os.remove(export_folder + "\\" + nom_export_player_cpp)
        print("[Generator] Suppression de l\"ancien " + nom_export_player_cpp)

    # Listing de tous les sons du fichier Sounds
    file_list_player = os.listdir(import_folder + "\\" + player_sound_folder + "\\")

    # Information si il n'y a pas de sound
    if not file_list_player:
        print("")
        print("")
        print("==================================================")
        print("Aucun sons ne se trouve dans le fichier d\'import.")
        print("")
        print("Placez dans le dossier \"" + import_folder + "/" + player_sound_folder +"\" les sons")
        print(".OGG jouables sur les JOUEURS.")
        print("")
        print("Vous trouverez une fois généré les fichiers dans")
        print("le dossier \""+ export_folder + "\"")
        print("                                          EA - Ted")
        print("==================================================")
        print("")
        print("")
        input("Appuyez sur n'importe quelle touche pour quitter...")
        return

    # Génération du fichier CPP
    for files in file_list_player:
        with open(export_folder + "\\" + nom_export_player_cpp, "a") as f:
            f.writelines("\n" + "class " + files[:-4] + " : default")
            f.writelines("\n" + "{")
            f.writelines("\n" + "    sound[]=")
            f.writelines("\n" + "        {")
            f.writelines("\n" + "            \"\\" + addon_name + "\\" + sounds_folder + "\\" + files[:-4] + "\",")
            f.writelines("\n" + "            1,")
            f.writelines("\n" + "            1,")
            f.writelines("\n" + "            1000};")
            f.writelines("\n" + "};")
    print("")
    print("")
    print("==================================================")
    print("Config de " + str(len(file_list_player)) + " sons de joueur générés.")

    # Génération du fichier profile-conf.json
    SoundsLists = {}
    Sounds = []
    for files in file_list_player:
        Sounds.append(files[:-4])
        SoundsLists["SoundsLists"] = Sounds
    with open(export_folder + "\\" + nom_profile_json, "w") as write_file:
        json.dump(SoundsLists, write_file, indent=4, sort_keys=True)
    print("Fichier profil de " + str(len(file_list_player)) + " sons générés.")
    print("==================================================")
    print("")
    print("")

    # Génération du fichier de son à coordonnée 500m
    if os.path.exists(import_folder + "\\" + player_sound_folder + "\\") == False:
        os.mkdir(import_folder + "\\" + player_sound_folder + "\\")
        
    file_list_500m = os.listdir(import_folder + "\\" + player_sound_folder + "\\")

    for files in file_list_player:
        with open(export_folder + "\\" + nom_export_player_cpp, "a") as f:
            f.writelines("\n" + "class " + files[:-4] + " : default")
            f.writelines("\n" + "{")
            f.writelines("\n" + "    sound[]=")
            f.writelines("\n" + "        {")
            f.writelines("\n" + "            \"\\" + addon_name + "\\" + sounds_folder + "\\" + files[:-4] + "\",")
            f.writelines("\n" + "            1,")
            f.writelines("\n" + "            1,")
            f.writelines("\n" + "            1000};")
            f.writelines("\n" + "};")


    # Génération du fichier de son à coordonnée 1000m

    # Génération du fichier de son à coordonnée 1500m

    # Génération du fichier de son à coordonnée 2000m

    # Génération du fichier de son à coordonnée 2500m

    # Génération du fichier de son à coordonnée 3000m

    # Génération du fichier de son à coordonnée 5000m

    # Génération du fichier de son à coordonnée 10000m

    # Vérification si le dossier Sound existe
    if os.path.exists(sounds_folder + "\\") == False:
        os.mkdir(sounds_folder + "\\")

    # Copie des sons dans le dossier sound
    for files in file_list_player:
        shutil.copyfile(import_folder + "\\" + player_sound_folder + "\\" + files, sounds_folder + "\\" + files)
    
    remover()
    
def remover(): 
    error_question = False

    # Demande de suppression
    print("")
    print("")
    print("==================================================")
    question1 = input("Voulez vous supprimer le dossier d'Import? Y ou N :")
    question2 = input("Voulez vous supprimer le dossier d'Export? Y ou N :")
    print("==================================================")
    print("")
    print("")
    print("")
    print("")
    print("==================================================")
    if question1 == "Y" or question1 == "y":
        if os.path.exists(import_folder + "\\") == True:
            shutil.rmtree(import_folder)
            print("Vous avez ACCEPTÉ la suppression des Imports.")
        else:
            print("Le fichier des Imports n'existait déjà plus.")
    elif question1 == "N" or question1 == "n": 
        print("Vous avez REFUSÉ la suppression des Imports.")
    else:
        error_question = True

    if question2 == "Y" or question2 == "y":
        if os.path.exists(export_folder + "\\") == True:
            shutil.rmtree(export_folder)
            print("Vous avez ACCEPTÉ la suppression des Exports.")
        else:
            print("Le fichier des Exports n'existait déjà plus.")
    elif question2 == "N" or question2 == "n": 
        print("Vous avez REFUSÉ la suppression des Exports.")    
    else:
        error_question = True

    if error_question == True:
        print("Vous avez fait une erreur, veuillez recommencer.")
        print("==================================================")
        remover()
        return

    print("==================================================")
    print("")
    print("")
    
    input("Appuyez sur n'importe quelle touche pour quitter...")


generator()
