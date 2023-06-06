#!/usr/bin/env bash
raspi-gpio get $1|grep level=|cut -d ' ' -f 3|cut -d= -f2
