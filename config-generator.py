from copy import copy
from glob import glob
import json
import os
from os.path import exists
import shutil
import string


#REGLAGES IMPORTANTS

# Variables de reglages
addon_name = "EA_Soundboard"
sounds_folder = "Sounds"

# Variables d'imports
import_folder = "import"
player_sound_folder = "player"
sound_dist_1 = "250"
sound_dist_2 = "500"
sound_dist_3 = "1000"
sound_dist_4 = "75"
sound_dist_5 = "100"
sound_dist_6 = "125"
sound_dist_7 = "150"
sound_dist_8 = "175"
sound_dist_9 = "200"

# Variables d'exports
export_folder = "generated"
nom_export_player_cpp = "conf-generated-player.cpp"
nom_export_dist_1_cpp = "conf-generated-dist_1.cpp"
nom_export_dist_2_cpp = "conf-generated-dist_2.cpp"
nom_export_dist_3_cpp = "conf-generated-dist_3.cpp"
nom_export_dist_4_cpp = "conf-generated-dist_4.cpp"
nom_export_dist_5_cpp = "conf-generated-dist_5.cpp"
nom_export_dist_6_cpp = "conf-generated-dist_6.cpp"
nom_export_dist_7_cpp = "conf-generated-dist_7.cpp"
nom_export_dist_8_cpp = "conf-generated-dist_8.cpp"
nom_export_dist_9_cpp = "conf-generated-dist_9.cpp"

nom_profile_json = "profile-conf.json"

# Activation des exports
enable_export_player_cpp = True
enable_export_distance_1_cpp = True
enable_export_distance_2_cpp = True
enable_export_distance_3_cpp = True
enable_export_distance_4_cpp = True
enable_export_distance_5_cpp = True
enable_export_distance_6_cpp = True
enable_export_distance_7_cpp = True
enable_export_distance_8_cpp = True
enable_export_distance_9_cpp = True
enable_export_profile_json = True

def init():
    check_import()
    check_export()
    cpp_remove()
    listing_sounds()
    notification()
    if (enable_export_player_cpp == True): export_player_cpp()
    if (enable_export_distance_1_cpp == True): export_distance_1_cpp()
    if (enable_export_distance_2_cpp == True): export_distance_2_cpp()
    if (enable_export_distance_3_cpp == True): export_distance_3_cpp()
    if (enable_export_distance_4_cpp == True): export_distance_4_cpp()
    if (enable_export_distance_5_cpp == True): export_distance_5_cpp()
    if (enable_export_distance_6_cpp == True): export_distance_6_cpp()
    if (enable_export_distance_7_cpp == True): export_distance_7_cpp()
    if (enable_export_distance_8_cpp == True): export_distance_8_cpp()
    if (enable_export_distance_9_cpp == True): export_distance_9_cpp()
    if (enable_export_profile_json == True): export_profile_json()
    copy()
    if (first_import == False and first_export == False): remover()


def check_import():
    # ==========================================
    # Verification si le dossier d'import existe
    # ==========================================
    global first_import
    first_import = False
    
    #import\
    if os.path.exists(import_folder + "\\") == False:
        os.mkdir(import_folder + "\\")
        first_import = True
        
    #import\player
    if os.path.exists(import_folder + "\\" + player_sound_folder + "\\") == False:
        os.mkdir(import_folder + "\\" + player_sound_folder + "\\")
        
    #import\dist_1
    if os.path.exists(import_folder + "\\" + sound_dist_1 + "\\") == False:
        os.mkdir(import_folder + "\\" + sound_dist_1 + "\\")
        
    #import\dist_2
    if os.path.exists(import_folder + "\\" + sound_dist_2 + "\\") == False:
        os.mkdir(import_folder + "\\" + sound_dist_2 + "\\")
    
    #import\dist_3
    if os.path.exists(import_folder + "\\" + sound_dist_3 + "\\") == False:
        os.mkdir(import_folder + "\\" + sound_dist_3 + "\\")
    
    #import\dist_4
    if os.path.exists(import_folder + "\\" + sound_dist_4 + "\\") == False:
        os.mkdir(import_folder + "\\" + sound_dist_4 + "\\")
        
    #import\dist_5
    if os.path.exists(import_folder + "\\" + sound_dist_5 + "\\") == False:
        os.mkdir(import_folder + "\\" + sound_dist_5 + "\\")
        
    #import\dist_6
    if os.path.exists(import_folder + "\\" + sound_dist_6 + "\\") == False:
        os.mkdir(import_folder + "\\" + sound_dist_6 + "\\")
        
    #import\dist_7
    if os.path.exists(import_folder + "\\" + sound_dist_7 + "\\") == False:
        os.mkdir(import_folder + "\\" + sound_dist_7 + "\\")
        
    #import\dist_8
    if os.path.exists(import_folder + "\\" + sound_dist_8 + "\\") == False:
        os.mkdir(import_folder + "\\" + sound_dist_8 + "\\")
        
    #import\dist_9
    if os.path.exists(import_folder + "\\" + sound_dist_9 + "\\") == False:
        os.mkdir(import_folder + "\\" + sound_dist_9 + "\\")


