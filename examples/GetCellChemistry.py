from mccprolib.api import MegacellCharger

# Initiate the megacell charger class with the ip of your device
tester = MegacellCharger("192.168.1.224")

chemistry = {
    "Chem":
        {
            "id": 5, #id's 1 to 4 are the ones shown on mcc menu, those cannot be modified
            "name": "MyCustom",
            "maxVolt": 4240,
            "minVolt": 2950,
            "sVolt": 3700,
            "maxCap": 500000,
            "chgCur": 1500,
            "pChgCur": 512,
            "terChgCur": 256,
            "dchgCur": 2000,
            "dchgRes": 1,
            "dchgMod": 0,
            "maxTemp": 50,
            "LmR": 400, # Low Voltage Recover Max Runtime in minutes
            "McH": 1200, # Max charge duration in minutes
            "DiC": 1, # Discharge cycles

        },
    "CiD": 0
}

# setting chemistry for one cell
# result = tester.set_cell_chemistry(chemistry)
# print(result)

# Setting the same chemistry to all cells
for i in range(16):
    newchemistry = {
        "Chem":
            {
                "id": 5, #id's 1 to 4 are the ones shown on mcc menu, those cannot be modified
                "name": "MyCustom",
                "maxVolt": 4240,
                "minVolt": 2950,
                "sVolt": 3700,
                "maxCap": 500000,
                "chgCur": 1500,
                "pChgCur": 512,
                "terChgCur": 256,
                "dchgCur": 2000,
                "dchgRes": 1,
                "dchgMod": 0,
                "maxTemp": 50,
                "LmR": 400, # Low Voltage Recover Max Runtime in minutes
                "McH": 1200, # Max charge duration in minutes
                "DiC": 1, # Discharge cycles

            },
        "CiD": i
    }

    result = tester.set_cell_chemistry(newchemistry)
    print(result)