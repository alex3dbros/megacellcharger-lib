from mccprolib.api import MegacellCharger
from cobs import cobs
import msgpack

# Initiate the megacell charger class with the ip of your device
tester = MegacellCharger("192.168.1.192")

# Get Chemistry for cell id
data = {
    "CiD": 0
}

result = tester.get_cell_chemistry(data)
print(result)

unpacked_data = msgpack.unpackb(result)
print(unpacked_data)