def check_export():
    # ==========================================
    # Verification si le dossier d'export existe
    # ==========================================
    global first_export
    first_export = False
    
    #export\
    if os.path.exists(export_folder + "\\") == False:
        os.mkdir(export_folder + "\\")
        first_export = True
    else:
        print("Attention en relancant un export vos fichiers CPP seront tous supprimes!")
        print("")
        input("Appuyez sur n'importe quelle touche pour continuer...")

def cpp_remove():
    # ==========================================
    # Suppression du fichier cpp est deja existant
    # ==========================================
    
    #Player
    if exists(export_folder + "\\" + nom_export_player_cpp):
        os.remove(export_folder + "\\" + nom_export_player_cpp)
        print("[Notification] Suppression de l'ancien " + nom_export_player_cpp)
    
    #Dist_1
    if exists(export_folder + "\\" + nom_export_dist_1_cpp):
        os.remove(export_folder + "\\" + nom_export_dist_1_cpp)
        print("[Notification] Suppression de l'ancien " + nom_export_dist_1_cpp)
        
    #Dist_2
    if exists(export_folder + "\\" + nom_export_dist_2_cpp):
        os.remove(export_folder + "\\" + nom_export_dist_2_cpp)
        print("[Notification] Suppression de l'ancien " + nom_export_dist_2_cpp)
    
    #Dist_3
    if exists(export_folder + "\\" + nom_export_dist_3_cpp):
        os.remove(export_folder + "\\" + nom_export_dist_3_cpp)
        print("[Notification] Suppression de l'ancien " + nom_export_dist_3_cpp)
    
    #Dist_4
    if exists(export_folder + "\\" + nom_export_dist_4_cpp):
        os.remove(export_folder + "\\" + nom_export_dist_4_cpp)
        print("[Notification] Suppression de l'ancien " + nom_export_dist_4_cpp)
    
    #Dist_5
    if exists(export_folder + "\\" + nom_export_dist_5_cpp):
        os.remove(export_folder + "\\" + nom_export_dist_5_cpp)
        print("[Notification] Suppression de l'ancien " + nom_export_dist_5_cpp)
    
    #Dist_6
    if exists(export_folder + "\\" + nom_export_dist_6_cpp):
        os.remove(export_folder + "\\" + nom_export_dist_6_cpp)
        print("[Notification] Suppression de l'ancien " + nom_export_dist_6_cpp)
    
    #Dist_7
    if exists(export_folder + "\\" + nom_export_dist_7_cpp):
        os.remove(export_folder + "\\" + nom_export_dist_7_cpp)
        print("[Notification] Suppression de l'ancien " + nom_export_dist_7_cpp)
    
    #Dist_8
    if exists(export_folder + "\\" + nom_export_dist_8_cpp):
        os.remove(export_folder + "\\" + nom_export_dist_8_cpp)
        print("[Notification] Suppression de l'ancien " + nom_export_dist_8_cpp)
    
    #Dist_9
    if exists(export_folder + "\\" + nom_export_dist_9_cpp):
        os.remove(export_folder + "\\" + nom_export_dist_9_cpp)
        print("[Notification] Suppression de l'ancien " + nom_export_dist_9_cpp)
    
