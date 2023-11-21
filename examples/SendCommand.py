from mccprolib.api import MegacellCharger

# Initiate the megacell charger class with the ip of your device
tester = MegacellCharger("192.168.1.224")

# Run the set_cell command, this will send the command to the cell you specify 0 to 15
# Check api.py for more info on what commands are supported
result = tester.set_cell(1, "sc")

print(result)
