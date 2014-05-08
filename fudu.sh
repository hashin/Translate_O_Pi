arecord -d 3 -r 48000 message.wav
aplay message.wav

sudo python kudu.py

value=`cat newf.txt`

echo "$value" 
#translate from English to Spanish and play over speakers
sudo python pydu.py -o en -d es -t "$value"
