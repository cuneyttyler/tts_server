# Installation

You need python 3.10 to run this app. Please download and install it via official python web site.
You also need Nvidia Geforce Graphics card in order to run this with app with GPU support (which is pretty faster than cpu)

Run install.bat file.

# Running
Fill in TTS_MODEL field with one of these:

 1: tts_models/multilingual/multi-dataset/xtts_v2 (Best quality, you need a good GPU)
 2: tts_models/multilingual/multi-dataset/xtts_v1.1 (Faster than xtts_v2, but compromises on quality)
 3: tts_models/multilingual/multi-dataset/your_tts (This runs very fast even with old GPUs, but quality isn't that good)

Run app.bat file.

You can check if server is running by going to http://localhost:5000 in your browser. If it's running it will pring "Server works!". You can also see it on the app window which opens when you click app.bat file.