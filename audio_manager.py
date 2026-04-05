import pygame

class AudioManager:
    def __init__(self):
        pygame.mixer.init()  # Initialize the audio mixer

    def load_sound(self, sound_file):
        return pygame.mixer.Sound(sound_file)

    def play_sound(self, sound):
        sound.play()
