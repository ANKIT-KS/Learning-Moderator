sed -i '$ d' arduino_sensor_data.txt
sed 's/.$//' arduino_sensor_data.txt
a=`tail -1 arduino_sensor_data.txt`
#a=("${@}")
$a
curl --data "command_string=$a&position=1" https://api.thingspeak.com/talkbacks/your_GUI_side_talkback_id/commands.json?api_key=your_GUI_side_talkback_api_key

#updating the channel as well
curl --data "field1=$a" https://api.thingspeak.com/update?api_key=your_GUI_side_channel_api_key 
#truncate -s0 arduino_sensor_data.txt
#truncate -s0 arduino_input.txt
exit 0
