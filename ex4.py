# Question :1
# L'algo de (Welsh & Powell)
def welsh_powell_coloring(graph):
    # Calculer le degré de chaque sommet
    degrees = {node: len(neighbors) for node, neighbors in graph.items()}

    # Trier les sommets par ordre décroissant de leurs degrés
    sorted_nodes = sorted(degrees, key=degrees.get, reverse=True)

    # Initialiser un dictionnaire pour stocker les couleurs des sommets
    coloring = {}
    # Liste des couleurs utilisées
    color = 0
    while len(coloring) < len(graph):  # Tant que tous les sommets ne sont pas coloriés
        color += 1  # Nouvelle couleur
        uncolored_nodes = [node for node in sorted_nodes if node not in coloring]

        for node in uncolored_nodes:
            # Vérifier si le sommet peut être coloré avec la couleur actuelle
            if all(neigh not in coloring or coloring[neigh] != color for neigh in graph[node]):
                coloring[node] = color
    return coloring

# Exemple de graphe avec les arêtes incompatibles
graphe_incompatibles = {
    "AC": ["EC", "DA", "DC", "CD", "BE", "BD"],
    "AE": ["BE"], 
    "BA": ["DA", "CA"],
    "BE": ["AC", "DA", "CA"],
    "BD": ["AC", "ED", "EC", "CD", "DA"],
    "CA": ["DA", "BD", "BE", "BA"],
    "CD": ["AC", "ED", "EC", "DA", "DC"],
    "DC": ["AC", "EC"],
    "DA": ["AC", "CD", "BA", "EC", "BE", "BD", "CA"],
    "EC": ["CD", "BD", "DC", "DA", "AC"],
    "ED": ["CD", "BD"]
}

# Exécuter l'algorithme
coloring_result = welsh_powell_coloring(graphe_incompatibles)

# Afficher le résultat
print("question 2: Coloration des sommets :", coloring_result)


# question 3 
# Il sont des stables , compatibles
def group_by_color(coloring):
    # Initialiser un dictionnaire pour regrouper les sommets par couleur
    color_groups = {}

    # Parcourir chaque sommet et sa couleur
    for node, color in coloring.items():
        if color not in color_groups:
            color_groups[color] = []
        color_groups[color].append(node)

    return color_groups
a=welsh_powell_coloring(graphe_incompatibles )
print("question3 : L'ensembles des stables  " ,group_by_color(a))


#question 4 
b= group_by_color(a)
print("Le nombre de chromatique de graphe :  ", len(b))



