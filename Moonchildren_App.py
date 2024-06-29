import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import ephem # to generate lunar information
from datetime import datetime
import random
import pygame #to create a music player

# Initialize pygame for music player
pygame.mixer.init()

# the list of the facts about the moon which will be randomly given to the user
moon_facts = [
    "Selenophile: (n.) a person who loves the moon 🌝",
    "The Moon is moving approximately 3.8 cm away from our planet every year 🌏",
    "The moon probably formed in a giant collision 💥",
    "The moon produces and changes the tides 🌊",
    "The moon's appearance can be affected by Earthshine 🌍",
    "The moon's surface is covered in craters 🌑",
    "Water exists on the moon in the form of ice, particularly in permanently shadowed craters at the lunar poles ❄️",
    "Unlike Earth, the moon does not have a global magnetic field 🧲",
    "In astrology, moonchild is often used to refer to someone born under the zodiac sign of Cancer ♋",
    "In popular culture, moonchild can symbolize someone who feels a strong connection to the moon, nature, and night🌙"
]

# the list of some myths about the moon which will be randomly given to the user
moon_mythology = [
    "In Greek mythology 🏛, Selene was the moon goddess. She was often depicted as riding a chariot across the night sky,"
    "Many Native American tribes have stories about the moon. For example, "
    "the Cree have a legend where the moon spirit transforms a young woman into a rabbit. "
    "This rabbit is seen in the moon's shadows, often referred to as the man in the moon in Western cultures.",
    "In Norse mythology 🌌, Máni was the personification of the moon. "
    "He was the brother of the sun goddess, Sol. Máni rode a chariot across the night sky, guiding the moon’s path.",
    "Chinese mythology 🏮 features the story of Chang’e, who drank an elixir of immortality and ascended to the moon. "
    "There, she resides with a jade rabbit, pounding the elixir of life. "
    "The moon rabbit is a symbol of selflessness and sacrifice.",
    "Chandra Dev 🛕, also known as Soma, is a lunar deity in Hindu mythology. "
    "He rides a chariot pulled by ten white horses or an antelope. "
    "Chandra is also associated with the nectar of immortality "
    "and is one of the Navagrahas (nine planets) in Hindu astrology."
]

# List of songs with their paths and descriptions and their relation to moon
songs = [
    {"file": "Music/Moonchild.mp3",
     "description": "Moonchild: Written and performed by RM. The song deals with themes of finding solace and identity "
                    "under the moonlight, often addressing feelings of loneliness and introspection. RM in this song"
                    "tries to comfort people who are dealing with these feelings and reassures them that as the moon "
                    "shines everynight, everything will be alright."},
    {"file": "Music/Moonlight.mp3",
     "description": "Moonlight: Written and performed by Agust D. This song conveys a message of self-reflection "
                    "and resilience.The song explores the artist's journey, highlighting the challenges and triumphs "
                    "he has faced. A relatable song for everyone. It delves into the pressures of fame, personal "
                    "insecurities, and the importance of staying true to oneself. Despite the hardships, the song "
                    "emphasizes growth, perseverance, and finding hope in the face of adversity, symbolized by "
                    "the guiding light of the moon. "},
    {"file": "Music/Moonlight Sonata.mp3",
     "description": "Moonlight Sonata: By Ludwig van Beethoven, while not a song with lyrics, conveys a profound "
                    "emotional journey through its music. The piece expresses a range of deep emotions, from the "
                    "tranquil and introspective mood of the first movement to the more playful and lyrical second "
                    "movement, culminating in the passionate and turbulent third movement. The sonata evokes a sense of"
                    "melancholy, longing, and intense drama, capturing the complexities of the human experience through"
                    " its evocative melodies and dynamic contrasts. Its timeless beauty continues to move listeners, "
                    "offering a musical reflection on the depths of emotion and the power of expression."},
    {"file": "Music/Moonflower.mp3",
     "description": "Moonflower: by Michael Hoppé is an instrumental piece that conveys a serene and contemplative mood"
                    " through its gentle melodies and soothing harmonies. The music evokes a sense of tranquility and "
                    "introspection, akin to the delicate beauty of a moonlit night. Through its serene and flowing "
                    "composition, Moonflower invites listeners to reflect, relax, and find peace, capturing the essence"
                    " of quiet beauty and the delicate, ephemeral nature of life. The piece is often appreciated for "
                    "its ability to evoke emotional calmness and a meditative state, offering a musical escape from"
                    " the chaos of daily life."}
]


