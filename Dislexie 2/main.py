import tkinter as tk
from math import cos, sin, pi
from tkinter import messagebox, font
import pygame
import os
import random
import sounddevice as sd
import numpy as np
from PIL import Image, ImageTk
import speech_recognition as sr

# Inițializează pygame pentru sunete
pygame.mixer.init()

# Funcție pentru a reda un fișier audio
def play_sound(file_name):
    file_name = file_name.upper()  # Convertim inputul la majuscule pentru consistență
    sound_path = os.path.join("static/sounds", f"{file_name}.mp3")
    if os.path.exists(sound_path):
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()
    else:
        messagebox.showerror("Eroare", f"Fișierul audio {file_name}.mp3 nu a fost găsit!")

# Funcție pentru a reda mesajul audio blocat
def play_locked_message():
    play_sound("locked_message")

def learn_vowels():
    """Creates the 'Învățăm vocalele' learning window."""
    learn_window = tk.Toplevel()
    learn_window.title("Învățăm vocalele")
    learn_window.geometry("900x700")
    learn_window.configure(bg="#DBE1F1")  # Matches the CSS background

    # Fonts for styling
    instruction_font = font.Font(family="Super Creamy", size=18, weight="bold")
    button_font = font.Font(family="Arial", size=16, weight="bold")

    # Instruction Label with hover and click-to-play functionality
    instruction_label = tk.Label(
        learn_window,
        text="Apasă pe fiecare vocală pentru a-i auzi sunetul! 🔊",
        font=instruction_font,
        bg="#DBE1F1",
        fg="#333",
        pady=20,
        cursor="hand2",  # Hand cursor to indicate interactivity
    )
    instruction_label.pack()

    # Play instruction sound when label is clicked
    instruction_label.bind("<Button-1>", lambda event: play_sound("instruction_apasa_vocala"))

    # Create a container for vowel buttons
    vowels_frame = tk.Frame(learn_window, bg="#DBE1F1", pady=20)
    vowels_frame.pack()

    vowels = [('A', 'a'), ('E', 'e'), ('I', 'i'), ('O', 'o'), ('U', 'u')]

    # Generate buttons for each vowel
    for big, small in vowels:
        # Frame for a pair of buttons (uppercase and lowercase)
        button_pair_frame = tk.Frame(vowels_frame, bg="#DBE1F1")
        button_pair_frame.pack(pady=10)

        # Uppercase button
        big_button = tk.Button(
            button_pair_frame,
            text=big,
            font=button_font,
            bg="#96ADFC", # albastru pastel
            fg="white",
            activebackground="#000c66", # albastru navy
            activeforeground="white",
            command=lambda v=big: play_sound(v),
            width=6,
            height=2,
            relief="raised",
            borderwidth=3,
            cursor="hand2",
        )
        big_button.pack(side=tk.LEFT, padx=10)

        # Lowercase button
        small_button = tk.Button(
            button_pair_frame,
            text=small,
            font=button_font,
            bg="#E0A6AA", #pastel roz
            fg="white",
            activebackground="#AA336A", # roz inchis
            activeforeground="white",
            command=lambda v=small: play_sound(v),
            width=6,
            height=2,
            relief="raised",
            borderwidth=3,
            cursor="hand2",
        )
        small_button.pack(side=tk.LEFT, padx=10)

