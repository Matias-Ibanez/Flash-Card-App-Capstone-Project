BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
from tkinter import PhotoImage
from MVC.controller.flashcard_controller import FlashCardController
from paths import CARD_FRONT_PATH, CARD_BACK_PATH, RIGHT_IMAGE_PATH, WRONG_IMAGE_PATH

class FlashCardApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Flash Card")
        self.root.configure(padx=25, pady=25, bg=BACKGROUND_COLOR)
        self.root.geometry("1000x700")
        self.root.resizable(False, False)
        self.center_window()

        self.start_screen = Frame(self.root, bg=BACKGROUND_COLOR)
        self.start_screen.place(relwidth=1, relheight=1)

        title = Label(self.start_screen, text="Flash Cards", font=("Impact", 60), bg=BACKGROUND_COLOR)
        title.pack(pady=50, padx=50)

        start_btn = Button(self.start_screen, text="Start", font=("Arial", 20), command=self.start_game)
        start_btn.pack()

        self.root.mainloop()

    def start_game(self):
        self.start_screen.place_forget()
        self.setup_flashcard_ui()
        self.change_card()

    def setup_flashcard_ui(self):
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        self.card_front = PhotoImage(file=CARD_FRONT_PATH)
        self.card_back = PhotoImage(file=CARD_BACK_PATH)
        self.right_image = PhotoImage(file=RIGHT_IMAGE_PATH)
        self.wrong_image = PhotoImage(file=WRONG_IMAGE_PATH)

        self.canvas = Canvas(self.root, width=800, height=526)
        self.canvas_image = self.canvas.create_image(400, 263, image=self.card_front)
        self.title_text = self.canvas.create_text(400, 150, text="English", font=("Arial", 48, "italic"))
        self.word_text = self.canvas.create_text(400, 263, text="day", font=("Arial", 60, "bold"), fill="black")
        self.canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=2, sticky="n")

        self.btn_right = Button(self.root, image=self.right_image, highlightthickness=0, borderwidth=0, relief="flat",
                                activebackground=BACKGROUND_COLOR, command=self.save_card)
        self.btn_wrong = Button(self.root, image=self.wrong_image, highlightthickness=0, borderwidth=0, relief="flat",
                                activebackground=BACKGROUND_COLOR, command=self.change_card)

        self.btn_right.grid(row=1, column=1)
        self.btn_wrong.grid(row=1, column=0)

    def center_window(self):
        self.root.update_idletasks()
        ancho = self.root.winfo_width()
        alto = self.root.winfo_height()
        pantalla_ancho = self.root.winfo_screenwidth()
        pantalla_alto = self.root.winfo_screenheight()

        x = (pantalla_ancho // 2) - (ancho // 2)
        y = (pantalla_alto // 2) - (alto // 2)

        self.root.geometry(f"+{x}+{y}")

    def hide_start_screen(self):
        self.start_screen.place_forget()
        self.change_card()

    def change_card(self):
        new_card = FlashCardController.get_random_word()
        self.current_english_word = new_card
        self.canvas.itemconfig(self.word_text, text=new_card)
        self.canvas.itemconfig(self.canvas_image, image=self.card_front)
        self.canvas.itemconfig(self.word_text, text=new_card, fill="black")
        self.canvas.itemconfig(self.title_text, text="English", fill="black")
        self.btn_right.config(state="disabled")
        self.btn_wrong.config(state="disabled")
        self.time()

    def time(self):
        self.root.after(3000, self.flip_card)

    def flip_card(self):
        current_word = self.canvas.itemcget(self.word_text, "text")
        word_in_spanish = FlashCardController.get_translation(current_word)
        self.canvas.itemconfig(self.canvas_image, image =self.card_back)
        self.canvas.itemconfig(self.word_text, text = word_in_spanish, fill = "white")
        self.canvas.itemconfig(self.title_text, text="Spanish", fill="white")
        self.btn_right.config(state="normal")
        self.btn_wrong.config(state="normal")
        self.btn_right.grid()
        self.btn_wrong.grid()

    def save_card(self):
        FlashCardController.update_csv(self.current_english_word)
        self.change_card()