# Function to calculate moon phase based on user input date
def calculate_moon_phase():
    date_str = date_entry.get()
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d") #change the format of date input
        observer = ephem.Observer()
        observer.date = date
        moon = ephem.Moon(observer)
        phase = moon.phase
    #definigng every moon phase and assigning an image to each one of them to visualize it
        if phase < 1.84566:
            moon_phase_name = "New Moon 🌑"
            image_path = "images/new_moon.png"
        elif phase < 5.53699:
            moon_phase_name = "Waxing Crescent 🌒"
            image_path = "images/waxing_crescent.png"
        elif phase < 9.22831:
            moon_phase_name = "First Quarter 🌓"
            image_path = "images/first_quarter.png"
        elif phase < 12.91963:
            moon_phase_name = "Waxing Gibbous 🌔"
            image_path = "images/waxing_gibbous.png"
        elif phase < 16.61096:
            moon_phase_name = "Full Moon 🌕"
            image_path = "images/full_moon.png"
        elif phase < 20.30228:
            moon_phase_name = "Waning Gibbous 🌖"
            image_path = "images/waning_gibbous.png"
        elif phase < 23.99361:
            moon_phase_name = "Last Quarter 🌗"
            image_path = "images/last_quarter.png"
        else:
            moon_phase_name = "Waning Crescent 🌘"
            image_path = "images/waning_crescent.png"

        result_label.configure(text=f"Moon Phase on {date_str}: {phase:.2f}% ({moon_phase_name})")

        # Load and resize the moon images
        moon_phase_image = Image.open(image_path)
        moon_phase_image = moon_phase_image.resize((200, 200), Image.LANCZOS)
        moon_phase_photo = ImageTk.PhotoImage(moon_phase_image)

        # Check if there's already a canvas, delete it if exists
        if hasattr(calculate_moon_phase, 'canvas'):
            calculate_moon_phase.canvas.delete('all')
        else:
            # Create a canvas for the moon phase image
            calculate_moon_phase.canvas = tk.Canvas(moon_phase_frame, width=200, height=200)
            calculate_moon_phase.canvas.place(x=690, y=260)

        # Display the image on the canvas
        calculate_moon_phase.canvas.create_image(0, 0, anchor='nw', image=moon_phase_photo)
        calculate_moon_phase.canvas.image = moon_phase_photo  # Keep a reference to avoid garbage collection

    except ValueError:
        result_label.configure(text="Invalid date format. Please use YYYY-MM-DD.")

# Function to display random moon fact
def display_random_fact():
    fact = random.choice(moon_facts)
    fact_label.configure(text=f"{fact}")

# Function to display random moon mythology
def display_random_mythology():
    myth = random.choice(moon_mythology)
    mythology_label.configure(text=f"{myth}")

# Function to play music and display song description
def play_music(song):
    pygame.mixer.music.load(song['file'])
    pygame.mixer.music.play()
    song_description_label.configure(text=song['description'])

#creating a function to stop the music
def stop_music():
    pygame.mixer.music.stop()
    song_description_label.configure(text="")

#function to get Lunar information based on the given date
def display_lunar_events():
    date_str = calendar_date_entry.get()
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        observer = ephem.Observer()
        observer.date = date
        moon = ephem.Moon(observer)
        phase = moon.phase
        illumination = moon.phase
        rise_time = ephem.localtime(moon.rise_time).strftime("%H:%M") if moon.rise_time else "N/A"
        set_time = ephem.localtime(moon.set_time).strftime("%H:%M") if moon.set_time else "N/A"

        lunar_events_text = (f"Date: {date_str}\n"
                             f"Moon Phase: {phase:.2f}%\n"
                             f"Illumination: {illumination:.2f}%\n"
                             f"Moonrise: {rise_time}\n"
                             f"Moonset: {set_time}")
        calendar_label.configure(text=lunar_events_text)
    except ValueError:
        calendar_label.configure(text="Invalid date format. Please use YYYY-MM-DD.")

# Create main application window
app = ctk.CTk()
app.title("Moonchildren")
app.geometry("950x680")  # Set the default size of the window

