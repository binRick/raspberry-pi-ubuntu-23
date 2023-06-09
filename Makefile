pi-joystick-json:
	gcc joystick-json.c -o joystick-json \
		-L /usr/lib/arm-linux-gnueabihf \
		-I /usr/include/libusb-1.0 \
		-I /usr/include/hidapi \
		-l hidapi-libusb \
		-l usb-1.0
osx-joystick-json:
	gcc joystick-json.c -o joystick-json \
		-L /usr/local/lib \
		-I /usr/local/Cellar/libusb/1.0.26/include/libusb-1.0 -l usb-1.0 \
		-I /usr/local/Cellar/hidapi/0.14.0/include/hidapi -l hidapi 

pi-setup:
	pip install RPi.GPIO
