arecord -d 3 -r 48000 message.wav
aplay message.wav

sudo python trc.py

value=`cat newf.txt`

echo "$value" 
#translate from English to Spanish and play over speakers
sudo python trn.py -o en -d es -t "$value"

rm message.wav


./trans.sh
