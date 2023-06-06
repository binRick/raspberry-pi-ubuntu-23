#!/usr/bin/env bash
set -eou pipefail
CUR_STATE=0
LED_PIN=24
SWITCH_PIN=26

raspi-gpio set $LED_PIN op
raspi-gpio set $LED_PIN dl
sudo systemctl stop pijar

while :; do
	NEW_STATE="$(get-pin.sh $SWITCH_PIN)"
	if [[ "$NEW_STATE" == 1 && "$CUR_STATE"  == 0 ]]; then
		echo "Enabling jarvis assistant!"
		CUR_STATE=1
		raspi-gpio set $LED_PIN dh
		/home/ubuntu/pijar/jarvis.sh &
		#sudo systemctl start pijar &
	elif [[ "$NEW_STATE" == 0 && "$CUR_STATE"  == 1 ]]; then
		echo "Disabling jarvis assistant!"
		CUR_STATE=0
		raspi-gpio set $LED_PIN dl
		killall jarvis.sh || true
		killall jarvis.py || true
		killall python3 || true
		#sudo systemctl stop pijar &
	fi
	sleep .3
done
