# ML-Powered Podcast Translator
Translate Podcasts using AI and Google Cloud Platform APIs

In this directory, you'll find code that takes a podcast (or any audio file) and:

1. Transcribes it to text.
2. Translates the transcription.
3. Generates an audio file that speaks out the translated content.

# Setup

1. Create a new Google Cloud Project.

2. Enable these Google Cloud APIs:

- Speech-to-Text
- Text-to-Speech
- Translation

3. Create a Cloud Bucket in your project

4. Create a new service account with the Translation Admin permission and download the credentials file.

# How to Use

1. Clone the repo
2. Set the environmental variable GOOGLE_APPLICATION_CREDENTIALS to point to your credentials file you've downloaded during the setup.
3. Upload your target audio file on the Cloud Bucket
4. Change source files details and source/target language parameters accordingly to your needs.
5. Enjoy!

# Useful Resources

- Speech to Text API supported languages - https://cloud.google.com/speech-to-text/docs/languages
- Translate API supported languages - https://cloud.google.com/translate/docs/languages
- Text to Speech API supported languages and available voices - https://cloud.google.com/text-to-speech/docs/voices
