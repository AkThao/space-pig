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
        self.pig = Actor("pig_round_right")
        self.pig.pos = WIDTH / 2, HEIGHT - self.pig.height / 2 # Image origin is at the center of the image
        self.pig_speed = 5
        self.pig_direction = 1  # 1 for right, 0 for left
        
        self.blocks = []
        self.block_interval = 0.75
        self.block_falling_speed = 4

        self.score = 0
        self.game_over = False

        # Call the add_block method after every block_interval
        clock.schedule_unique(self.add_block, self.block_interval)

        self.create_stars()

        music.play("space_music")

    def add_block(self):
        block = Actor("block")
        # New block falls from the top at a random horizontal position
        block.pos = random.randrange(block.width / 2, WIDTH - (block.width / 2)), 0 - (block.height / 2)
        self.blocks.append(block)
        self.block_interval = random.random() * 1.5
        clock.schedule_unique(self.add_block, self.block_interval)

    def create_stars(self):
        self.stars = []
        
        for i in range(100):
            rand_x_pos = random.randint(0, WIDTH)
            rand_y_pos = random.randint(0, HEIGHT)
            rand_size = random.random() * 4
            self.stars.append((rand_x_pos, rand_y_pos, rand_size))

    def reset_game(self):
        # Stop the game for 2.0 seconds to show a game over message then reset the game
        self.game_over = True
        sounds.oink.play()
        music.stop()
        self.pig.image = "pig_square_right" if self.pig_direction == 1 else "pig_square_left"
        clock.unschedule(self.add_block)
        clock.schedule_unique(self.init_game, 2.0)


game = Game()


# Used by pgzero
def draw():
    screen.clear()

    for star in game.stars:
        screen.draw.filled_circle((star[0], star[1]), star[2], (255, 255, 255))

    for block in game.blocks:
        block.draw()

    game.pig.draw()

    screen.draw.text(f"Score: {game.score}", center=(WIDTH / 2, 40), fontname="bruce_forever", fontsize=40, color=(193, 127, 64), owidth=1, ocolor=(240, 240, 240))
    if game.game_over:
        screen.draw.text("Game over!", center=(WIDTH / 2, HEIGHT / 2), fontname="bruce_forever", fontsize=50, color=(193, 127, 64), owidth=1, ocolor=(240, 240, 240))



# Used by pgzero
def update():
    if game.game_over == False:
        # Pig movement
        if keyboard.left:
            game.pig.x -= game.pig_speed
            game.pig_direction = 0
            game.pig.image = "pig_round_left"
        elif keyboard.right:
            game.pig.x += game.pig_speed
            game.pig_direction = 1
            game.pig.image = "pig_round_right"

        # Stop pig from going off screen
        if (game.pig.x + game.pig.width / 2) > WIDTH:
            game.pig.x = WIDTH - (game.pig.width / 2)
        if (game.pig.x - game.pig.width / 2) < 0:
            game.pig.x = game.pig.width / 2

        # Update block position and block array
        for block in game.blocks:
            block.y += game.block_falling_speed
            if (block.y > HEIGHT + (block.height / 2)):
                game.blocks.remove(block)
                game.score += 1
                if game.score % 10 == 0:
                    sounds.get_point.play()

        # collidelist stores a list of collisions, returns the index of the first collision and returns -1 if there are no collisions
        collision = game.pig.collidelist(game.blocks)
        if collision >= 0:
            game.reset_game()



pgzrun.go()

