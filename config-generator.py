import json
import os
from os.path import exists
from tracemalloc import stop


def generator():

    #REGLAGES IMPORTANTS
    #IMPORTANT!!! Dossier dans lequel l'addon se trouve!
    work_folder = "addons"

    # Variables de réglages
    addon_name = "EA_Soundboard"
    sounds_file = "Sounds"

    # Variables d'imports
    import_folder = "import"
    player_sound_folder = "player"

    # Variables d'exports
    export_folder = "generated"
    nom_export_player_cpp = "conf-generated-player.cpp"
    nom_profile_json = "profile-conf.json"


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

    if not file_list_player:
        print("Aucun sons ne se trouve dans le fichier d\'import.")
        return

    # Génération du fichier CPP
    for files in file_list_player:
        with open(export_folder + "\\" + nom_export_player_cpp, "a") as f:
            f.writelines("\n" + "class " + files[:-4] + " : default")
            f.writelines("\n" + "{")
            f.writelines("\n" + "    sound[]=")
            f.writelines("\n" + "        {")
            f.writelines("\n" + "            \"\\" + addon_name + "\\" + sounds_file + "\\" + files[:-4] + "\",")
            f.writelines("\n" + "            1,")
            f.writelines("\n" + "            1,")
            f.writelines("\n" + "            1000};")
            f.writelines("\n" + "};")
    print("Config de " + str(len(file_list_player)) + " sons de joueur généré.")

    # Génération du fichier profile-conf.json
    SoundsLists = {}
    Sounds = []
    for files in file_list_player:
        Sounds.append(files[:-4])
        SoundsLists["SoundsLists"] = Sounds
    with open(export_folder + "\\" + nom_profile_json, "w") as write_file:
        json.dump(SoundsLists, write_file, indent=4, sort_keys=True)
    print("Fichier profil de " + str(len(file_list_player)) + " sons généré.")


generator()
