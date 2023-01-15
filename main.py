import pgzrun
import random
import time


# These values need to be outside of any function or class to be seen by pgzero
TITLE = "Space Pig"
WIDTH = 800
HEIGHT = 800


class Game:
    def __init__(self):
        self.init_game()
    
    def init_game(self):
        self.pig = Actor("pig_round")
        self.pig.pos = WIDTH / 2, HEIGHT - self.pig.height / 2 # Image origin is at the center of the image
        
        self.blocks = []
        self.block_interval = 1.5
        self.score = 0
        self.game_over = False

        # Call the add_block method after every block_interval
        clock.schedule_interval(self.add_block, self.block_interval)

    def add_block(self):
        block = Actor("block")
        # New block falls from the top at a random horizontal position
        block.pos = random.randrange(block.width / 2, WIDTH - (block.width / 2)), 0 - (block.height / 2)
        self.blocks.append(block)

    def reset_game(self):
        # Stop the game for 2.0 seconds to show a game over message then reset the game
        self.game_over = True
        self.pig.image = "pig_square"
        clock.unschedule(self.add_block)
        clock.schedule_unique(self.init_game, 2.0)


game = Game()


# Used by pgzero
def draw():
    screen.clear()
    game.pig.draw()
    for block in game.blocks:
        block.draw()
    screen.draw.text(f"Score: {game.score}", center=(WIDTH / 2, 40), fontname="bruce_forever", fontsize=40, color=(193, 127, 64), owidth=1, ocolor=(240, 240, 240))
    if game.game_over:
        screen.draw.text("Game over!", center=(WIDTH / 2, HEIGHT / 2), fontname="bruce_forever", fontsize=50, color=(193, 127, 64), owidth=1, ocolor=(240, 240, 240))


# Used by pgzero
def update():
    if game.game_over == False:
        # Pig movement
        if keyboard.left:
            game.pig.x -=4
        elif keyboard.right:
            game.pig.x += 4

        # Stop pig from going off screen
        if (game.pig.x + game.pig.width / 2) > WIDTH:
            game.pig.x = WIDTH - (game.pig.width / 2)
        if (game.pig.x - game.pig.width / 2) < 0:
            game.pig.x = game.pig.width / 2

        # Update block position and block array
        for block in game.blocks:
            block.y += 4
            if (block.y > HEIGHT + (block.height / 2)):
                game.blocks.remove(block)
                game.score += 1

        # collidelist stores a list of collisions, returns the index of the first collision and returns -1 if there are no collisions
        collision = game.pig.collidelist(game.blocks)
        if collision >= 0:
            game.reset_game()



pgzrun.go()

