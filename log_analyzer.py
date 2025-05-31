import os
from colorama import Fore, Style, init

# Initialiser colorama (nécessaire pour Windows)
init(autoreset=True)

def analyze_log_file(input_file, output_file):
    # Vérifier si le fichier existe
    if not os.path.exists(input_file):
        print(Fore.RED + f"Erreur : le fichier {input_file} n'existe pas.")
        return

    # Initialiser les compteurs
    counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    # Lecture et analyse du fichier log
    with open(input_file, "r") as file:
        for line in file:
            for level in counts:
                if level in line:
                    counts[level] += 1

    # Affichage des résultats avec couleurs
    print("\nRésumé de l'analyse :")
    print(Fore.GREEN + f"INFO    : {counts['INFO']}")
    print(Fore.YELLOW + f"WARNING : {counts['WARNING']}")
    print(Fore.RED + f"ERROR   : {counts['ERROR']}")

    # Écriture du rapport dans un fichier
    with open(output_file, "w") as f:
        f.write("Statistiques des logs :\n")
        f.write(f"INFO    : {counts['INFO']}\n")
        f.write(f"WARNING : {counts['WARNING']}\n")
        f.write(f"ERROR   : {counts['ERROR']}\n")

    print(Fore.CYAN + f"\nLe rapport a été généré dans le fichier {output_file}")

# Point d'entrée
if __name__ == "__main__":
    analyze_log_file("log.txt", "rapport.txt")
