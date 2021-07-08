from tkinter import Canvas

BACKGROUND_COLOR = "#B1DDC6"

class flashCard(Canvas):
    def __init__(self, image, language, word, color):
        super().__init__()
        self.config(width=820, height=550, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.change_image(image, language, word, color)

    def change_image(self, image, language, word, color):
        '''Changes the flashCard: 
        Image must be a tk.PhotoImage, all other args are strings.'''

        self.create_image(410, 275, image=image)
        self.create_text(400, 150, text=language, fil=color, font=("Arial", 40, "italic"))
        self.create_text(400, 300, text=word, fill=color, font=("Arial", 60, "bold"))