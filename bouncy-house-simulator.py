import tkinter as tk
import random
import time

# Constants for the bouncy house dimensions
HOUSE_WIDTH = 600
HOUSE_HEIGHT = 400

# Constants for ball properties
BALL_RADIUS = 20
BALL_COLORS = ["red", "green", "blue", "yellow", "purple", "orange"]
BALL_SPEED = 5

class Ball:
    def __init__(self, canvas, x, y, color):
        self.canvas = canvas
        self.id = canvas.create_oval(x - BALL_RADIUS, y - BALL_RADIUS,
                                     x + BALL_RADIUS, y + BALL_RADIUS,
                                     fill=color)
        self.vx = random.randint(-BALL_SPEED, BALL_SPEED)
        self.vy = random.randint(-BALL_SPEED, BALL_SPEED)
    
    def move(self):
        self.canvas.move(self.id, self.vx, self.vy)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0 or pos[2] >= HOUSE_WIDTH:
            self.vx = -self.vx
        if pos[1] <= 0 or pos[3] >= HOUSE_HEIGHT:
            self.vy = -self.vy

def start_simulation(canvas, balls):
    # Create initial balls
    for _ in range(5):
        x = random.randint(BALL_RADIUS, HOUSE_WIDTH - BALL_RADIUS)
        y = random.randint(BALL_RADIUS, HOUSE_HEIGHT - BALL_RADIUS)
        color = random.choice(BALL_COLORS)
        ball = Ball(canvas, x, y, color)
        balls.append(ball)
    
    # Start moving balls
    while True:
        for ball in balls:
            ball.move()
        canvas.update()
        time.sleep(0.03)  # Adjust speed of simulation

def create_bouncy_house():
    # Create main window
    root = tk.Tk()
    root.title("Virtual Bouncy House Simulator")

    # Create canvas for bouncy house
    canvas = tk.Canvas(root, width=HOUSE_WIDTH, height=HOUSE_HEIGHT, bg="lightblue")
    canvas.pack()

    # Buttons to control simulation
    start_button = tk.Button(root, text="Start Simulation",
                             command=lambda: start_simulation(canvas, []))
    start_button.pack(pady=10)

    stop_button = tk.Button(root, text="Stop Simulation", command=root.quit)
    stop_button.pack(pady=10)

    # Run the GUI loop
    root.mainloop()

# Call function to create the bouncy house simulator
create_bouncy_house()