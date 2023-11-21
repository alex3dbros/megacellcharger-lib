import serial
from cobs import cobs
import time
import msgpack

# Initialize the serial port
ser = serial.Serial('COM11', 115200)  # Change 'COM11' to your port name
recv_index = 0x34


def send_packet():
    # Encode the data using COBS encoding
    # The supported commands are the same with those from jSon SendCommand.py example
    data = {
        "cells": [{"CiD": 0, "CmD": "mCap"}]
    }
    encoded = msgpack.packb(data, use_bin_type=True)

    encoded_data = cobs.encode(encoded)

    # Write the encoded data to the serial port
    ser.write(encoded_data)

    # Add a zero-byte delimiter
    ser.write(b'\x00')


send_packet()

