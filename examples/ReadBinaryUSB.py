import serial
from cobs import cobs
import time
import msgpack

# Initialize the serial port
ser = serial.Serial('COM11', 115200)  # Change 'COM11' to your port name
recv_index = 0x34


def read_packet():
    packet = bytearray()
    while True:
        # Read one byte from the serial port
        byte = ser.read(1)

        if byte[0] == recv_index:
            while True:
                byte = ser.read(1)

                # print(f"Adding Bytes: {packet}")
                if byte[0] == 0x00:  # End of msgpack bytes
                    break
                packet.extend(byte)

            try:
                # print(f"Packet: {packet}")
                decoded_packet = cobs.decode(packet)
                # print(f"Received: {decoded_packet}")

                # print(f"Attempting to decode: {decoded_packet}")
                unpacked_data = msgpack.unpackb(decoded_packet)  # Remove last byte
                print(unpacked_data)
                packet = bytearray()

            except cobs.DecodeError:
                print("Decode Error")
                print(packet);
                packet = bytearray()


try:
    # Keep listening for incoming data
    while True:
        read_packet()

except KeyboardInterrupt:
    # Close the serial port if Ctrl+C is pressed
    ser.close()
    print("Serial port closed.")
