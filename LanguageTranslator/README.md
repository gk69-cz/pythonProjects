
Speech Translator Application

This is a simple Python application that allows you to translate spoken text from one language to another using speech recognition and translation APIs.

Features
Speech recognition: The application listens to your voice input and converts it into text using the Google Speech Recognition API.
Language translation: It translates the recognized text from one language to another using the Google Translate API.
Text-to-speech: It converts the translated text into speech using the gTTS (Google Text-to-Speech) library.

Installation

Clone the repository:

git clone https://github.com/your_username/speech-translator.git
Install dependencies:

Copy code
pip install -r requirements.txt
Usage
Make sure you have a microphone connected to your system.

Run the speech_translator.py file:

Speak into the microphone when prompted. The application will attempt to recognize your speech and translate it into the desired language.

The translated text will be converted into speech and saved as voice.mp3 in the current directory.

Configuration

You can specify the source language (from_language) and the target language (to_language) in the speech_translator.py file.
By default, the source language is set to English and the target language is set to French. You can change these values according to your preferences.

Dependencies
playsound: For playing audio files.
googletrans: For translating text using Google Translate.
gtts: For converting text to speech using Google Text-to-Speech.
speech_recognition: For recognizing speech input.
google_trans_new: For translation using Google Translate API.

License
This project is licensed under the MIT License - see the LICENSE file for details.