def listing_sounds():
    # ==========================================
    # Listing de tous les sons du fichier Sounds
    # ==========================================
    global need_export
    
    
    #Player
    global file_list_player
    global listing_player
    
    file_list_player = os.listdir(import_folder + "\\" + player_sound_folder + "\\")
    if not file_list_player:
        listing_player = "Placez dans le dossier \"" + import_folder + "/" + player_sound_folder +"\" les sons.OGG jouables sur les JOUEURS." 
    else:
        listing_player = "Il y a " + str(len(file_list_player)) + " son de joueurs."
        
    #Dist_1
    global file_list_1
    global listing_1
    
    file_list_1 = os.listdir(import_folder + "\\" + sound_dist_1 + "\\")
    if not file_list_1:
        listing_1 = "Placez dans le dossier \"" + import_folder + "/" + sound_dist_1 +"\" les sons.OGG d'objets avec " + sound_dist_1 + "m de distance." 
    else:
        listing_1 = "Il y a " + str(len(file_list_1)) + " son de " + sound_dist_1 + "m."
        
    #Dist_2
    global file_list_2
    global listing_2
    
    file_list_2 = os.listdir(import_folder + "\\" + sound_dist_2 + "\\")
    if not file_list_2:
        listing_2 = "Placez dans le dossier \"" + import_folder + "/" + sound_dist_2 +"\" les sons.OGG d'objets avec " + sound_dist_2 + "m de distance." 
    else:
        listing_2 = "Il y a " + str(len(file_list_2)) + " son de " + sound_dist_2 + "m."
    
    #Dist_3
    global file_list_3
    global listing_3
    
    file_list_3 = os.listdir(import_folder + "\\" + sound_dist_3 + "\\")
    if not file_list_3:
        listing_3 = "Placez dans le dossier \"" + import_folder + "/" + sound_dist_3 +"\" les sons.OGG d'objets avec " + sound_dist_3 + "m de distance." 
    else:
        listing_3 = "Il y a " + str(len(file_list_3)) + " son de " + sound_dist_3 + "m."
        
    #Dist_4
    global file_list_4
    global listing_4
    
    file_list_4 = os.listdir(import_folder + "\\" + sound_dist_4 + "\\")
    if not file_list_4:
        listing_4 = "Placez dans le dossier \"" + import_folder + "/" + sound_dist_4 +"\" les sons.OGG d'objets avec " + sound_dist_4 + "m de distance." 
    else:
        listing_4 = "Il y a " + str(len(file_list_4)) + " son de " + sound_dist_4 + "m."
        
    #Dist_5
    global file_list_5
    global listing_5
    
    file_list_5 = os.listdir(import_folder + "\\" + sound_dist_5 + "\\")
    if not file_list_5:
        listing_5 = "Placez dans le dossier \"" + import_folder + "/" + sound_dist_5 +"\" les sons.OGG d'objets avec " + sound_dist_5 + "m de distance." 
    else:
        listing_5 = "Il y a " + str(len(file_list_5)) + " son de " + sound_dist_5 + "m."
    
    #Dist_6
    global file_list_6
    global listing_6
    
    file_list_6 = os.listdir(import_folder + "\\" + sound_dist_6 + "\\")
    if not file_list_6:
        listing_6 = "Placez dans le dossier \"" + import_folder + "/" + sound_dist_6 +"\" les sons.OGG d'objets avec " + sound_dist_6 + "m de distance." 
    else:
        listing_6 = "Il y a " + str(len(file_list_6)) + " son de " + sound_dist_6 + "m."
            
    #Dist_7
    global file_list_7
    global listing_7
    
    file_list_7 = os.listdir(import_folder + "\\" + sound_dist_7 + "\\")
    if not file_list_7:
        listing_7 = "Placez dans le dossier \"" + import_folder + "/" + sound_dist_7 +"\" les sons.OGG d'objets avec " + sound_dist_7 + "m de distance." 
    else:
        listing_7 = "Il y a " + str(len(file_list_7)) + " son de " + sound_dist_7 + "m."
            
    #Dist_8
    global file_list_8
    global listing_8
    
    file_list_8 = os.listdir(import_folder + "\\" + sound_dist_8 + "\\")
    if not file_list_8:
        listing_8 = "Placez dans le dossier \"" + import_folder + "/" + sound_dist_8 +"\" les sons.OGG d'objets avec " + sound_dist_8 + "m de distance." 
    else:
        listing_8 = "Il y a " + str(len(file_list_8)) + " son de " + sound_dist_8 + "m."
            
    #Dist_9
    global file_list_9
    global listing_9
    
    file_list_9 = os.listdir(import_folder + "\\" + sound_dist_9 + "\\")
    if not file_list_9:
        listing_9 = "Placez dans le dossier \"" + import_folder + "/" + sound_dist_9 +"\" les sons.OGG d'objets avec " + sound_dist_9 + "m de distance." 
    else:
        listing_9 = "Il y a " + str(len(file_list_9)) + " son de " + sound_dist_9 + "m."

