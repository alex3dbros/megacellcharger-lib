from mccprolib.api import MegacellCharger

# Initiate the megacell charger class with the ip of your device
tester = MegacellCharger("192.168.1.224")

# Set hardware config will do the following operations:

# First parameter can be 0 or 1, this will set the temp source
# 0 = Onboard temp sensor, 1 = Accessory temp sensor

# Second parameter will set the number of cells available for grouping,
# 1 to 16 is the value that can be set. If you set the parmeter to 8 and
# 3rd parameter to 2, this will create 4 cell groups of 2 and the rest of
# 8 slots will remain regular. The cell grouping is helpful when you want
# to charge / discharge the cells with more power. You will achieve this by
# connecting the grouped slots in parallel with accessories for XS12 slots.
# When cells are grouped, it's recommended to have at least one of the connections
# with a temperature sensor. That temperature sensor will be used for the entire
# group.

# 3rd parameter sets the number of cells per group. If the second parameter is set
# to 8 and the 3rd parmaeters to 3, this will create 2 groups of 3 cells and the
# remaining ones will remain ungrouped and will be treated as regular cells.
# On the display you will see the cells that are grouped together being closer.

# The 4th parameter sets the data feed type. Supported datafeed types:
# 0 - jSon, 1 - Multicast (not  available for now), 2 - Binary TCP (not available for now),
# 3 - Binary UDP, 4 - (Binary USB)

# More info about the grouping behaviour:
# When a group has more than 1 cell, the following behaviour can be observed:
# - If a command is sent to any of the cells in that group, the group will follow that command
# - If the group has more than 1 temp sensor, the temp sensor with higher temperature will be used
# to trigger any eventual stopping procedure
# - When charging or discharging, the process will wait until all slots complete the procedure before
# moving to the next step

res = tester.set_hardware_config(0, 16, 1, 0)

print(res)
