from mccprolib.api import MegacellCharger

# Initiate the megacell charger class with the ip of your device
tester = MegacellCharger("192.168.1.152")

# The only macro available for now is mCap . mCap will do a charge to set voltage, discharge to min
# voltage then charge to store voltage. After fully charged, the ESR measurement will take place if
# slots are not grouped together. If there's more than 1 cell in a group, the ESR step will not be added
# and I recommend using an external ESR measurement tool like RC3563 or Yr1035

# Params for set_cell_macro
# cells: 0 to 15
# supported commands: mCap, stop
result = tester.set_cell_macro(0, "mCap")

print(result)
