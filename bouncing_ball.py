{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "ecc988f2-0bda-4477-9d79-17ddf9378dd5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pygame in /opt/anaconda3/lib/python3.12/site-packages (2.6.1)\n"
     ]
    }
   ],
   "source": [
    "!pip install pygame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "ad649fcd-4e98-42d6-b328-39adce70b38e",
   "metadata": {},
   "outputs": [
    {
     "ename": "SystemExit",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[0;31mSystemExit\u001b[0m\n"
     ]
    }
   ],
   "source": [
    "import pygame\n",
    "import sys\n",
    "\n",
    "# Initialize Pygame\n",
    "pygame.init()\n",
    "\n",
    "# Screen dimensions\n",
    "WIDTH, HEIGHT = 600, 400\n",
    "\n",
    "# Colors\n",
    "BLACK = (0, 0, 0)\n",
    "WHITE = (255, 255, 255)\n",
    "RED = (255, 0, 0)\n",
    "\n",
    "# Ball properties\n",
    "ball_radius = 20\n",
    "ball_x = WIDTH // 2\n",
    "ball_y = ball_radius\n",
    "ball_speed_y = 0\n",
    "gravity = 0.5\n",
    "elasticity = 0.8\n",
    "horizontal_speed = 5\n",
    "vertical_speed = 5\n",
    "\n",
    "# Set up the display\n",
    "screen = pygame.display.set_mode((WIDTH, HEIGHT))\n",
    "pygame.display.set_caption(\"Fully Interactive Bouncing Ball\")\n",
    "\n",
    "# Clock for controlling the frame rate\n",
    "clock = pygame.time.Clock()\n",
    "\n",
    "# Main loop\n",
    "running = True\n",
    "while running:\n",
    "    for event in pygame.event.get():\n",
    "        if event.type == pygame.QUIT:\n",
    "            running = False\n",
    "\n",
    "    # Get key states\n",
    "    keys = pygame.key.get_pressed()\n",
    "\n",
    "    # Horizontal movement\n",
    "    if keys[pygame.K_LEFT]:\n",
    "        ball_x -= horizontal_speed\n",
    "    if keys[pygame.K_RIGHT]:\n",
    "        ball_x += horizontal_speed\n",
    "\n",
    "    # Vertical movement\n",
    "    if keys[pygame.K_UP]:\n",
    "        ball_y -= vertical_speed\n",
    "    if keys[pygame.K_DOWN]:\n",
    "        ball_y += vertical_speed\n",
    "\n",
    "    # Prevent the ball from going out of bounds horizontally\n",
    "    if ball_x - ball_radius < 0:\n",
    "        ball_x = ball_radius\n",
    "    if ball_x + ball_radius > WIDTH:\n",
    "        ball_x = WIDTH - ball_radius\n",
    "\n",
    "    # Prevent the ball from going out of bounds vertically\n",
    "    if ball_y - ball_radius < 0:\n",
    "        ball_y = ball_radius\n",
    "\n",
    "    # Ball physics\n",
    "    ball_speed_y += gravity\n",
    "    ball_y += ball_speed_y\n",
    "\n",
    "    # Bounce when hitting the ground\n",
    "    if ball_y + ball_radius > HEIGHT:\n",
    "        ball_y = HEIGHT - ball_radius\n",
    "        ball_speed_y = -ball_speed_y * elasticity\n",
    "\n",
    "    # Clear the screen\n",
    "    screen.fill(BLACK)\n",
    "\n",
    "    # Draw the ball\n",
    "    pygame.draw.circle(screen, RED, (ball_x, int(ball_y)), ball_radius)\n",
    "\n",
    "    # Update the display\n",
    "    pygame.display.flip()\n",
    "\n",
    "    # Cap the frame rate\n",
    "    clock.tick(60)\n",
    "\n",
    "# Quit Pygame\n",
    "pygame.quit()\n",
    "sys.exit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6fac691a-3893-4733-ab0d-8d08789eaa48",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
