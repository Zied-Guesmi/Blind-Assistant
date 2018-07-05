from io import BytesIO
import os
import sys
from time import sleep

import pytesseract
from gtts import gTTS
from PIL import Image
from picamera import PiCamera

# TODO: add self everywhere

class OCR(object):
    """docstring for OCR."""
    def __init__(self, arg):
        super(OCR, self).__init__()
        self.arg = arg

    def image2text(arg):
        pass

    def extract_text(image_file):
        try:
            image = Image.open(image_file)
            text = pytesseract.image_to_string(image, lang="eng")
            return text
        except Exception as e:
            print("==> Error: can't extract text from image")
            print(str(e))


class TTS(object):
    """docstring for TTS."""
    def __init__(self, arg):
        super(TTS, self).__init__()
        self.arg = arg
    def text_to_speech(text):
        try:
            tts = gTTS(text=text, lang='en')
            # tts.save("speech.mp3")
            if not(os.path.exists("/home/pi/mp3_files")) :
                os.mkdir("/home/pi/mp3_files",0o755)
            tts.save("/home/pi/mp3_files/speech.mp3")
        except Exception as e:
            print("==> can't convert text to speech")
            print(str(e))


class ImageToSpeech(object):
    """docstring for Main."""

    def __init__(self, arg):
        super(Main, self).__init__()
        self.arg = arg

    def capture_image(self):
        try:
            camera = PiCamera()
            print("==> About to take an image...")
            #camera = PiCamera()
            # camera.resolution = (1920, 1080)
            # camera.framerate = 15
            # camera.start_preview()
            # sleep(2)
            camera.capture("/home/pi/images/image.jpg")
            # camera.stop_preview()
        except Exception as e:
            print("==> Erro: can't capture the image")
            print(str(e))

    def display_text(text):
        try:
            print("==> Text:")
            print(text)
        except Exception as e:
            print("==> Error: can't print text")
            print(str(e))

    def read_mp3_file():
        try:
            os.system("mpg123 /home/pi/mp3_files/speech.mp3")
        except Exception as e:
            print("==> can't read mp3 file")
            print(str(e))

    def remove_files():
        os.system("rm /home/pi/mp3_files/speech.mp3")
        os.system("mv /home/pi/images/image.jpg .")

    def main(arg):
        image = capture_image(camera)
        print("==> Image taken. Extracting text...")
        text = extract_text("/home/pi/images/image.jpg")
        display_text(text)
        text_to_speech(text)
        read_mp3_file()
        remove_files()


if __name__ == '__main__':
    ImageToSpeech().main()