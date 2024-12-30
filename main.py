from tkinter import *
from PIL import Image, ImageTk

from Book import Book
from CreateEvent import CreateEvent
from ViewTickets import ViewTickets
from ViewEvents import ViewEvents
from CancelTicket import CancelTicket
from JoggingRoute import JoggingRoute
from FacilitiesLocation import FacilitiesLocation

# Initialize the main application window
top = Tk()
top.title('Sports Tracker & Event Booking UMPSA')
top.geometry('800x600')  # Set initial window size
top.state('zoomed')  # Make the window fullscreen

# Load and resize the background image to fit the full window
def load_fullscreen_image(file_path):
    screen_width = top.winfo_screenwidth()
    screen_height = top.winfo_screenheight()
    img = Image.open(file_path)
    img = img.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)

# Load the background image
bg_image = load_fullscreen_image("C:/Users/HANIF/Downloads/trackimage.png")

# Set the background image
bg_label = Label(top, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Stretch to fill the entire screen

# Define the dark color
dark_color = "black"  # Use a dark gray color

# Header Section
header_frame = Frame(top, bg=dark_color, bd=0)  # Changed to dark color
header_frame.pack(fill=X, pady=10)

header_label = Label(header_frame, text="SPORTS TRACKER & EVENT BOOKING\nUMPSA", font=('Times', 25, 'bold'), bg="#191970", fg="white")  # Text in white
header_label.pack()

# SECTION 1
icon_frame = Frame(top, bg=dark_color, bd=0)  # Changed to dark color
icon_frame.pack(pady=20)

button_texts = [
    'Join Event', 'Create Event', 'Participants',
    'View Events', 'Cancel', 'Jogging Route', 'Facilities Location'
]
button_commands = [
    Book, CreateEvent, ViewTickets, ViewEvents, CancelTicket, JoggingRoute, FacilitiesLocation
]

for i in range(len(button_texts)):
    Button(icon_frame, text=button_texts[i], font=('Arial', 12), width=20, height=2, bg='#191970', fg='white', command=button_commands[i]).grid(row=i // 2, column=i % 2, padx=10, pady=10)

# SECTION 2
content_frame = Frame(top, bg=dark_color, bd=0)  # Changed to dark color
content_frame.pack(pady=20)

Label(content_frame, text="Join the action!", font=('Arial', 14, 'bold'), bg=dark_color, fg="white", anchor=W).pack(fill=X, padx=10, pady=5)

card_texts = [
    "Upcoming & Trending",
    "Fitness Journey",
    "How To Stay Fit?",
]

card_commands = [
    None,None,None
]

card_frame = Frame(content_frame, bg=dark_color)  # Changed to dark color
card_frame.pack(pady=10)

for i in range(len(card_texts)):
    Button(
        card_frame,
        text=card_texts[i],
        font=('Arial', 12),
        bg='#191970',
        fg="white",
        width=25,
        height=5,
        relief=GROOVE,
        command=card_commands[i]
    ).grid(row=0, column=i, padx=10, pady=10)

# SECTION 3 (FOOTER)
footer_frame = Frame(top, bg=dark_color, bd=0)  # Changed to dark color
footer_frame.pack(side=BOTTOM, fill=X, pady=10)

footer_texts = ['Home', 'Explore', 'Book', 'Upcoming', 'Profile']
footer_commands = [None, None, None, None, None]

for i in range(len(footer_texts)):
    Button(footer_frame, text=footer_texts[i], font=('Arial', 10), width=15, bg='#191970', fg='white', command=footer_commands[i]).grid(row=0, column=i, padx=5, pady=5)

# Run the application
top.mainloop()