# Joc interactiv pentru selectarea vocalei corecte
def play_game():
    global score
    game_window = tk.Toplevel(app)
    game_window.title("Joacă - Selectează vocala corectă")
    game_window.geometry("600x400")
    game_window.configure(bg="#D4F1B4")

    vowels = [('A', 'a'), ('E', 'e'), ('I', 'i'), ('O', 'o'), ('U', 'u')]
    correct_vowel = tk.StringVar()

    def update_question():
        selected_pair = random.choice(vowels)
        correct_vowel.set(random.choice(selected_pair))
        question_label.config(text=f"Alege vocala: {correct_vowel.get()}")
        feedback_label.config(text="")

    def check_answer(vowel):
        global score
        if vowel == correct_vowel.get():
            score += 1
            score_label.config(text=f"Scor: {score}")
            play_sound("correct")
            feedback_label.config(text="Bravo! Ai ales corect!", fg="green")
        else:
            play_sound("wrong")
            feedback_label.config(text="Mai încearcă! Nu ai ales corect.", fg="red")
        update_match_button()
        update_question()

    question_label = tk.Label(game_window, text="", font=("Super Creamy", 20), bg="#D4F1B4", fg="black")
    question_label.pack(pady=20)

    buttons_frame = tk.Frame(game_window, bg="#D4F1B4")
    buttons_frame.pack()

    for big, small in vowels:
        row_frame = tk.Frame(buttons_frame, bg="#D4F1B4")
        row_frame.pack(pady=5)

        big_button = tk.Button(
            row_frame,
            text=big,
            font=("Arial", 20),
            bg="#8CD790",
            fg="black",
            command=lambda v=big: check_answer(v),
            width=5
        )
        big_button.pack(side=tk.LEFT, padx=5)

        small_button = tk.Button(
            row_frame,
            text=small,
            font=("Arial", 20),
            bg="#8CD790",
            fg="black",
            command=lambda v=small: check_answer(v),
            width=5
        )
        small_button.pack(side=tk.LEFT, padx=5)

    score_label = tk.Label(game_window, text=f"Scor: {score}", font=("Karmatic Arcade", 18), bg="#D4F1B4", fg="black")
    score_label.pack(pady=10)

    feedback_label = tk.Label(game_window, text="", font=("Arial", 16), bg="#D4F1B4", fg="black")
    feedback_label.pack(pady=10)

    update_question()

# Jocul de asociere a vocalelor cu cuvintele
def play_sound(file_name):
    file_name = file_name.upper()  # Convertim inputul la majuscule pentru consistență
    sound_path = os.path.join("static/sounds", f"{file_name}.mp3")
    if os.path.exists(sound_path):
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()
    else:
        messagebox.showerror("Eroare", f"Fișierul audio {file_name}.mp3 nu a fost găsit!")

# Jocul de asociere a vocalelor cu cuvintele

