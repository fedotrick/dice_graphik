import random
import time
import tkinter as tk

def roll_dice(label):
    numbers = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    for _ in range(10):
        dice_num = random.choice(numbers)
        label.config(text=dice_num)
        label.update()
        time.sleep(0.1)

def dice():
    player = random.randint(1, 6)
    ai = random.randint(1, 6)
    
    root = tk.Tk()
    root.title("Dice Game")

    player_label = tk.Label(root, text="Вы: ", font=("Helvetica", 16))
    player_label.pack()

    player_dice_label = tk.Label(root, text="", font=("Helvetica", 100))
    player_dice_label.pack()

    ai_label = tk.Label(root, text="Компьютер: ", font=("Helvetica", 16))
    ai_label.pack()

    ai_dice_label = tk.Label(root, text="", font=("Helvetica", 100))
    ai_dice_label.pack()

    result_label = tk.Label(root, text="", font=("Helvetica", 16))
    result_label.pack()

    roll_dice(player_dice_label)
    player_dice_label.config(text=str(player))

    roll_dice(ai_dice_label)
    ai_dice_label.config(text=str(ai))

    if player > ai:
        result_label.config(text="Вы одержали победу!")
    elif player == ai:
        result_label.config(text="Ничья!")
    else:
        result_label.config(text="Вы проиграли...")

    def exit_game():
        root.destroy()

    def play_again():
        root.destroy()
        dice()

    exit_button = tk.Button(root, text="Выход", command=exit_game)
    exit_button.pack()

    play_again_button = tk.Button(root, text="Сыграть еще раз", command=play_again)
    play_again_button.pack()

    root.mainloop()

dice()