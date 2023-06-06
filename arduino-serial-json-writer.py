#!/usr/bin/env python3
import os, sys, json, subprocess, shlex, serial, time, queue, threading

DEBUG_MODE = False
JOYSTICK_JSON_COMMAND = './joystick-json'
port = '/dev/tty.usbserial-A601EGHU'


ser = serial.Serial()
q = queue.Queue()
ser.port = port
ser.baudrate = 115200
ser.open()
print("opening serial port...")
time.sleep(2)
print("serial port ready...")

def worker():
    qty = 0
    while True:
        qty = qty+1
        t = q.get()
        ser.write(t)
        if DEBUG_MODE:
         if (qty % 10) == 0:
          print(t)
        q.task_done()

def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            output = bytes(output.decode().strip() + '\n','utf-8')
            q.put(output)
    rc = process.poll()
    return rc

def main():
  threading.Thread(target=worker, daemon=True).start()
  q.join()
  run_command(JOYSTICK_JSON_COMMAND)

main()
