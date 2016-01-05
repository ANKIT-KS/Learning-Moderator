truncate -s0 arduino_input.txt
curl -i -H "Accept: application/json" -H "Content-Type: application/json" GET https://api.thingspeak.com/talkbacks/4580/commands/execute.json?api_key=PJ3BES0HDVVULGSQ | json command_string > new_arduino_input.txt

sed '1,18d' new_arduino_input.txt >> arduino_input.txt
#sed -i '$ d' arduino_input.txt
#sed 's/.$//' arduino_input.txt
#tail -n 1 arduino_input.txt
exit 0
