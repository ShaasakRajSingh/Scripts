from gtts import gTTS
import os
import playsound

def text_to_speech(text, lang='en'):
    """
    Converts text to speech and plays the audio.

    :param text: Text to be converted to speech
    :param lang: Language in which the text should be spoken (default is 'en' for English)
    """
    try:
        # Create gTTS object
        tts = gTTS(text=text, lang=lang)

        # Save the converted audio to a file
        audio_file = "output.mp3"
        tts.save(audio_file)

        # Play the converted audio file
        playsound.playsound(audio_file)

        # Optionally, remove the audio file after playing
        os.remove(audio_file)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    text = "Hello, this is a text to speech conversion using gTTS in Python."
    text_to_speech(text)