def learn_by_drawing():
    # Crearea ferestrei jocului
    draw_window = tk.Toplevel(app)
    draw_window.title("Mod de învățare prin desenare")
    draw_window.geometry("800x800")
    draw_window.configure(bg="#FFFACD")

    # Dimensiuni și culori
    WIDTH, HEIGHT = 600, 400  # Fundal alb mai centrat
    WHITE = "#FFFFFF"
    BLACK = "#000000"
    YELLOW = "#FFCC00"
    RED = "#FF0000"
    BLUE = "#0000FF"

    # Etichetă pentru mesajul de instrucțiuni
    instruction_label = tk.Label(
        draw_window,
        text="Urmărește bulina roșie pentru a desena vocala!",
        font=("Arial", 18),
        bg="#FFFACD",
        fg=BLACK
    )
    instruction_label.pack(pady=10)  # Adaugă un spațiu deasupra

    # Etichetă pentru vocala curentă
    current_vowel_label = tk.Label(
        draw_window,
        text="Desenează vocala: A",  # Setarea implicită pentru prima vocală
        font=("Arial", 22, "bold"),
        bg="#FFFACD",
        fg=BLACK
    )
    current_vowel_label.pack(pady=5)

    # Canvas pentru desenare
    canvas = tk.Canvas(draw_window, width=WIDTH, height=HEIGHT, bg=WHITE)
    canvas.pack(pady=20)

    # Date pentru traseele de săgeți ale vocalelor
    arrow_paths = {
        "A": [
            [(300, 100), (250, 200), (200, 300)],  # Diagonală stânga
            [(300, 100), (350, 200), (400, 300)],  # Diagonală dreapta
            [(250, 200), (350, 200)]               # Bara orizontală
        ],
        "E": [
            [(250, 100), (250, 200)],  # Vertical sus
            [(250, 200), (250, 300)],  # Vertical jos
            [(250, 100), (350, 100)],  # Orizontal sus
            [(250, 200), (350, 200)],  # Orizontal mijloc
            [(250, 300), (350, 300)]   # Orizontal jos
        ],
        "I": [[(300, 100), (300, 300)]],  # Linie verticală
        "O": [
            [(300 + 100 * cos(angle), 200 + 100 * sin(angle))
             for angle in [2 * pi - i * (2 * pi / 20) for i in range(21)]]
        ],
        "U": [
            [(250, 100), (250, 250)],  # Linie verticală stânga
            [
                # Semicerc conectat la capetele dreptelor verticale
                (300 + 50 * cos(angle), 250 + 50 * sin(angle))  # Centru semicerc: (300, 250), rază: 50
                for angle in [pi - i * (pi / 20) for i in range(21)]  # Semicerc invers, de la stânga la dreapta
            ],
            [(350, 250), (350, 100)],  # Linie verticală dreapta
        ],
    }

    # Vocală curentă și progres
    current_vowel = tk.StringVar(value="A")
    traced_points = []  # Puncte desenate de utilizator
    progress_index = 0
    line_index = 0
    is_completed = tk.BooleanVar(value=False)  # Stare de completare a literei

    # Funcții pentru desenare
    def draw_arrows(vowel, line_idx, progress_idx):
        """Desenează săgețile traseului."""
        canvas.delete("all")  # Curăță traseele anterioare
        path = arrow_paths[vowel]
        for l_idx, line in enumerate(path):
            for p_idx, point in enumerate(line):
                x, y = point
                if l_idx == line_idx and p_idx == progress_idx:
                    canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill=RED)  # Punct curent
                else:
                    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=YELLOW)

    def draw_trace():
        """Desenează traseul urmat."""
        for line in traced_points:
            for i in range(1, len(line)):
                x1, y1 = line[i - 1]
                x2, y2 = line[i]
                canvas.create_line(x1, y1, x2, y2, fill=BLUE, width=3)

    def is_near(pos1, pos2, tolerance=20):
        """Verifică dacă două puncte sunt aproape."""
        return abs(pos1[0] - pos2[0]) <= tolerance and abs(pos1[1] - pos2[1]) <= tolerance

    def on_mouse_move(event):
        nonlocal progress_index, line_index
        mouse_pos = (event.x, event.y)
        vowel = current_vowel.get()

        if line_index < len(arrow_paths[vowel]):
            line = arrow_paths[vowel][line_index]
            if progress_index < len(line):
                target_point = line[progress_index]
                if is_near(mouse_pos, target_point):
                    if len(traced_points) <= line_index:
                        traced_points.append([])  # Creăm sublista dacă nu există
                    traced_points[line_index].append(target_point)
                    progress_index += 1

                    # Verifică dacă linia este completă
                    if progress_index == len(line):
                        line_index += 1
                        progress_index = 0

        draw_arrows(vowel, line_index, progress_index)
        draw_trace()

        # Verifică dacă toate liniile au fost completate
        if line_index == len(arrow_paths[vowel]) and not is_completed.get():
            is_completed.set(True)  # Marchează vocala ca fiind complet desenată
            draw_full_letter()  # Desenează litera complet
            play_sound("litera_finalizata")  # Redă sunetul "Bravo!" o singură dată

    def draw_full_letter():
        """Desenează litera completă în albastru."""
        canvas.delete("all")
        for line in arrow_paths[current_vowel.get()]:
            for i in range(1, len(line)):
                x1, y1 = line[i - 1]
                x2, y2 = line[i]
                canvas.create_line(x1, y1, x2, y2, fill=BLUE, width=3)

    def next_vowel():
        """Trece la următoarea vocală."""
        if not is_completed.get():
            play_sound("complete_the_letter")  # Redă mesajul audio dacă nu e terminată
            return

        nonlocal traced_points, line_index, progress_index
        vowels = list(arrow_paths.keys())
        current_index = vowels.index(current_vowel.get())
        next_index = (current_index + 1) % len(vowels)
        current_vowel.set(vowels[next_index])

        # Actualizează eticheta pentru vocala curentă
        current_vowel_label.config(text=f"Desenează vocala: {current_vowel.get()}")

        # Resetează progresul
        traced_points = []
        line_index = 0
        progress_index = 0
        is_completed.set(False)
        draw_arrows(current_vowel.get(), line_index, progress_index)

    # Buton pentru următoarea vocală
    next_button = tk.Button(
        draw_window, text="Următoarea vocală", font=("Arial", 16), bg=YELLOW,
        state=tk.NORMAL, command=next_vowel
    )
    next_button.pack(pady=10)

    # Evenimente
    canvas.bind("<Motion>", on_mouse_move)

    # Desenează prima vocală
    draw_arrows(current_vowel.get(), line_index, progress_index)