def notification():
    
    # ==========================================
    # Information si il n'y a pas de sound
    # ==========================================
    print("")
    print("")
    print("==================================================")
    print("")
    print(listing_player)
    print(listing_1)
    print(listing_2)
    print(listing_3)
    print(listing_4)
    print(listing_5)
    print(listing_6)
    print(listing_7)
    print(listing_8)
    print(listing_9)
    print("")
    print("Vous trouverez une fois genere les fichiers dans")
    print("le dossier \""+ export_folder + "\"")
    print("                                          EA - Ted")
    print("==================================================")
    print("")
    print("")
    input("Appuyez sur n'importe quelle touche pour continuer...")
    return


def export_player_cpp():
    if (enable_export_player_cpp != True): return

    # ==========================================
    # Generation du fichier CPP
    # ==========================================
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
    print("Fichier player avec " + str(len(file_list_player)) + " sons generes.")


def export_profile_json():
    if (enable_export_profile_json != True): return

    # ==========================================
    # Generation du fichier profile-conf.json
    # ==========================================
    SoundsLists = {}
    Sounds = []
    for files in file_list_player:
        Sounds.append(files[:-4] + "_PLAYER")
    for files in file_list_1:
        Sounds.append(files[:-4] + "_" + sound_dist_1 + "m")
    for files in file_list_2:
        Sounds.append(files[:-4] + "_" + sound_dist_2 + "m")
    for files in file_list_3:
        Sounds.append(files[:-4] + "_" + sound_dist_3 + "m")
    for files in file_list_4:
        Sounds.append(files[:-4] + "_" + sound_dist_4 + "m")
    for files in file_list_5:
        Sounds.append(files[:-4] + "_" + sound_dist_5 + "m")
    for files in file_list_6:
        Sounds.append(files[:-4] + "_" + sound_dist_6 + "m")
    for files in file_list_7:
        Sounds.append(files[:-4] + "_" + sound_dist_7 + "m")
    for files in file_list_8:
        Sounds.append(files[:-4] + "_" + sound_dist_8 + "m")
    for files in file_list_9:
        Sounds.append(files[:-4] + "_" + sound_dist_9 + "m")
    SoundsLists["SoundsLists"] = Sounds
    with open(export_folder + "\\" + nom_profile_json, "w") as write_file:
        json.dump(SoundsLists, write_file, indent=4, sort_keys=True)
    print("Fichier profil de " + str(len(file_list_player + file_list_1 + file_list_2 + file_list_3 + file_list_4 + file_list_5 + file_list_6 + file_list_7 + file_list_8 + file_list_9)) + " sons generes.")
    print("==================================================")
    print("")
    print("") 


def export_distance_1_cpp():
    if (enable_export_distance_1_cpp != True): return

    # ==========================================
    # Generation du fichier de son a coordonnee 1
    # ==========================================
    with open(export_folder + "\\" + nom_export_dist_1_cpp, "a") as f:
        f.writelines("   //==========================================")
        f.writelines("\n   //Generation du fichier de son a coordonnee 1")
        f.writelines("\n   //==========================================")
        f.writelines("\n")

    for files in file_list_1:
        with open(export_folder + "\\" + nom_export_dist_1_cpp, "a") as f:
            f.writelines("\n" + "    class " + files[:-4] + "_" + sound_dist_1 + "M")
            f.writelines("\n" + "    {")
            f.writelines("\n" + "        samples[]=")
            f.writelines("\n" + "        {")
            f.writelines("\n" + "            {")
            f.writelines("\n" + "                \"\\" + addon_name + "\\" + sounds_folder + "\\" + files[:-4] + "_" + sound_dist_1 + "M" + "\",")
            f.writelines("\n" + "                1")
            f.writelines("\n" + "            }")
            f.writelines("\n" + "        };")
            f.writelines("\n" + "        volume=1;")
            f.writelines("\n" + "        range=" + sound_dist_1 + ";")
            f.writelines("\n" + "        rangeCurve[]=")
            f.writelines("\n" + "        {")
            f.writelines("\n" + "            {0,1},")
            f.writelines("\n" + "            {50,1},")
            f.writelines("\n" + "            {300,1}")
            f.writelines("\n" + "        };")
            f.writelines("\n" + "    };")      
            
    print("Fichier " + sound_dist_1 + "m avec " + str(len(file_list_1)) + " sons generes.")
     
