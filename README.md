translate_o_pi
==============

A universal language translator using Raspberry Pi.

An adapted version of Translator made by Dave Conroy at http://www.daveconroy.com/turn-raspberry-pi-translator-speech-recognition-playback-60-languages/

This version uses Nexiwave speech API instead of Google API for transcription. 

===============

clone:

git clone https://github.com/hashin/translate_o_pi

Edit trc.py by adding your directory in line number 37.

make trans.sh executable:

sudo chmod +x trans.sh

Run trans.sh:

./trans.sh

===============

You can also use the trn.py file to translate a piece of text by running:

python trn.py -o "Origin language code" -d "destination language code" -t "your text"