def play_matching_game():
    match_window = tk.Toplevel(app)
    match_window.title("Joacă - Asociază vocala cu cuvântul")
    match_window.geometry("800x500")
    match_window.configure(bg="#FFE4B5")

    # Cuvintele asociate pentru fiecare vocală
    words = {
        "A": ["Ana"],
        "E": ["Elena"],
        "I": ["India"],
        "O": ["Oscar"],
        "U": ["Ungaria"],
        "a": ["aer", "arbore"],
        "e": ["energie", "efort"],
        "i": ["inel"],
        "o": ["ochi"],
        "u": ["urs"]
    }

    selected_vowel = tk.StringVar()  # Vocală selectată
    current_score = tk.IntVar(value=0)  # Scorul curent
    buttons_dict = {}  # Referințe la butoanele pentru cuvinte

    # Amestecăm cuvintele
    all_words = [(vowel, word) for vowel, word_list in words.items() for word in word_list]
    random.shuffle(all_words)

    def select_vowel(vowel):
        selected_vowel.set(vowel)
        feedback_label.config(text=f"Ai selectat vocala: {vowel}", fg="blue")
        play_sound(vowel)

    def select_word(word):
        vowel = selected_vowel.get()
        if not vowel:
            feedback_label.config(text="Te rog să selectezi mai întâi o vocală!", fg="red")
            play_sound("select_vowel")  # Mesaj audio pentru a selecta vocala
            return

        # Verificăm dacă prima literă a cuvântului corespunde cu vocala selectată
        if word.startswith(vowel):
            play_sound("correct")  # Mesaj audio pentru răspuns corect
            current_score.set(current_score.get() + 1)
            score_label.config(text=f"Scor: {current_score.get()}")
            feedback_label.config(text="Bravo! Ai făcut corect! Selectează o altă vocală.", fg="green")
            # Eliminăm butonul cuvântului corect
            if word in buttons_dict:
                buttons_dict[word].destroy()
                del buttons_dict[word]
            # Resetează selecția vocalei
            selected_vowel.set("")
        else:
            play_sound("wrong")
            feedback_label.config(text="Mai încearcă!", fg="red")

    # Layout-ul pentru vocale
    left_frame = tk.Frame(match_window, bg="#FFE4B5")
    left_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.Y)

    right_frame = tk.Frame(match_window, bg="#FFE4B5")
    right_frame.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.Y)

    # Vocale grupate
    tk.Label(left_frame, text="Vocale", font=("Arial", 20), bg="#FFE4B5").pack(pady=10)
    vowels = [("A", "a"), ("E", "e"), ("I", "i"), ("O", "o"), ("U", "u")]

    for big, small in vowels:
        row_frame = tk.Frame(left_frame, bg="#FFE4B5")
        row_frame.pack(pady=5)

        tk.Button(
            row_frame,
            text=big,
            font=("Arial", 18),
            bg="#F4A460",
            fg="black",
            command=lambda v=big: select_vowel(v),
            width=5
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            row_frame,
            text=small,
            font=("Arial", 18),
            bg="#F4A460",
            fg="black",
            command=lambda v=small: select_vowel(v),
            width=5
        ).pack(side=tk.LEFT, padx=5)

    # Cuvinte în dreapta
    tk.Label(right_frame, text="Cuvinte", font=("Arial", 20), bg="#FFE4B5").pack(pady=10)
    words_frame = tk.Frame(right_frame, bg="#FFE4B5")
    words_frame.pack(pady=10)

    for i, (vowel, word) in enumerate(all_words):
        button = tk.Button(
            words_frame,
            text=word,
            font=("Arial", 18),
            bg="#87CEFA",
            fg="black",
            command=lambda w=word: select_word(w),
            width=10
        )
        button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
        buttons_dict[word] = button  # Salvăm referința la buton

    # Feedback și scor
    feedback_label = tk.Label(match_window, text="", font=("Arial", 16), bg="#FFE4B5", fg="black")
    feedback_label.pack(pady=10)

    score_label = tk.Label(match_window, text="Scor: 0", font=("Karmatic Arcade", 18), bg="#FFE4B5", fg="black")
    score_label.pack(pady=10)
