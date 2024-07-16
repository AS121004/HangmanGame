import tkinter as tk
import random

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.master.geometry("900x650")
        self.master.configure(bg='light blue')
        
        self.category_list = ['Coding Language', 'Car Company', 'Cricket Team', 'Smartphones', 'Laptops', 'Kitchen Item', 'Living Room Stuff', 'Home Office Item', 'Men Clothing', 'Women Clothing', 'Sportswear', 'Clothing Accessories', 'Footwear', 'Outerwear', 'Fruit', 'Vegetable', 'Snack', 'Dairy', 'Meat', 'Seafood', 'Beverages', 'Outdoor Sport', 'Water Sports Equipment', 'Team Sports Equipment']
        self.category_word_list = {
            'Coding Language': ["Python", "JavaScript", "Java", "Ruby", "PHP", "Swift", "Kotlin", "R", "Go", "TypeScript", "Perl", "Scala", "Dart", "Rust", "Elixir", "Haskell", "MATLAB"],
            'Car Company': ["Toyota", "Volkswagen", "Ford", "Honda", "Chevrolet", "BMW", "MercedesBenz", "Audi", "Nissan", "Hyundai", "Kia", "Tesla", "Subaru", "Mazda", "Porsche", "Jaguar", "LandRover", "Volvo", "Fiat", "Mitsubishi"],
            'Cricket Team': ["India", "Australia", "England", "Pakistan", "SouthAfrica", "NewZealand", "WestIndies", "SriLanka", "Bangladesh", "Afghanistan", "Zimbabwe", "Ireland", "Scotland", "Netherlands", "UAE", "Nepal", "Oman", "Namibia", "USA"],
            
            "Smartphones": ["iPhone", "SamsungGalaxy", "GooglePixel", "OnePlus", "SonyXperia", "HuaweiMate", "XiaomiMi"],
            "Laptops": ["MacBookPro", "DellXPS", "HPSpectre", "LenovoThinkPad", "AsusZenBook", "AcerPredator", "MicrosoftSurface"],

            "Kitchen Item": ["Refrigerator", "Microwave", "Dishwasher", "Oven", "CoffeeMaker", "Blender", "Toaster", "SlowCooker"],
            "Living Room Stuff": ["Television", "SoundSystem", "AirConditioner", "SmartSpeaker",  "VacuumCleaner", "Fan"],
            "Home Office Item": ["Printer", "Scanner", "DeskLamp", "PaperShredder", "Monitor", "HardDrive", "Router"],

            "Men Clothing": ["Tshirts", "Jeans", "Suits", "PoloShirts", "Jackets", "Sneakers", "Hoodies"],
            "Women Clothing": ["Dresses", "Blouses", "Skirts", "Cardigans", "Heels", "Flats", "Handbags", "Scarves"],
            "Sportswear": ["RunningShoes", "Shorts", "SportsBras", "Leggings", "TankTops", "Sweatbands", "Socks", "Jackets"],
            "Clothing Accessories": ["Watches", "Handbags", "Sunglasses", "Belts", "Hats", "Jewelry", "Wallets", "Ties"],
            "Footwear": ["Boots", "Sandals", "Slippers", "Loafers", "FlipFlops", "Clogs", "Wedges", "BalletFlats"],
            "Outerwear": ["Coats", "Raincoats", "Windbreakers", "Parkas", "Blazers", "TrenchCoats", "Vests", "Ponchos"],

            "Fruit": ["Apples", "Bananas", "Oranges", "Grapes", "Strawberries", "Blueberries", "Pineapples", "Mangoes"],
            "Vegetable": ["Carrots", "Spinach", "Broccoli", "Potatoes", "Tomatoes", "Cucumbers", "BellPeppers", "Onions"],
            "Snack": ["Chips", "Chocolate", "Nuts", "GranolaBars", "Popcorn", "Crackers", "Cookies", "Pretzels"],
            "Dairy": ["Milk", "Cheese", "Yogurt", "Butter", "Cream", "IceCream", "CottageCheese", "SourCream"],
            "Meat": ["Chicken", "Beef", "Pork", "Lamb", "Turkey", "Bacon", "Sausage", "Ham"],
            "Seafood": ["Salmon", "Tuna", "Shrimp", "Crab", "Lobster", "Scallops", "Mussels", "Clams"],
            "Beverages": ["Coffee", "Tea", "Juice", "Soda", "Water", "Beer", "Wine", "Smoothies"],

            "Outdoor Sport": ["Bicycle", "Soccer", "Tennis", "Basketball", "Football", "Golf"],
            "Water Sports Equipment": ["Surfboard", "Kayak", "Snorkel", "SwimFins", "LifeJacket", "Paddleboard", "ScubaGear", "WaterSkis"],
            "Team Sports Equipment": ["BaseballBat", "HockeyStick", "Volleyball", "LacrosseStick", "RugbyBall", "CricketBat", "SoftballGlove", "HockeyStick"],
        
        }
        
        self.choosen_category=''
        self.word_list = []
        self.secret_word = ''  #self.choose_secret_word()
        self.choose_secret_word()
        self.correct_guesses = set()
        self.incorrect_guesses = set()
        self.attempts_left = 7
        self.initialize_gui()

    def initialize_gui(self):
        button_bg = "#4a7a8c"
        button_fg = "white"
        button_font = ("Helvetica", 12, "bold")
        self.hangman_canvas = tk.Canvas(self.master, width=300, height=300, bg="white")
        self.hangman_canvas.pack(pady=10)
        self.category_display = tk.Label(self.master, text=f'Word is a name of {self.choosen_category}', font=("Helvetica", 20), bg='light blue')
        self.category_display.pack(pady=(5, 5))
        self.word_display = tk.Label(self.master, text="_ " * len(self.secret_word), font=("Helvetica", 30), bg='light blue')
        self.word_display.pack(pady=(10, 10))
        self.reset_button = tk.Button(self.master, text="Reset Game", command=self.reset_game, width=20, height=2, bg=button_bg, fg=button_fg, font=button_font)
        self.reset_button.pack(pady=(10, 0))
        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.pack(pady=20)
        self.setup_alphabet_buttons()

    def setup_alphabet_buttons(self):
        button_bg = "#4a7a8c"
        button_fg = "white"
        button_font = ("Helvetica", 12, "bold")

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        upper_row = alphabet[:13]
        lower_row = alphabet[13:]

        upper_frame = tk.Frame(self.buttons_frame)
        upper_frame.pack()
        lower_frame = tk.Frame(self.buttons_frame)
        lower_frame.pack()

        for letter in upper_row:
            button = tk.Button(upper_frame, text=letter, command=lambda l=letter: self.guess_letter(l), width=4, height=2, bg=button_bg, fg=button_fg, font=button_font)
            button.pack(side="left", padx=2, pady=2)

        for letter in lower_row:
            button = tk.Button(lower_frame, text=letter, command=lambda l=letter: self.guess_letter(l), width=4, height=2, bg=button_bg, fg=button_fg, font=button_font)
            button.pack(side="left", padx=2, pady=2)

    def choose_secret_word(self):
        self.choose_word_list()
        # return random.choice(self.word_list)
        self.secret_word = random.choice(self.word_list).upper()
        print(self.choosen_category,self.secret_word)
    
    def choose_word_list(self):
        self.choosen_category = random.choice(self.category_list)
        self.word_list = self.category_word_list[self.choosen_category]

    def update_hangman_canvas(self):
        self.hangman_canvas.delete("all")
        stages = [self.draw_head, self.draw_body, self.draw_left_arm, self.draw_right_arm,
                  self.draw_left_leg, self.draw_right_leg, self.draw_face]
        for i in range(len(self.incorrect_guesses)):
            if i < len(stages):
                stages[i]()

    def draw_head(self):
        self.hangman_canvas.create_oval(125, 50, 185, 110, outline="black")

    def draw_body(self):
        self.hangman_canvas.create_line(155, 110, 155, 170, fill="black")

    def draw_left_arm(self):
        self.hangman_canvas.create_line(155, 130, 125, 150, fill="black")

    def draw_right_arm(self):
        self.hangman_canvas.create_line(155, 130, 185, 150, fill="black")

    def draw_left_leg(self):
        self.hangman_canvas.create_line(155, 170, 125, 200, fill="black")

    def draw_right_leg(self):
        self.hangman_canvas.create_line(155, 170, 185, 200, fill="black")

    def draw_face(self):
        self.hangman_canvas.create_line(140, 70, 150, 80, fill="black")
        self.hangman_canvas.create_line(160, 70, 170, 80, fill="black")
        self.hangman_canvas.create_arc(140, 85, 170, 105, start=0, extent=-180, fill="black")

    def guess_letter(self, letter):
        if letter in self.secret_word and letter not in self.correct_guesses:
            self.correct_guesses.add(letter)
        elif letter not in self.incorrect_guesses:
            self.incorrect_guesses.add(letter)
            self.attempts_left -= 1
            self.update_hangman_canvas()

        self.update_word_display()
        self.check_game_over()

    def update_word_display(self):
        displayed_word = " ".join([letter if letter in self.correct_guesses else "_" for letter in self.secret_word])
        self.word_display.config(text=displayed_word)
        
    def update_category_display(self):
        self.category_display.config(text=f'Word is a name of {self.choosen_category}')

    def check_game_over(self):
        if set(self.secret_word).issubset(self.correct_guesses):
            self.display_game_over_message("Congratulations, you've won!")
        elif self.attempts_left == 0:
            self.display_game_over_message(f"Game over! The word was: {self.secret_word}")

    def display_game_over_message(self, message):
        stylish_font = ("Arial", 18, "italic")
        button_bg = "#4a7a8c"
        button_fg = "white"
        button_font = ("Helvetica", 12, "bold")

        self.reset_button.pack_forget()
        self.buttons_frame.pack_forget()

        self.game_over_label = tk.Label(self.master, text=message, font=stylish_font, fg="red", bg='light blue')
        self.game_over_label.pack(pady=(10, 20))

        if not hasattr(self, 'restart_button'):
            self.restart_button = tk.Button(self.master, text="Restart Game", command=self.reset_game, width=20, height=2, bg=button_bg, fg=button_fg, font=button_font)
        self.restart_button.pack(pady=(10, 20))

    def reset_game(self):
        # self.secret_word = self.choose_secret_word()
        self.choose_secret_word()
        self.correct_guesses = set()
        self.incorrect_guesses = set()
        self.attempts_left = 7

        self.hangman_canvas.delete("all")
        self.update_word_display()
        self.update_category_display()

        for frame in self.buttons_frame.winfo_children():
            for button in frame.winfo_children():
                button.configure(state=tk.NORMAL)

        self.reset_button.pack(pady=(10, 0))

        if hasattr(self, 'game_over_label') and self.game_over_label.winfo_exists():
            self.game_over_label.pack_forget()
        if hasattr(self, 'restart_button') and self.restart_button.winfo_exists():
            self.restart_button.pack_forget()

        self.buttons_frame.pack()

def main():
    root = tk.Tk()
    HangmanGame(root)
    root.mainloop()


main()
