import pandas as pd
import subprocess
import argparse

# Funktion zum Ausführen des mbpoll-Kommandos
def run_mbpoll(register_value, verbose=False):
    command = f"mbpoll 172.30.3.8 -0 -r {register_value} -t 3 -c 1"
    try:
        # Ausführen des Kommandos und Ausgabe erfassen
        result = subprocess.check_output(command, shell=True, text=True)
        if verbose:
            print(f"Register {register_value}: {result.strip()}")
        return result.strip()
    except subprocess.CalledProcessError as e:
        error_message = f"Error: {e}"
        if verbose:
            print(error_message)
        return error_message

def main():
    # Argumente parsen
    parser = argparse.ArgumentParser(description="Führe mbpoll auf CSV-Daten aus und gib die Ergebnisse aus.")
    parser.add_argument("csv_file", help="Pfad zur CSV-Datei")
    parser.add_argument("-v", "--verbose", action="store_true", help="Gibt jede Zeile direkt aus")
    args = parser.parse_args()

    # CSV-Datei einlesen
    csv_data = pd.read_csv(args.csv_file, delimiter='\t')

    # Neue Spalte für die Ergebnisse erstellen
    csv_data['mbpoll_output'] = csv_data['Register'].apply(run_mbpoll, verbose=args.verbose)

    # Speichere die aktualisierte CSV-Datei
    output_file = 'updated_csv_file.csv'
    csv_data.to_csv(output_file, sep='\t', index=False)

    print(f"Die Datei wurde erfolgreich erstellt: {output_file}")

if __name__ == "__main__":
    main()
