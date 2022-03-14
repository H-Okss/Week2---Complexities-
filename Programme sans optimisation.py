result = []
with open("Ids.in", 'r') as ids:
    with open("Details.in","r") as details:
        with open("results.out", "w") as results:
            ids_content = ids.read().splitlines() #Liste du contenu du fichier Ids
            details_content = details.read().splitlines() #Liste du contenu du fichier details
                
            details_content2 = []
            for el in details_content[1:]:
                details_content2.append(el.split(","))  #Conversion de la liste details_content[1:] en liste de listes de lignes en séparant chaque ligne de celle-ci par des virgules.
     
            for i in range(int(ids_content[0])+1): #Parcours de la liste ids_content
                for j in range(int(details_content[0])):  #Parcours de la liste details_content
                    if ids_content[i] == details_content2[j][0]:  #Vérification que les IDs sont identiques
                        result.append(','.join(details_content2[j]))  # Conversion de la liste details_content2[j] en 
                        result.append("\n")
            results.writelines(result)
  

# Complexité : O(taille(ids)*taille(details))