from mccprolib.api import MegacellCharger
from cobs import cobs
import msgpack

# Initiate the megacell charger class with the ip of your device
tester = MegacellCharger("192.168.1.192")

# Get Chemistry
data = {
    "CiD": 0
}

result = tester.get_cell_chemistry(data)
print(result)

# decoded_packet = cobs.decode(result)
# print(f"Received: {decoded_packet}")

unpacked_data = msgpack.unpackb(result)  # Remove last byte
print(unpacked_data)
# packet = bytearray()