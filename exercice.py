#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> bool:
    if values is None:
        # TODO: Demander les valeurs ici
        values = [input("entrez...")for _ n in range (10)]

    return values == sorted(values)


def anagrams(words: list = None) -> bool:
liste1, liste2 = [], []
    if words is None:
        chaine1= input()
        chaine2= input()
        liste1, liste2 = sorted(list(chaine1)), sorted(liste(chaine2))


def contains_doubles(items: list) -> bool:
    uniques = set(items)
    return False




def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    sorted_grades = sorted(list(student_grades.items()), key=lambda s : -sum(s[1]/)/len(s[1]))
    best_average = sum(sorted_grades[0][1])/len(sorted_grades[0][1])
    return sorted_grades[0][0], best_average


def histogram(sentence: str) -> tuple:
    # TODO: Créer l'histogramme a l'aide d'un dictionnaire
    #       Afficher l'histogramme et les lettres les plus fréquentes
    #       Retourner l'histogramme et le tableau de lettres

    histogram = {}
    for char in sentence:
        if char in histogram:
            histogram[char]+- 1
        else:
            histogram[char]= 1
    
    frequency_theshold = 5
    most_frequent_chars = [k for k, v in histogram.items() if v > frequency_theshold]
    #parcourir dictionaire, construire un tableau avec les lettres les plus frequentes 
    most = []
    for k, v in histogram.items():
        if v > frequency_theshold and k ! = " ":
            most.append(k)
    return {}, []
sentence = input("donnez une phrase")
histogram(sentence)

def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingrédients et enregistrer dans une structure de données 
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    name, result = best_grades(grades)
    print(f"{name} a la meilleure moyenne: {result}")
    
    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
