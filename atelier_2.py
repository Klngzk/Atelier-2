# 1. Créer une liste en choisissant des éléments d'index impair dans la première liste et des
# éléments d'index pair dans la seconde.
def creerl_0(l1,l2):
    result = l1[1::2] + l2[::2]
    return result

# Exemple
list_01 =[3, 6, 9, 12, 15, 18, 21]
list_02 =[4, 8, 12, 16, 20, 24, 28]

creerl_0(list_01,list_02)

# 2. Deviser la liste en 3 morceaux égaux et inverser chaque morceau
def divl_0(l1):
    m= len(l1) // 3
    #deviser la list en 3
    first = l1[:m]
    second = l1[m:m*2]
    third = l1[m*2:]
    #inverser l'ordre
    first.reverse()
    second.reverse()
    third.reverse()
    #afficher les resultats
    print(first)
    print(second)
    print(third)
# Exemple
list_03 = [11, 45, 8, 23, 14, 12, 78, 45, 89]
divl_0(list_03)
# 3. Écrire un programme pour itérer une liste donnée et compter l'occurrence de chaque élément et
# créer un dictionnaire pour montrer le nombre de chaque élément.
def dict_0(l1):
    mydict={}
    uni = set(l1) #utiliser set pour eviter les duplication
    for i in uni:
#ajouter des keys et values au dictionnaire avec key=élément dans set;value= combien se élément est répétée dans la list donnée
        mydict[i] = l1.count(i) 
    print(mydict)
#Exemple
list_04 = [11, 45, 8, 11, 23, 45, 23, 45, 89]
dict_0(list_04)
# 4. Trouver l'intersection (commune) de deux Sets et supprimez ces éléments du premier Set

def set_0(set1,set2):
    set3 = set1.intersection(set2) #Trouver l'intersection et stocker le résultat dans une nouvelle set
    print("Intersection: ", set3)
    set4 = set1.difference(set3) #Supprimer les elements répétés et stocker le resultat dans une nouvelle set
    print("Set 1 après suppression : ", set4)

#Exemple
set_01 ={23, 42, 65, 57, 78, 83, 29}
set_02 ={57, 83, 29, 67, 73, 43, 48}
set_0(set_01,set_02)
# 5. Itérer une liste donnée et vérifier si un élément donné existe en tant que valeur de clé dans
# un dictionnaire. Sinon, supprimez-le de la liste


def creerl_1(list,dict):
    for i in list:
        for j in dict:
            if i == dict[j]:
                break
            else: #check si l'elemnt du list donnee = valeur de cle
                list.remove(i)
                break
                  #sinon supprimer 
    print(list)

#Exemple
list_05 = [47, 64, 69, 37, 76, 83, 95, 97]
dict_01= {'Yassine':47, 'Imane':95, 'Mohammed':76, 'Abir':97}
creerl_1(list_05,dict_01)
