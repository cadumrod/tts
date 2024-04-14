from gtts import gTTS
import pygame
import os


def text_to_speech(text,language):
    #Convert text to speech
    tts = gTTS(text=text,lang=language, slow=False)
    #Save audio to a file
    audio_file = "output.mp3"
    tts.save(audio_file)
    return audio_file


def play_audio(audio_file):
    # Initialize Pygame mixer
    pygame.mixer.init()
    # Load audio file
    pygame.mixer.music.load(audio_file)
    #Play the audio file
    pygame.mixer.music.play()
    # Wait until the audio is done playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def main():
    #Read the text from a file
    file_path = "text.txt"
    with open(file_path, "r") as file:
        text = file.read()
    #Convert text to speech
    audio_file = text_to_speech(text,language='pt')
    #Play the audio
    play_audio(audio_file)


if __name__ == "__main__":
    main()