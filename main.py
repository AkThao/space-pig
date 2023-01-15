import pgzrun
import random
import time


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

        clock.schedule_interval(self.add_block, self.block_interval)

    def add_block(self):
        block = Actor("block")
        block.pos = random.randrange(block.width / 2, WIDTH - (block.width / 2)), 0 - (block.height / 2)
        self.blocks.append(block)

    def reset_game(self):
        self.game_over = True
        self.pig.image = "pig_square"
        clock.unschedule(self.add_block)
        clock.schedule_unique(self.init_game, 2.0)


game = Game()


def draw():
    screen.clear()
    game.pig.draw()
    for block in game.blocks:
        block.draw()
    screen.draw.text(f"Score: {game.score}", center=(WIDTH / 2, 40), fontname="bruce_forever", fontsize=40, color=(193, 127, 64), owidth=1, ocolor=(240, 240, 240))
    if game.game_over:
        screen.draw.text("Game over!", center=(WIDTH / 2, HEIGHT / 2), fontname="bruce_forever", fontsize=50, color=(193, 127, 64), owidth=1, ocolor=(240, 240, 240))


def update():
    if game.game_over == False:
        # Basic pig movement
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

        collision = game.pig.collidelist(game.blocks)
        if collision >= 0:
            game.reset_game()



pgzrun.go()

