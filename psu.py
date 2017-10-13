import telnetlib
import time
import config
import socket

class PSU:
    def __init__(self):
        self.tel = telnetlib.Telnet()

    def connect(self):
        try:
            self.tel.open(config.HOST, config.PORT, timeout=config.TIMEOUT)
        except socket.timeout:
            return False
        return True

    def disconnect(self):
        self.tel.close()

    def send(self, message):
        print("sending: {}".format(message))
        self.tel.write(message.encode())
        #self.tel.write('/n'.encode())

    def read(self):
        try:
            return self.tel.read_eager().decode("utf-8").strip()
        except EOFError:
            return "EOFError"

    def get_id(self):
        self.send(config.GET_ID)
        time.sleep(0.1)
        return self.read()

    def get_voltage(self):
        self.send(config.GET_VOLTAGE)
        time.sleep(0.1)
        return self.read()

    def get_current(self):
        self.send(config.GET_CURRENT)
        time.sleep(0.1)
        return self.read()

    def is_on(self):
        self.send(config.IS_ON)
        time.sleep(0.1)
        return self.read()

    def turn_on(self):
        self.send(config.TURN_ON)

    def turn_off(self):
        self.send(config.TURN_OFF)

    def set_voltage(self, v):
        self.send("{} {:.2f}".format(config.SET_VOLTAGE, v))

    def set_current_limit(self, i):
        self.send("{} {:.2f}".format(config.SET_CURRENT_LIMIT, i))

    def start_ramp(self, i):
        self.send("{} {:.2f}".format(config.SET_CURRENT_LIMIT, i))
