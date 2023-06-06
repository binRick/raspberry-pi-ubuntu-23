import os, sys, json, subprocess, shlex, serial, time, queue, threading, uvloop, asyncio

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


class MyProtocol(asyncio.Protocol):

    def connection_made(self, transport):
        print('pipe opened', file=sys.stderr, flush=True)
        super(MyProtocol, self).connection_made(transport=transport)

    def data_received(self, data):
        print(f"working with {len(data)}")
        #data = bytes(data+"\n",'utf-8')
        #print(data)
#        print("\n")
        #print(f'received: {data}', file=sys.stderr, flush=True)
#        print(data.decode(), file=sys.stderr, flush=True)
        super(MyProtocol, self).data_received(data)

    def connection_lost(self, exc):
        print('pipe closed', file=sys.stderr, flush=True)
        super(MyProtocol, self).connection_lost(exc)

if __name__ == "__main__":
    with open("/dev/stdin", "rb", buffering=0) as stdin:
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
        loop = asyncio.get_event_loop()
        try:
            stdin_pipe_reader = loop.connect_read_pipe(MyProtocol, stdin)
            loop.run_until_complete(stdin_pipe_reader)
            loop.run_forever()
        finally:
            loop.close()
