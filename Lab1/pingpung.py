import tkinter as tk
import random
import time

# Inicjalizacja okna
root = tk.Tk()
root.title("Ping-Pong Game")
root.geometry("400x400")

# Ustawienia paletki
paddle_width = 80
paddle_height = 10
paddle_x = (400 - paddle_width) // 2
paddle_y = 380
paddle_speed = 10

# Ustawienia piłki
ball_radius = 10
ball_x = 200
ball_y = 100
ball_x_speed = 5
ball_y_speed = 5

# Utworzenie paletki
paddle = tk.Canvas(root, width=paddle_width, height=paddle_height, bg="blue")
paddle.create_rectangle(0, 0, paddle_width, paddle_height, fill="blue")
paddle.pack()
paddle.place(x=paddle_x, y=paddle_y)

# Utworzenie piłki
ball = tk.Canvas(root, width=ball_radius * 2, height=ball_radius * 2, bg="red")
ball.create_oval(0, 0, ball_radius * 2, ball_radius * 2, fill="red")
ball.pack()
ball.place(x=ball_x, y=ball_y)

# Zmienna do śledzenia stanu gry
game_running = False

# Zmienna do przechowywania etykiety "Game Over"
game_over_label = None

# Funkcja do ruchu paletki w lewo
def move_left(event):
    global paddle_x
    if paddle_x > 0:
        paddle_x -= paddle_speed
        paddle.place(x=paddle_x, y=paddle_y)

# Funkcja do ruchu paletki w prawo
def move_right(event):
    global paddle_x
    if paddle_x < 400 - paddle_width:
        paddle_x += paddle_speed
        paddle.place(x=paddle_x, y=paddle_y)

# Obsługa klawiszy strzałek
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

# Funkcja do ruchu piłki
def move_ball():
    global ball_x, ball_y, ball_x_speed, ball_y_speed

    # Aktualizacja pozycji piłki
    ball_x += ball_x_speed
    ball_y += ball_y_speed

    # Odbicie od lewej i prawej krawędzi
    if ball_x < 0 or ball_x > 400 - ball_radius * 2:
        ball_x_speed *= -1

    # Odbicie od paletki
    if (
        ball_y + ball_radius * 2 > paddle_y
        and ball_x + ball_radius * 2 > paddle_x
        and ball_x < paddle_x + paddle_width
    ):
        ball_y_speed *= -1

    # Odbicie od górnej krawędzi
    if ball_y < 0:
        ball_y_speed *= -1

    # Koniec gry
    if ball_y > 400:
        game_over()

    # Aktualizacja pozycji piłki na ekranie
    ball.place(x=ball_x, y=ball_y)

    # Wywołaj funkcję ponownie po pewnym czasie
    if game_running:
        root.after(30, move_ball)

# Funkcja do rozpoczęcia gry
def start_game():
    global game_running, game_over_label
    if not game_running:
        game_running = True
        start_button.place_forget()
        # Przywrócenie paletki i piłki do początkowych pozycji
        global paddle_x, ball_x, ball_y, ball_x_speed, ball_y_speed
        paddle_x = (400 - paddle_width) // 2
        ball_x = 200
        ball_y = 100
        ball_x_speed = 5
        ball_y_speed = 5
        paddle.place(x=paddle_x, y=paddle_y)
        ball.place(x=ball_x, y=ball_y)
        if game_over_label:
            game_over_label.place_forget()  # Usunięcie napisu "Game Over"
        move_ball()

# Funkcja do zakończenia gry
def game_over():
    global game_running, game_over_label
    game_running = False
    ball.place(x=ball_x, y=ball_y)  # Przywrócenie piłki na dolnym ekranie
    paddle.place_forget()
    game_over_label = tk.Label(root, text="Game Over!", font=("Helvetica", 24))
    game_over_label.pack()
    game_over_label.place(x=120, y=180)
    start_button.place(x=190, y=130)

# Przycisk Start
start_button = tk.Button(root, text="Start", command=start_game)
start_button.pack()
start_button.place(x=190, y=130)

# Rozpoczęcie głównej pętli programu
root.mainloop()
