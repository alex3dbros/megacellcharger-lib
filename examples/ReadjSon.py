from mccprolib.api import MegacellCharger

# Initiate the megacell charger class with the ip of your device
tester = MegacellCharger("192.168.1.224")

# This will return a json containing all the data for all 16 cells
result = tester.get_cells_data()

print(result)

# Example result:


# {
#     "cells":[
#         {
#             "CiD":0, // Cell ID 0 to 15
#             "VlT":3.92, // Voltage
#             "AmP":0, // Current, if positive is charging current, if negative is discharging current
#             "CaP":0.0, // The capacity measured during discharging
#             "CCa":18.65, // The capacity measured during charging

#             "StS":"Regular Cell", // Status ( Not Inserted, Cell inserted, Checking Chemistry, LVC Cell, Regular Cell, Bad VC Reading, Too Cold,
#             LVC Charging, Started Charging, Cooldown, Charging Failed, Checking if Charged, Volt Drop Check, Charged, Anormal Charged, Bad Cell,
#             Started Discharging, Discharged, Discharge Failed, ESR Reading, ESR Read Completed, ESR Read Failed, Resting, Rested,
#             Checking Store Action, Started Store Charging, Started Store Discharging, Checking If Stored, Stored, Failed Store, Dispose started,
#             Disposed, Error

#             "esr":0.0, // Internal resistance measured with volt drop and applying ohms law
#             "AcL":47.23, // Total running time in seconds
#             "DiC":1, // The set discharge cycles
#             "CoC":0, // Completed discharge cycles
#             "TmP":22.26, // Temperature in degree Celsius
#             "ChC":false, // no longer used, will be removed in future firmwares
#             "CcO":1, // not used
#             "DcO":1, // not used
#             "MaV":4.24, // Max voltage in current chemistry
#             "StV":3.7, // Store voltage in current chemistry
#             "MiV":2.95, // Min voltage in current chemistry
#             "GiD":0, // Group id (useful when multiple slots are grouped together)
#             "StT":"Not Set" // Not used
#         },
#         .....