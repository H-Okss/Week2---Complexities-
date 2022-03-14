import re

def extract_id_details(line):
    """
    entrée: CV45365468,Mohamed,Jilali,Tanger
    sortie: CV45365468
    """
    result = re.search(r'(\w{1,2}\d*)', line)
    if result != None:
        return result.group(1)
    else:
        return None
        
with open("Ids.in", 'r') as ids:
    with open("Details.in","r") as details:
        with open("results.out", "w") as results:
            ids_content = [line.strip() for line in ids]      
            for line in details:
                if extract_id_details(line) in ids_content[1:]:
                    results.write(line)

# Complexité : O(taille(details))