# Funcție pentru acțiunea butonului blocat
def locked_button_action():
    play_locked_message()  # Redăm mesajul audio când jocul este blocat
    messagebox.showinfo("Lacăt",
                        "Trebuie să obții 30 de puncte în jocul de selectare a vocalelor pentru a debloca acest joc!")

# Funcție pentru actualizarea stării butonului de asociere
def update_match_button():
    if score < 2:
        match_button.config(
            text="🔒 Joacă un joc - Asociază cuvântul",
            bg="#FFA07A",
            command=locked_button_action
        )
    else:
        match_button.config(
            text="Joacă un joc - Asociază cuvântul",
            bg="#87CEFA",
            command=play_matching_game
        )

def play_matching_game_with_images():
    match_window = tk.Toplevel(app)
    match_window.title("Joacă - Asociază vocala cu imaginea")
    match_window.geometry("900x600")
    match_window.configure(bg="#FFE4B5")

    # Imagini asociate pentru fiecare vocală
    images = {
        "A": ["arici.png"],  # Exemplu: imagine pentru litera A
        "E": ["elefant.png"],  # Exemplu: imagine pentru litera E
        "I": ["iepure.png"],  # Exemplu: imagine pentru litera I
        "O": ["oaie.png"],  # Exemplu: imagine pentru litera O
        "U": ["urs.png"],  # Exemplu: imagine pentru litera U
    }

    selected_vowel = tk.StringVar()  # Vocală selectată
    current_score = tk.IntVar(value=0)  # Scorul curent
    buttons_dict = {}  # Referințe la butoanele pentru imagini

    # Generăm lista completă de imagini asociate vocalelor
    all_images = [(vowel, image) for vowel, image_list in images.items() for image in image_list]
    random.shuffle(all_images)

    def select_vowel(vowel, feedback_label):
        selected_vowel.set(vowel)
        feedback_label.config(text=f"Ai selectat vocala: {vowel}", fg="blue")
        play_sound(vowel)

    def select_image(image, associated_vowel, feedback_label, score_label):
        vowel = selected_vowel.get()
        if not vowel:
            feedback_label.config(text="Te rog să selectezi mai întâi o vocală!", fg="red")
            play_sound("select_vowel")
            return

        # Verificăm dacă imaginea corespunde cu vocala selectată
        if vowel == associated_vowel:
            play_sound("correct")
            current_score.set(current_score.get() + 1)
            score_label.config(text=f"Scor: {current_score.get()}")
            feedback_label.config(text="Bravo! Ai făcut corect! Selectează o altă vocală.", fg="green")
            # Eliminăm butonul imaginii corecte
            if image in buttons_dict:
                buttons_dict[image].destroy()
                del buttons_dict[image]
            # Resetează selecția vocalei
            selected_vowel.set("")
        else:
            play_sound("wrong")
            feedback_label.config(text="Mai încearcă!", fg="red")

    # Layout-ul pentru vocale
    left_frame = tk.Frame(match_window, bg="#FFE4B5")
    left_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.Y)

    right_frame = tk.Frame(match_window, bg="#FFE4B5")
    right_frame.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.Y)

    # Vocale grupate
    tk.Label(left_frame, text="Vocale", font=("Arial", 20), bg="#FFE4B5").pack(pady=10)
    vowels = ["A", "E", "I", "O", "U"]

    feedback_label = tk.Label(match_window, text="", font=("Arial", 16), bg="#FFE4B5", fg="black")
    feedback_label.pack(pady=10)

    score_label = tk.Label(match_window, text="Scor: 0", font=("Karmatic Arcade", 18), bg="#FFE4B5", fg="black")
    score_label.pack(pady=10)

    for vowel in vowels:
        tk.Button(
            left_frame,
            text=vowel,
            font=("Arial", 18),
            bg="#F4A460",
            fg="black",
            command=lambda v=vowel: select_vowel(v, feedback_label),
            width=5
        ).pack(pady=5)

    # Imagini în dreapta
    tk.Label(right_frame, text="Imagini", font=("Arial", 20), bg="#FFE4B5").pack(pady=10)
    images_frame = tk.Frame(right_frame, bg="#FFE4B5")
    images_frame.pack(pady=10)

    for i, (vowel, image_file) in enumerate(all_images):
        image_path = os.path.join("static/images", image_file)
        try:
            image = tk.PhotoImage(file=image_path)
        except tk.TclError:
            # Placeholder pentru imagine invalidă
            image = tk.PhotoImage(width=100, height=100)
            messagebox.showerror("Eroare", f"Imaginea {image_path} nu este validă sau este coruptă!")

        button = tk.Button(
            images_frame,
            image=image,
            command=lambda img=image_file, v=vowel: select_image(img, v, feedback_label, score_label),
            relief="raised"
        )
        button.image = image  # Stocăm referința imaginii pentru a evita garbage collection
        button.grid(row=i // 3, column=i % 3, padx=10, pady=10)
        buttons_dict[image_file] = button

# Jocul în care utilizatorul trebuie să citească vocala folosind vocea
import speech_recognition as sr

# Jocul de citit vocalele cu vocea
def read_vowel_game_with_voice():
    read_window = tk.Toplevel(app)
    read_window.title("Joacă - Citește vocala cu vocea")
    read_window.geometry("600x400")
    read_window.configure(bg="#FFEDCC")

    vowels = ["A", "E", "I", "O", "U"]  # Lista vocalelor
    current_vowel = tk.StringVar()

    # Funcție pentru generarea unei vocale noi
    def generate_new_vowel():
        current_vowel.set(random.choice(vowels))
        vowel_label.config(text=current_vowel.get())
        feedback_label.config(text="Vorbește clar și spune vocala!")

    # Funcție pentru înregistrare audio
    def record_audio(duration=3, samplerate=16000):
        try:
            feedback_label.config(text="Ascultând... Vorbește clar!", fg="blue")
            audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
            sd.wait()  # Așteaptă să termine înregistrarea
            return np.array(audio_data, dtype='int16').tobytes()
        except Exception as e:
            feedback_label.config(text="Eroare la înregistrare: Verifică microfonul!", fg="red")
            return None

    # Funcție pentru recunoașterea vocii
    def recognize_speech():
        audio_bytes = record_audio()
        if audio_bytes:
            try:
                recognizer = sr.Recognizer()
                audio_data = sr.AudioData(audio_bytes, 16000, 2)
                recognized_text = recognizer.recognize_google(audio_data, language="ro-RO").upper()
                check_reading(recognized_text)
            except sr.UnknownValueError:
                feedback_label.config(text="Nu am înțeles. Încearcă din nou!", fg="red")
                play_sound("wrong")
            except sr.RequestError:
                feedback_label.config(text="Eroare de conectare la serviciul de recunoaștere vocală.", fg="red")

    # Funcție pentru verificarea răspunsului
    def check_reading(user_input):
        if user_input == current_vowel.get():
            play_sound("correct")
            feedback_label.config(text="Bravo! Ai citit corect!", fg="green")
            generate_new_vowel()
        else:
            play_sound("wrong")
            feedback_label.config(
                text=f"Nu ai citit corect. Ai spus: {user_input}, dar vocala este: {current_vowel.get()}",
                fg="red"
            )

    # Eticheta cu vocala curentă
    vowel_label = tk.Label(
        read_window,
        text="",
        font=("Arial", 50),
        bg="#FFEDCC",
        fg="black",
        pady=20
    )
    vowel_label.pack()

    # Buton pentru a începe recunoașterea vocii
    start_button = tk.Button(
        read_window,
        text="Citește cu voce tare",
        font=("Arial", 16),
        bg="#87CEFA",
        fg="black",
        command=recognize_speech
    )
    start_button.pack(pady=20)

    # Eticheta pentru feedback
    feedback_label = tk.Label(
        read_window,
        text="",
        font=("Arial", 16),
        bg="#FFEDCC",
        fg="black"
    )
    feedback_label.pack(pady=20)

    # Generăm prima vocală
    generate_new_vowel()


def play_sound(file_name):
    sound_path = f"static/sounds/{file_name}.mp3"
    try:
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()
    except pygame.error:
        messagebox.showerror("Eroare", f"Fișierul audio {file_name}.mp3 nu a fost găsit!")

def drag_and_drop_game():
    # Configurare fereastră principală
    drag_window = tk.Toplevel(app)
    drag_window.title("Joacă - Drag and Drop")
    drag_window.geometry("1000x800")
    drag_window.configure(bg="#FFFACD")

    baskets = ["A", "E", "I", "O", "U"]  # Lista vocalelor
    score = tk.IntVar(value=0)  # Variabilă pentru scor

    # Feedback și scor
    feedback_label = tk.Label(
        drag_window, text="Trage vocala în coșul corect!", font=("Arial", 16), bg="#FFFACD", fg="black"
    )
    feedback_label.pack(pady=10)

    score_label = tk.Label(
        drag_window, text="Scor: 0", font=("Karmatic Arcade", 16), bg="#FFFACD", fg="black"
    )
    score_label.pack(pady=10)

    # Creăm coșurile
    basket_frame = tk.Frame(drag_window, bg="#FFFACD")
    basket_frame.pack(side=tk.BOTTOM, pady=20)

    baskets_dict = {}
    for basket in baskets:
        basket_label = tk.Label(
            basket_frame,
            text=basket,
            font=("Arial", 18),
            bg="#FFD700",
            width=10,
            height=2,
            relief="solid",
        )
        basket_label.pack(side=tk.LEFT, padx=10)
        baskets_dict[basket] = basket_label

    # Funcție pentru mutarea widget-ului (drag)
    def on_drag(event):
        widget = event.widget
        widget.place(x=event.x_root - drag_window.winfo_rootx() - 25,
                     y=event.y_root - drag_window.winfo_rooty() - 25)

    # Funcție pentru plasare (drop)
    def on_drop(event, vowel_widget):
        x, y = vowel_widget.winfo_x(), vowel_widget.winfo_y()  # Coordonatele vocalei
        placed = False

        for basket, basket_label in baskets_dict.items():
            # Coordonatele coșului
            bx1, by1 = basket_label.winfo_rootx(), basket_label.winfo_rooty()
            bx2, by2 = bx1 + basket_label.winfo_width(), by1 + basket_label.winfo_height()

            # Verificăm dacă vocala este plasată în interiorul coșului
            if bx1 <= x <= bx2 and by1 <= y <= by2:
                if basket == vowel_widget.vowel:
                    play_sound("correct")
                    feedback_label.config(text="Bravo! Ai plasat corect!", fg="green")
                    score.set(score.get() + 1)
                    score_label.config(text=f"Scor: {score.get()}")
                    vowel_widget.destroy()
                    placed = True
                else:
                    play_sound("wrong")
                    feedback_label.config(text="Mai încearcă!", fg="red")
                break

        if not placed:
            feedback_label.config(text="Nu ai plasat vocala în coșul corect!", fg="red")

    # Generăm vocale pentru drag-and-drop
    def generate_vowels():
        vowels_to_drag = []  # Stocăm vocalele generate

        for _ in range(5):
            vowel = random.choice(baskets)
            vowel_label = tk.Label(
                drag_window, text=vowel, font=("Arial", 20), bg="#ADD8E6", relief="raised"
            )
            vowel_label.place(x=random.randint(50, 700), y=random.randint(50, 300))
            vowel_label.vowel = vowel

            # Asocieri pentru drag and drop
            vowel_label.bind("<B1-Motion>", on_drag)  # Drag
            vowel_label.bind("<ButtonRelease-1>", lambda e, v=vowel_label: on_drop(e, v))  # Drop
            vowels_to_drag.append(vowel_label)

        return vowels_to_drag

    vowels_to_drag = generate_vowels()

    # Funcție pentru terminarea jocului
    def check_end_game():
        if not vowels_to_drag:  # Dacă toate vocalele au fost plasate
            messagebox.showinfo("Felicitări", f"Ai terminat jocul cu scorul {score.get()}!")
            drag_window.destroy()

    drag_window.after(500, check_end_game)

# Create the main window
app = tk.Tk()
app.title("Învățăm Vocalele")
app.geometry("1200x800")
app.configure(bg="#26a0e9")

# Global variable for debounce delay
resize_job = None


# Function to resize and set the background image dynamically
def resize_background(event):
    global resize_job

    # Cancel any pending resize operations
    if resize_job:
        app.after_cancel(resize_job)

    # Schedule a new resize operation after 100ms
    resize_job = app.after(100, perform_resize, event.width, event.height)


def perform_resize(width, height):
    # Resize the image to match the new window size
    resized_image = original_image.resize((width, height), resample=Image.Resampling.LANCZOS)  # Updated resampling method
    tk_image = ImageTk.PhotoImage(resized_image)

    # Update the label with the resized image
    background_label.config(image=tk_image)
    background_label.image = tk_image  # Keep a reference to prevent garbage collection


# Load the background image with PIL
original_image = Image.open("static/images/main-menu-background-4k-float.gif")  # Use your image path here
tk_image = ImageTk.PhotoImage(original_image)

# Set the initial background image
background_label = tk.Label(app, image=tk_image)
background_label.place(relwidth=1, relheight=1)  # Set to cover the entire window

# Bind the resize event to dynamically handle window resizing
app.bind("<Configure>", resize_background)

score = 0

# Welcome label with sound on click using the Super Shiny font
try:
    # Attempt to load the custom "Super Shiny" font
    custom_font = font.Font(family="Super Morning", size=24)  # Set font family and size
except tk.TclError:
    # Fallback if the font fails to load
    print("Could not load 'Super Morning' font. Ensure it's installed correctly.")
    custom_font = ("Arial", 20)  # Fallback font

welcome_label = tk.Label(
    app,
    text="Bine ai venit! Să învățăm vocalele! 🔊",
    font=custom_font,
    bg="#26a0e9",
    fg="black",
    pady=10,
    cursor="hand2",
)
welcome_label.pack()

# Play a sound when the welcome label is clicked
welcome_label.bind("<Button-1>", lambda event: play_sound("welcome"))

# Function to create a button with sound functionality
def create_button(parent, text, bg_color, command, sound_name):
    button = tk.Button(
        parent,
        text=text,
        font=("Arial", 16),
        bg=bg_color,
        fg="black",
        command=lambda: [play_sound(sound_name), command()]  # Play sound and execute action
    )
    return button

# Buttons with associated sounds
learn_button = create_button(app, "Mod de învățare prin ascultare", "#87CEFA", learn_vowels, "learn")
learn_button.pack(pady=10)

draw_button = create_button(app, "Mod de învățare prin desenare", "#FFB6C1", learn_by_drawing, "draw")
draw_button.pack(pady=10)

game_button = create_button(app, "Joacă un joc - Selectează vocala", "#90EE90", play_game, "game")
game_button.pack(pady=10)

match_button = create_button(app, "🔒 Joacă un joc - Asociază cuvântul", "#FFA07A", locked_button_action, "match")
match_button.pack(pady=10)

image_match_button = create_button(app, "Joacă un joc - Asociază cu imaginea", "#87CEFA", play_matching_game_with_images, "image_match")
image_match_button.pack(pady=10)

read_vowel_voice_button = create_button(app, "Joacă un joc - Citește vocala cu vocea", "#FFA07A", read_vowel_game_with_voice, "read_voice")
read_vowel_voice_button.pack(pady=10)

drag_and_drop_button = create_button(app, "Joacă un joc - Drag & Drop", "#FFD700", drag_and_drop_game, "drag_drop")
drag_and_drop_button.pack(pady=10)

exit_button = create_button(app, "Ieși", "#FF6961", app.quit, "exit")
exit_button.pack(pady=10)

app.mainloop()
