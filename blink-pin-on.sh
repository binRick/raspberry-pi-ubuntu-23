#!/usr/bin/env bash
set -eou pipefail
LED_PIN=24

raspi-gpio set $LED_PIN op
raspi-gpio set $LED_PIN dl
sleep .1
raspi-gpio set $LED_PIN dh
sleep .1

raspi-gpio set $LED_PIN dl
sleep .1
raspi-gpio set $LED_PIN dh