def export_distance_2_cpp():
    if (enable_export_distance_2_cpp != True): return

    # ==========================================
    # Generation du fichier de son a coordonnee 2
    # ==========================================
    with open(export_folder + "\\" + nom_export_dist_2_cpp, "a") as f:
        f.writelines("   //==========================================")
        f.writelines("\n   //Generation du fichier de son a coordonnee 2")
        f.writelines("\n   //==========================================")
        f.writelines("\n")
        
    for files in file_list_2:
        with open(export_folder + "\\" + nom_export_dist_2_cpp, "a") as f:
            f.writelines("\n" + "    class " + files[:-4] + "_" + sound_dist_2 + "M")
            f.writelines("\n" + "    {")
            f.writelines("\n" + "        samples[]=")
            f.writelines("\n" + "        {")
            f.writelines("\n" + "            {")
            f.writelines("\n" + "                \"\\" + addon_name + "\\" + sounds_folder + "\\" + files[:-4] + "_" + sound_dist_2 + "M" + "\",")
            f.writelines("\n" + "                1")
            f.writelines("\n" + "            }")
            f.writelines("\n" + "        };")
            f.writelines("\n" + "        volume=1;")
            f.writelines("\n" + "        range=" + sound_dist_2 + ";")
            f.writelines("\n" + "        rangeCurve[]=")
            f.writelines("\n" + "        {")
            f.writelines("\n" + "            {0,1},")
            f.writelines("\n" + "            {50,1},")
            f.writelines("\n" + "            {300,1}")
            f.writelines("\n" + "        };")
            f.writelines("\n" + "    };")      
            
    print("Fichier " + sound_dist_2 + "m avec " + str(len(file_list_2)) + " sons generes.")

def export_distance_3_cpp():
    if (enable_export_distance_3_cpp != True): return

    # ==========================================
    # Generation du fichier de son a coordonnee 3
    # ==========================================
    with open(export_folder + "\\" + nom_export_dist_3_cpp, "a") as f:
        f.writelines("   //==========================================")
        f.writelines("\n   //Generation du fichier de son a coordonnee 3")
        f.writelines("\n   //==========================================")
        f.writelines("\n")
        
    for files in file_list_3:
        with open(export_folder + "\\" + nom_export_dist_3_cpp, "a") as f:
            f.writelines("\n" + "    class " + files[:-4] + "_" + sound_dist_3 + "M")
            f.writelines("\n" + "    {")
            f.writelines("\n" + "        samples[]=")
            f.writelines("\n" + "        {")
            f.writelines("\n" + "            {")
            f.writelines("\n" + "                \"\\" + addon_name + "\\" + sounds_folder + "\\" + files[:-4] + "_" + sound_dist_3 + "M" + "\",")
            f.writelines("\n" + "                1")
            f.writelines("\n" + "            }")
            f.writelines("\n" + "        };")
            f.writelines("\n" + "        volume=1;")
            f.writelines("\n" + "        range=" + sound_dist_3 + ";")
            f.writelines("\n" + "        rangeCurve[]=")
            f.writelines("\n" + "        {")
            f.writelines("\n" + "            {0,1},")
            f.writelines("\n" + "            {50,1},")
            f.writelines("\n" + "            {300,1}")
            f.writelines("\n" + "        };")
            f.writelines("\n" + "    };")      
            
    print("Fichier " + sound_dist_3 + "m avec " + str(len(file_list_3)) + " sons generes.")
    
