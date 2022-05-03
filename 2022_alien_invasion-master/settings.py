
class Settings():
    """A class to store all settings for alien invasion"""

    def __init__(self):
        """ initialize game's settings"""

        # screen settings
        self.bg_color = (25, 0, 50)
        self.screen_width = 1200
        self.screen_height = 700

        # bullet settings
        self.bullet_speed = 3
        self.bullet_width = 5
        self.bullet_height = 5
        self.bullet_color = (0, 255, 0)
        self.bullet_limit = 2

        # player settings
        self.lives = 3
        self.score = 0

        # play game
        self.game_active = False