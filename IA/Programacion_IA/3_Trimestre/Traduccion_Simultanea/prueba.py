import whisper
import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing speech...")
        text = recognizer.recognize_google(audio, language="en-US")
        print("Speech recognized:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return None

def translate(text):
    model = whisper.load_model("small")
    mel = whisper.log_mel_spectrogram(text).to(model.device)
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)
    return result.text

def conversation():
    print("Welcome to the simultaneous translation app. Speak something to start the conversation, type 'exit' to quit.")
    while True:
        user_input = recognize_speech()
        if user_input is None:
            continue
        elif user_input.lower() == 'exit':
            print("Goodbye!")
            break
        else:
            translated_text = translate(user_input)
            print("Translated:", translated_text)

if __name__ == "__main__":
    conversation()