def export_distance_4_cpp():
    if (enable_export_distance_4_cpp != True): return

    # ==========================================
    # Generation du fichier de son a coordonnee 4
    # ==========================================
    with open(export_folder + "\\" + nom_export_dist_4_cpp, "a") as f:
        f.writelines("   //==========================================")
        f.writelines("\n   //Generation du fichier de son a coordonnee 4")
        f.writelines("\n   //==========================================")
        f.writelines("\n")
        
    for files in file_list_4:
        with open(export_folder + "\\" + nom_export_dist_4_cpp, "a") as f:
            f.writelines("\n" + "    class " + files[:-4] + "_" + sound_dist_4 + "M")
            f.writelines("\n" + "    {")
            f.writelines("\n" + "        samples[]=")
            f.writelines("\n" + "        {")
            f.writelines("\n" + "            {")
            f.writelines("\n" + "                \"\\" + addon_name + "\\" + sounds_folder + "\\" + files[:-4] + "_" + sound_dist_4 + "M" + "\",")
            f.writelines("\n" + "                1")
            f.writelines("\n" + "            }")
            f.writelines("\n" + "        };")
            f.writelines("\n" + "        volume=1;")
            f.writelines("\n" + "        range=" + sound_dist_4 + ";")
            f.writelines("\n" + "        rangeCurve[]=")
            f.writelines("\n" + "        {")
            f.writelines("\n" + "            {0,1},")
            f.writelines("\n" + "            {50,1},")
            f.writelines("\n" + "            {300,1}")
            f.writelines("\n" + "        };")
            f.writelines("\n" + "    };")      
            
    print("Fichier " + sound_dist_4 + "m avec " + str(len(file_list_4)) + " sons generes.")
    
def export_distance_5_cpp():
    if (enable_export_distance_5_cpp != True): return

    # ==========================================
    # Generation du fichier de son a coordonnee 5
    # ==========================================
    with open(export_folder + "\\" + nom_export_dist_5_cpp, "a") as f:
        f.writelines("   //==========================================")
        f.writelines("\n   //Generation du fichier de son a coordonnee 5")
        f.writelines("\n   //==========================================")
        f.writelines("\n")
        
    for files in file_list_5:
        with open(export_folder + "\\" + nom_export_dist_5_cpp, "a") as f:
            f.writelines("\n" + "    class " + files[:-4] + "_" + sound_dist_5 + "M")
            f.writelines("\n" + "    {")
            f.writelines("\n" + "        samples[]=")
            f.writelines("\n" + "        {")
            f.writelines("\n" + "            {")
            f.writelines("\n" + "                \"\\" + addon_name + "\\" + sounds_folder + "\\" + files[:-4] + "_" + sound_dist_5 + "M" + "\",")
            f.writelines("\n" + "                1")
            f.writelines("\n" + "            }")
            f.writelines("\n" + "        };")
            f.writelines("\n" + "        volume=1;")
            f.writelines("\n" + "        range=" + sound_dist_5 + ";")
            f.writelines("\n" + "        rangeCurve[]=")
            f.writelines("\n" + "        {")
            f.writelines("\n" + "            {0,1},")
            f.writelines("\n" + "            {50,1},")
            f.writelines("\n" + "            {300,1}")
            f.writelines("\n" + "        };")
            f.writelines("\n" + "    };")      
            
    print("Fichier " + sound_dist_5 + "m avec " + str(len(file_list_5)) + " sons generes.")
    
def export_distance_6_cpp():
    if (enable_export_distance_6_cpp != True): return
        
    # ==========================================
    # Generation du fichier de son a coordonnee 6
    # ==========================================
    with open(export_folder + "\\" + nom_export_dist_6_cpp, "a") as f:
        f.writelines("   //==========================================")
        f.writelines("\n   //Generation du fichier de son a coordonnee 6")
        f.writelines("\n   //==========================================")
        f.writelines("\n")
        
    for files in file_list_6:
        with open(export_folder + "\\" + nom_export_dist_6_cpp, "a") as f:
            f.writelines("\n" + "    class " + files[:-4] + "_" + sound_dist_6 + "M")
            f.writelines("\n" + "    {")
            f.writelines("\n" + "        samples[]=")
            f.writelines("\n" + "        {")
            f.writelines("\n" + "            {")
            f.writelines("\n" + "                \"\\" + addon_name + "\\" + sounds_folder + "\\" + files[:-4] + "_" + sound_dist_6 + "M" + "\",")
            f.writelines("\n" + "                1")
            f.writelines("\n" + "            }")
            f.writelines("\n" + "        };")
            f.writelines("\n" + "        volume=1;")
            f.writelines("\n" + "        range=" + sound_dist_6 + ";")
            f.writelines("\n" + "        rangeCurve[]=")
            f.writelines("\n" + "        {")
            f.writelines("\n" + "            {0,1},")
            f.writelines("\n" + "            {50,1},")
            f.writelines("\n" + "            {300,1}")
            f.writelines("\n" + "        };")
            f.writelines("\n" + "    };")      
            
    print("Fichier " + sound_dist_6 + "m avec " + str(len(file_list_6)) + " sons generes.")