# Function to set background image
def set_background(frame, image_path):
    bg_image = Image.open(image_path)
    bg_image = bg_image.resize((950, 680), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    canvas = tk.Canvas(frame, width=950, height=680)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
    canvas.bg_photo = bg_photo  # Keep a reference to avoid garbage collection
    return canvas

# Create a frame for each page
frames = {}
for F in ('Welcome', 'MoonPhase', 'MoonFacts', 'MoonMythology', 'Music', 'LunarCalendar'):
    frame = ctk.CTkFrame(app, width=850, height=680)
    frames[F] = frame
    frame.grid(row=0, column=0, sticky="nsew")

    # making sure the same backgrounds is applied to all frames
    set_background(frame, "images/Moonlight.png")

# Function to show a frame
def show_frame(frame_name):
    frame = frames[frame_name]
    frame.tkraise()

# Centering widgets on each frame
def center_widget(widget, relx=0.5, rely=0.5):
    widget.place(relx=relx, rely=rely, anchor='center')

# Welcome page
welcome_frame = frames['Welcome']
welcome_label = ctk.CTkLabel(welcome_frame, text="Hello Moonchild 🌙", font=('Courier', 24))
center_widget(welcome_label)
start_button = ctk.CTkButton(welcome_frame, text="Let's take you to the galaxy",
                             command=lambda: show_frame('MoonPhase'),
                             fg_color="#5A9", hover_color="#4A8", text_color="#FFF")
center_widget(start_button, rely=0.6)

# Moon phase page functions
moon_phase_frame = frames['MoonPhase']
moon_phase_label = ctk.CTkLabel(moon_phase_frame, text="Let's see how the moon looked like on any day",
                                font=('courier', 22 , 'italic'))
center_widget(moon_phase_label, rely=0.2)
#making a date entry input for the user
date_entry_label = ctk.CTkLabel(moon_phase_frame, text="Enter Date (YYYY-MM-DD)📅:", font=('courier', 18 , 'italic'))
center_widget(date_entry_label, rely=0.35)
date_entry = ctk.CTkEntry(moon_phase_frame, width=200)
center_widget(date_entry, rely=0.4)
#making the moon phase calculator button and giving it the command
calculate_button = ctk.CTkButton(moon_phase_frame, text="Calculate Moon Phase 🧮", command=calculate_moon_phase,
                                 fg_color="#5A9", hover_color="#4A8", text_color="#FFF")
center_widget(calculate_button, rely=0.45)
result_label = ctk.CTkLabel(moon_phase_frame, text="", font=('Helvetica', 18))
result_label.place (x= 160, y= 350)
#creating a button that directs the user to the facts page
facts_button = ctk.CTkButton(moon_phase_frame, text="Moon Facts 📖", command=lambda: show_frame('MoonFacts'),
                             fg_color="#5A9", hover_color="#4A8", text_color="#FFF")
center_widget(facts_button, rely=0.65)
#creating a button that directs the user to the mythologies page
mythology_button = ctk.CTkButton(moon_phase_frame, text="Moon Mythology 🔮", command=lambda: show_frame('MoonMythology'),
                                 fg_color="#5A9", hover_color="#4A8", text_color="#FFF")
center_widget(mythology_button, rely=0.7)
#creating a button that directs the user to the music page
music_button = ctk.CTkButton(moon_phase_frame, text="Music 🎶", command=lambda: show_frame('Music'),
                             fg_color="#5A9", hover_color="#4A8", text_color="#FFF")
center_widget(music_button, rely=0.75)
#creating a button that directs the user to the lunar calendar page
calendar_button = ctk.CTkButton(moon_phase_frame, text="Lunar Calendar 📅", command=lambda: show_frame('LunarCalendar'),
                                fg_color="#5A9", hover_color="#4A8", text_color="#FFF")
center_widget(calendar_button, rely=0.8)

# designing the moon facts page
moon_facts_frame = frames['MoonFacts']
moon_facts_label = ctk.CTkLabel(moon_facts_frame, text="Moon Facts", font=('courier', 23 , 'italic'))
center_widget(moon_facts_label, rely=0.2)
#create a button that randomly gives one of the moon facts
fact_button = ctk.CTkButton(moon_facts_frame, text="Get Random Fact⁉️", command=display_random_fact,
                            fg_color="#5A9", hover_color="#4A8", text_color="#FFF")
center_widget(fact_button, rely=0.45)
fact_label = ctk.CTkLabel(moon_facts_frame, text="", font=('Helvetica', 18))
center_widget(fact_label, rely=0.55)
#creat a back button so the user can go back to the main page again
back_button1 = ctk.CTkButton(moon_facts_frame, text="Back", command=lambda: show_frame('MoonPhase'),
                             fg_color="#5A9", hover_color="#4A8", text_color="#FFF")
center_widget(back_button1, rely=0.65)

# designing the mythologies page
moon_mythology_frame = frames['MoonMythology']
moon_mythology_label = ctk.CTkLabel(moon_mythology_frame, text="Moon Mythology", font=('courier', 23 , 'italic'))
center_widget(moon_mythology_label, rely=0.2)
mythology_button = ctk.CTkButton(moon_mythology_frame, text="Get Random Mythology ‍♆🌩", command=display_random_mythology,
                                 fg_color="#5A9", hover_color="#4A8", text_color="#FFF")
mythology_label = ctk.CTkLabel(moon_mythology_frame, text="", font=('courier', 17 , 'italic'))
center_widget(mythology_label, rely=0.55)
mythology_button.place(x= 550, y= 500)

# Set wraplength to wrap text at 400 pixels and set the width (in order to make sure the texts won't appear in one line)
mythology_label = ctk.CTkLabel(moon_mythology_frame, text="",
                               font=('courier', 18 , 'italic'), wraplength=400, width=400)
center_widget(mythology_label, rely=0.55)
back_button2 = ctk.CTkButton(moon_mythology_frame, text="Back", command=lambda: show_frame('MoonPhase'),
                             fg_color="#5A9", hover_color="#4A8", text_color="#FFF")
back_button2.place(x= 250, y= 500)

# designing the music page
music_frame = frames['Music']
music_label = ctk.CTkLabel(music_frame, text="Music Player ♬", font=('courier', 23 , 'italic'))
center_widget(music_label, rely=0.2)

# Load an image for every song button
play_images = [
    ImageTk.PhotoImage(Image.open("images/Moonchild.jpeg").resize((40, 40))),
    ImageTk.PhotoImage(Image.open("images/MoonlightD2.png").resize((40, 40))),
    ImageTk.PhotoImage(Image.open("images/MoonlightSonata.jpg").resize((40, 40))),
    ImageTk.PhotoImage(Image.open("images/Moonflower.jpg").resize((40, 40)))
]
#loading images for the stop and back button
stop_image = ImageTk.PhotoImage(Image.open("images/Pause.jpg").resize((40, 40)))
back_image = ImageTk.PhotoImage(Image.open("images/starsBG.jpg").resize((40, 40)))

#locating every song button
positions = [
    {"x": 200, "y": 280},
    {"x": 590, "y": 280},
    {"x": 200, "y": 380},
    {"x": 590, "y": 380}
]

# Create buttons for each song
for idx, song in enumerate(songs):
    song_button = ctk.CTkButton(music_frame, text=f"{song['description'].split(':')[0]}",
                                command=lambda s=song: play_music(s),image=play_images[idx],
                                compound="left",fg_color="#5A9", hover_color="#4A8", text_color="#FFF")
    #defining positions to be able to relocate where every button appears
    song_button.place(x=positions[idx]["x"], y=positions[idx]["y"])

# displaying every song description and making a wraplength to make sure the descriptions don't run out of the screen
song_description_label = ctk.CTkLabel(music_frame, text="", font=('courier', 18, 'italic'), wraplength=600)
center_widget(song_description_label, rely=0.80)

#creating a stop music button
stop_button = ctk.CTkButton(music_frame, text="Stop Music", command=stop_music,
                            image=stop_image, compound="left",
                            fg_color="#D55", hover_color="#C44", text_color="#FFF")
stop_button.place(x= 410, y= 320)
back_button3 = ctk.CTkButton(music_frame, text="Back", command=lambda: show_frame('MoonPhase'),
                             image=back_image, compound="left",
                             fg_color="#5A9", hover_color="#4A8", text_color="#FFF")
back_button3.place(x= 410, y= 370)

# designing the lunar calendar page
lunar_calendar_frame = frames['LunarCalendar']
lunar_calendar_label = ctk.CTkLabel(lunar_calendar_frame, text="Let's see what the future is like",
                                    font=('courier', 24 , 'italic'))
center_widget(lunar_calendar_label, rely=0.2)
calendar_date_entry_label = ctk.CTkLabel(lunar_calendar_frame, text="Enter Date (YYYY-MM-DD):",
                                         font=('courier', 23 , 'italic'))
center_widget(calendar_date_entry_label, rely=0.35)
calendar_date_entry = ctk.CTkEntry(lunar_calendar_frame, width=200)
center_widget(calendar_date_entry, rely=0.4)
generate_calendar_button = ctk.CTkButton(lunar_calendar_frame, text="Get Lunar Events", command=display_lunar_events,
                                         fg_color="#5A9", hover_color="#4A8", text_color="#FFF")
center_widget(generate_calendar_button, rely=0.45)
calendar_label = ctk.CTkLabel(lunar_calendar_frame, text="", font=('courier', 17 , 'italic'), wraplength=600)
center_widget(calendar_label, rely=0.55)
back_button4 = ctk.CTkButton(lunar_calendar_frame, text="Back", command=lambda: show_frame('MoonPhase'),
                             fg_color="#5A9", hover_color="#4A8", text_color="#FFF")
center_widget(back_button4, rely=0.7)

# Show the welcome frame initially
show_frame('Welcome')

# Start the application
app.mainloop()