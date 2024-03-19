import sys
import time
import msvcrt
from reprint import output
import nltk
import random
import re
def typing_test_ydratec():
    text_to_display = ""  # Initialise le texte saisi
    nltk.download('gutenberg', quiet=True)
    nltk.download('punkt', quiet=True)
    gutenberg_files = nltk.corpus.gutenberg.fileids()
    random_text = nltk.corpus.gutenberg.raw(random.choice(gutenberg_files))
    random_text = random_text[0:1000]
    random_text = re.sub(r'[\n\r\t\[\]]', '', random_text)
    random_text = random_text.replace("  ", " ")
    text_to_display = random_text
    typed_text = ""  # Initialise le texte saisi
    i = 0
    barre ="\033[31;40m|\033[0m" + "_"*(60)
    text_to_display_60_chars = text_to_display[0:60]
    with output(initial_len=3, interval=0) as output_lines:
        output_lines[0] = barre
        output_lines[1] = text_to_display_60_chars
        output_lines[2] = barre
    sys.stdout.write("\x1b[1A" * 3)
    sys.stdout.flush()  # Force l'affichage
    while True:
        if msvcrt.kbhit():  # Vérifie si une touche a été enfoncée
            char = msvcrt.getch().decode()  # Récupère le caractère pressé
            if char == '\r':  # Si l'utilisateur appuie sur Entrée, affiche la ligne
                nb_word = len(typed_text.split())
                time_end = time.time()
                time_total = time_end - time_start
                time_seconde = int(time_total)
                nb_word_per_minute = int(nb_word / time_seconde * 60)
                print("\n\n\n\nVous avez tapé", nb_word, "mots en", time_seconde, "secondes, soit", nb_word_per_minute, "mots par minute.")
                break
            else:
                ## check if the char is equal to the next char in the text_to_display
                if char == text_to_display[i]:
                    if i == 0: 
                        time_start = time.time()
                    i += 1
                    if i < 20 :
                        text_to_display_60_chars = text_to_display[0:60]
                        barre = "_"*(i) + "\033[31;40m|\033[0m" + "_"*(60-i)
                        text_to_display_60_chars ='\033[31;47m'+ text_to_display_60_chars[0:i] + "\033[31;40m" + text_to_display_60_chars[i] + "\033[0m" + text_to_display_60_chars[i+1:]
                    else:
                        barre = "____________________\033[31;40m|\033[0m_________________________________"
                        text_to_display_60_chars = text_to_display[i-20:i+40]
                        text_to_display_60_chars = '\033[30;47m'+ text_to_display_60_chars[0:20]+ "\033[31;40m" + text_to_display_60_chars[20] + "\033[0m"+text_to_display_60_chars[21:]
                    typed_text += char  # Ajoute le caractère à la ligne en cours de saisie
                    with output(initial_len=3, interval=0) as output_lines:
                        output_lines[0] = barre
                        output_lines[1] = text_to_display_60_chars
                        output_lines[2] = barre
                    sys.stdout.write("\x1b[1A" * 3)
                    sys.stdout.flush()  # Force l'affichage
if __name__ == "__main__":
    typing_test_ydratec()
