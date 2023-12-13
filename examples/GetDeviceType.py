from mccprolib.api import MegacellCharger

# Initiate the megacell charger class with the ip of your device
tester = MegacellCharger("192.168.1.224")

# This will return a json containing device info
result = tester.get_device_type()

print(result)