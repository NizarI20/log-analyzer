# log_analyzer.py

def analyze_log_file(input_file, output_file):
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    with open(input_file, "r") as f:
        for line in f:
            for level in counts.keys():
                if level in line:
                    counts[level] += 1

    with open(output_file, "w") as f:
        f.write("Statistiques des logs :\n")
        for level, count in counts.items():
            f.write(f"{level} : {count}\n")

    print("Analyse terminée. Résultat dans", output_file)

if __name__ == "__main__":
    analyze_log_file("log.txt", "rapport.txt")
