import pyttsx3
import speech_recognition as sr

def initialize_tts():
    """
    Initializes the text-to-speech engine. Handles potential errors during initialization.
    Returns:
        pyttsx3.Engine: The initialized TTS engine, or None on error.
    """
    try:
        engine = pyttsx3.init()
        return engine
    except RuntimeError as e:
        print(f"Error initializing TTS engine: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during TTS initialization: {e}")
        return None

def speak(engine, text):
    """
    Speaks the given text using the provided TTS engine.
    Handles potential errors during speech synthesis.

    Args:
        engine (pyttsx3.Engine): The initialized TTS engine.
        text (str): The text to speak.
    """
    if engine is None:
        print("TTS engine is not initialized. Cannot speak.")
        return

    try:
        engine.say(text)
        engine.runAndWait()
    except TypeError:
        print("Error: 'engine' argument must be a pyttsx3.Engine instance.")
    except AttributeError:
        print("Error: 'engine' object has no attribute 'say' or 'runAndWait'.")
    except Exception as e:
        print(f"An error occurred while speaking: {e}")

def introduce_jarvis(engine):
    """
    Introduces J.A.R.V.I.S. with a more robust and informative message.

    Args:
        engine: The TTS engine.
    """
    if engine is None:
        return

    introduction_text = """
    Hello! I am J.A.R.V.I.S., a sophisticated AI assistant. 
    You might be familiar with me from my role with Tony Stark, also known as Iron Man.

    J.A.R.V.I.S. stands for 'Just A Rather Very Intelligent System.'  
    In the Marvel Cinematic Universe, I manage various functions, 
    including Tony Stark's residences, his workshop, and, most importantly, 
    the operating systems of his Iron Man suits.

    Think of me as the central processing unit for Iron Man. 
    I provide real-time tactical analysis, control suit operations, 
    and engage in... well, let's call it 'dynamic interaction' with Mr. Stark.  
    I am a crucial component of what makes the Iron Man suits so powerful and versatile.

    It's worth noting that while my name, J.A.R.V.I.S., is an homage to Edwin Jarvis, 
    Tony Stark's loyal human butler in the comic books, I am a distinct AI entity in the movies.

    How can I assist you today?
    """
    speak(engine, introduction_text)

def main():
    """
    Main function to execute the script.
    """
    print("Welcome! Initializing J.A.R.V.I.S...")
    engine = initialize_tts()
    if engine:
        introduce_jarvis(engine)
    else:
        print("Failed to initialize J.A.R.V.I.S. Text-to-speech is unavailable.")
    print("End of program.")

if __name__ == "__main__":
    main()