def export_distance_7_cpp():
    if (enable_export_distance_7_cpp != True): return

    # ==========================================
    # Generation du fichier de son a coordonnee 7
    # ==========================================
    with open(export_folder + "\\" + nom_export_dist_7_cpp, "a") as f:
        f.writelines("   //==========================================")
        f.writelines("\n   //Generation du fichier de son a coordonnee 7")
        f.writelines("\n   //==========================================")
        f.writelines("\n")
        
    for files in file_list_7:
        with open(export_folder + "\\" + nom_export_dist_7_cpp, "a") as f:
            f.writelines("\n" + "    class " + files[:-4] + "_" + sound_dist_7 + "M")
            f.writelines("\n" + "    {")
            f.writelines("\n" + "        samples[]=")
            f.writelines("\n" + "        {")
            f.writelines("\n" + "            {")
            f.writelines("\n" + "                \"\\" + addon_name + "\\" + sounds_folder + "\\" + files[:-4] + "_" + sound_dist_7 + "M" + "\",")
            f.writelines("\n" + "                1")
            f.writelines("\n" + "            }")
            f.writelines("\n" + "        };")
            f.writelines("\n" + "        volume=1;")
            f.writelines("\n" + "        range=" + sound_dist_7 + ";")
            f.writelines("\n" + "        rangeCurve[]=")
            f.writelines("\n" + "        {")
            f.writelines("\n" + "            {0,1},")
            f.writelines("\n" + "            {50,1},")
            f.writelines("\n" + "            {300,1}")
            f.writelines("\n" + "        };")
            f.writelines("\n" + "    };")      
            
    print("Fichier " + sound_dist_7 + "m avec " + str(len(file_list_7)) + " sons generes.")

def export_distance_8_cpp():
    if (enable_export_distance_8_cpp != True): return

    # ==========================================
    # Generation du fichier de son a coordonnee 8
    # ==========================================
    with open(export_folder + "\\" + nom_export_dist_8_cpp, "a") as f:
        f.writelines("   //==========================================")
        f.writelines("\n   //Generation du fichier de son a coordonnee 8")
        f.writelines("\n   //==========================================")
        f.writelines("\n")
        
    for files in file_list_8:
        with open(export_folder + "\\" + nom_export_dist_8_cpp, "a") as f:
            f.writelines("\n" + "    class " + files[:-4] + "_" + sound_dist_8 + "M")
            f.writelines("\n" + "    {")
            f.writelines("\n" + "        samples[]=")
            f.writelines("\n" + "        {")
            f.writelines("\n" + "            {")
            f.writelines("\n" + "                \"\\" + addon_name + "\\" + sounds_folder + "\\" + files[:-4] + "_" + sound_dist_8 + "M" + "\",")
            f.writelines("\n" + "                1")
            f.writelines("\n" + "            }")
            f.writelines("\n" + "        };")
            f.writelines("\n" + "        volume=1;")
            f.writelines("\n" + "        range=" + sound_dist_8 + ";")
            f.writelines("\n" + "        rangeCurve[]=")
            f.writelines("\n" + "        {")
            f.writelines("\n" + "            {0,1},")
            f.writelines("\n" + "            {50,1},")
            f.writelines("\n" + "            {300,1}")
            f.writelines("\n" + "        };")
            f.writelines("\n" + "    };")      
            
    print("Fichier " + sound_dist_8 + "m avec " + str(len(file_list_8)) + " sons generes.")

def export_distance_9_cpp():
    if (enable_export_distance_9_cpp != True): return

    # ==========================================
    # Generation du fichier de son a coordonnee 9
    # ==========================================
    with open(export_folder + "\\" + nom_export_dist_9_cpp, "a") as f:
        f.writelines("   //==========================================")
        f.writelines("\n   //Generation du fichier de son a coordonnee 9")
        f.writelines("\n   //==========================================")
        f.writelines("\n")

    for files in file_list_9:
        with open(export_folder + "\\" + nom_export_dist_9_cpp, "a") as f:
            f.writelines("\n" + "    class " + files[:-4] + "_" + sound_dist_9 + "M")
            f.writelines("\n" + "    {")
            f.writelines("\n" + "        samples[]=")
            f.writelines("\n" + "        {")
            f.writelines("\n" + "            {")
            f.writelines("\n" + "                \"\\" + addon_name + "\\" + sounds_folder + "\\" + files[:-4] + "_" + sound_dist_9 + "M" + "\",")
            f.writelines("\n" + "                1")
            f.writelines("\n" + "            }")
            f.writelines("\n" + "        };")
            f.writelines("\n" + "        volume=1;")
            f.writelines("\n" + "        range=" + sound_dist_9 + ";")
            f.writelines("\n" + "        rangeCurve[]=")
            f.writelines("\n" + "        {")
            f.writelines("\n" + "            {0,1},")
            f.writelines("\n" + "            {50,1},")
            f.writelines("\n" + "            {300,1}")
            f.writelines("\n" + "        };")
            f.writelines("\n" + "    };")      
            
    print("Fichier " + sound_dist_9 + "m avec " + str(len(file_list_9)) + " sons generes.")

