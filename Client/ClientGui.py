import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from ClientGame import ClientGame
from PIL import Image, ImageTk

main_frame = None

class ClientGui:
    def __init__(self, shared_data):
        self.shared_data = shared_data
        self.root = tk.Tk()
        self.root.title("Меню игры")
        self.root.attributes('-fullscreen', True)  # Полноэкранный режим
        self.players = tk.IntVar()
        self.board_size = tk.IntVar()
        self.computer_mode = tk.BooleanVar()
        self.computer_difficulty = tk.StringVar()
        self.create_main_menu()
        self.game = None

        self.canvas = tk.Canvas(self.root, width=1000, height=800)
        self.square_size = 90
        self.diffy = 80
        self.diffx = 140
        self.images = None

        self.load_images()

    def load_images(self):
        self.images = {}
        for piece in ["pawn", "rook", "horse", "elephant", "queen", "king"]:
            for color in ["white", "black"]:
                filename = rf"output\{color}_{piece}.png"
                image = Image.open(filename)
                image = image.resize((int(image.width), int(image.height)), Image.BILINEAR)
                photo = ImageTk.PhotoImage(image)
                self.images[f"{color}_{piece}"] = photo

    def get_non_empty_string(self, prompt, parent):
        while True:
            player_name = simpledialog.askstring("Введите никнейм", prompt, parent=parent)
            if player_name is not None and player_name.strip() != "":
                return player_name

    def start_game(self, mode, computer_difficulty, count_players, map_grid):
        global main_frame

        # Очистить главное окно, уничтожив все дочерние элементы
        for widget in self.root.winfo_children():
            widget.destroy()

        # Здесь вы можете создать новый холст и другие виджеты, как вам нужно
        self.canvas = tk.Canvas(self.root, width=1000, height=1000)
        self.canvas.pack()

        # Создайте экземпляр игры и что-либо еще, что вам нужно для вашего приложения
        self.game = ClientGame(self.root, self.images, self.canvas, self.square_size, self.diffy, self.diffx,
                               self.shared_data)

    def create_main_menu(self):
        global main_frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0)

        # Устанавливаем растягивание рядов и колонок на главном окне root
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Создаем фрейм внутри главного фрейма для центрирования элементов
        center_frame = ttk.Frame(main_frame)
        center_frame.grid(row=0, column=0, padx=10, pady=10)

        # Создаем стиль для кнопок
        button_style = ttk.Style()
        # Увеличиваем размер шрифта для кнопок
        button_style.configure("Custom.TButton", font=("Helvetica", 14))
        # Увеличиваем внутренний и внешний паддинг для кнопок
        button_style.configure("Custom.TButton", padding=10)

        # Создаем стиль для надписи
        label_style = ttk.Style()
        # Увеличиваем размер шрифта для надписи
        label_style.configure("Custom.TLabel", font=("Helvetica", 16))

        # Создаем новый стиль для OptionMenu, чтобы сохранить значок списка
        players_style = ttk.Style()
        players_style.configure("Custom.TMenubutton", font=("Helvetica", 12), background="lightblue", foreground="black")

        ttk.Label(center_frame, text="Выберите режим игры", style="Custom.TLabel").grid(row=0, column=0, columnspan=2, pady=(0, 10))
        ttk.Button(center_frame, text="Играть с игроками",  command=lambda:self.start_game("P", self.computer_difficulty.get(), 1, self.board_size.get()), width=20, style="Custom.TButton").grid(row=1, column=0, padx=5, pady=10)
        ttk.Button(center_frame, text="Играть с компьютером",  command=lambda:self.create_computer_options(), width=22, style="Custom.TButton").grid(row=1, column=1, padx=5, pady=10)
        ttk.Button(self.root, text="Выход", command=self.on_exit_button_click, style="Custom.TButton").grid(row=0, column=1, sticky=tk.NE)

    def create_computer_options(self):
        global main_frame
        main_frame.grid_forget()

        computer_options_frame = ttk.Frame(self.root, padding="20")
        computer_options_frame.grid(row=0, column=0)

        # Устанавливаем растягивание рядов и колонок на основном окне root
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Создаем фрейм внутри computer_options_frame для центрирования элементов
        center_frame = ttk.Frame(computer_options_frame)
        center_frame.grid(row=0, column=0, padx=10, pady=10)

        computer_difficulty_label = ttk.Label(center_frame, text="Сложность компьютера:", style="Custom.TLabel")
        computer_difficulty_label.grid(row=0, column=0, pady=(0, 10), sticky="W")
        computer_difficulty_values = ["Легкий", "Сложный"]
        self.computer_difficulty.set(computer_difficulty_values[0])
        board_size_menu = ttk.OptionMenu(center_frame, self.computer_difficulty, computer_difficulty_values[0], *computer_difficulty_values,
                                         style="Custom.TMenubutton")
        board_size_menu.grid(row=0, column=1, pady=(0, 10))

        computer_difficulty_menu = ttk.OptionMenu(center_frame, self.computer_difficulty, computer_difficulty_values[0], *computer_difficulty_values,
                                                  style="Custom.TMenubutton")
        computer_difficulty_menu.grid(row=0, column=1, pady=(0, 10), sticky="W")

        ttk.Button(center_frame, text="Начать игру", command=lambda:self.start_game("PC", self.computer_difficulty.get(), 1, self.board_size.get()), width=20, style="Custom.TButton").grid(row=2, column=0, columnspan=2, pady=(10, 0))
        ttk.Button(center_frame, text="Назад", command= lambda:self.return_to_main_menu(), style="Custom.TButton").grid(row=3, column=0, columnspan=2, pady=(10, 0))

    def on_exit_button_click(self):
        if messagebox.askokcancel("Выход", "Вы уверены, что хотите выйти?"):
            self.root.quit()

    def return_to_main_menu(self):
        # Удаляем все дочерние элементы у главного окна
        for child in self.root.winfo_children():
            child.destroy()
        # Заново создаем главное меню
        self.create_main_menu()