def copy():
    # ==========================================
    # Verification si le dossier Sound existe
    # ==========================================
    
    #Creation du dossier
    if os.path.exists(sounds_folder + "\\") == False:
        os.mkdir(sounds_folder + "\\")

    # ==========================================
    # Copie et suppression des sons dans le dossier sound
    # ==========================================
    
    #Players
    for files in file_list_player:
        shutil.copyfile(import_folder + "\\" + player_sound_folder + "\\" + files, sounds_folder + "\\" + files[:-4] + "_PLAYER.ogg")
        
    #Dist_1
    for files in file_list_1:
        shutil.copyfile(import_folder + "\\" + sound_dist_1 + "\\" + files, sounds_folder + "\\" + files[:-4] + "_" + sound_dist_1 + "M.ogg")
        
    #Dist_2
    for files in file_list_2:
        shutil.copyfile(import_folder + "\\" + sound_dist_2 + "\\" + files, sounds_folder + "\\" + files[:-4] + "_" + sound_dist_2 + "M.ogg")
        
    #Dist_3
    for files in file_list_3:
        shutil.copyfile(import_folder + "\\" + sound_dist_3 + "\\" + files, sounds_folder + "\\" + files[:-4] + "_" + sound_dist_3 + "M.ogg")
        
    #Dist_4
    for files in file_list_4:
        shutil.copyfile(import_folder + "\\" + sound_dist_4 + "\\" + files, sounds_folder + "\\" + files[:-4] + "_" + sound_dist_4 + "M.ogg")
        
    #Dist_5
    for files in file_list_5:
        shutil.copyfile(import_folder + "\\" + sound_dist_5 + "\\" + files, sounds_folder + "\\" + files[:-4] + "_" + sound_dist_5 + "M.ogg")
        
    #Dist_6
    for files in file_list_6:
        shutil.copyfile(import_folder + "\\" + sound_dist_6 + "\\" + files, sounds_folder + "\\" + files[:-4] + "_" + sound_dist_6 + "M.ogg")
        
    #Dist_7
    for files in file_list_7:
        shutil.copyfile(import_folder + "\\" + sound_dist_7 + "\\" + files, sounds_folder + "\\" + files[:-4] + "_" + sound_dist_7 + "M.ogg")
        
    #Dist_8
    for files in file_list_8:
        shutil.copyfile(import_folder + "\\" + sound_dist_8 + "\\" + files, sounds_folder + "\\" + files[:-4] + "_" + sound_dist_8 + "M.ogg")
        
    #Dist_9
    for files in file_list_9:
        shutil.copyfile(import_folder + "\\" + sound_dist_9 + "\\" + files, sounds_folder + "\\" + files[:-4] + "_" + sound_dist_9 + "M.ogg")
    
    
def remover(): 
    error_question = False

    # ==========================================
    # Demande de suppression
    # ==========================================
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
            print("Vous avez ACCEPTe la suppression des Imports.")
        else:
            print("Le fichier des Imports n'existait deja plus.")
    elif question1 == "N" or question1 == "n": 
        print("Vous avez REFUSe la suppression des Imports.")
    else:
        error_question = True

    if question2 == "Y" or question2 == "y":
        if os.path.exists(export_folder + "\\") == True:
            shutil.rmtree(export_folder)
            print("Vous avez ACCEPTe la suppression des Exports.")
        else:
            print("Le fichier des Exports n'existait deja plus.")
    elif question2 == "N" or question2 == "n": 
        print("Vous avez REFUSe la suppression des Exports.")    
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


init()
