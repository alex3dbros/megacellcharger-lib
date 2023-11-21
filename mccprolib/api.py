import requests
import json


class MegacellCharger:
    def __init__(self, ip):
        self.ip = ip
        self.headers = {'content-type': 'application/json'}

    def get_cells_data(self):
        data = {
            "start": 1, "end": 16
        }
        result = self.get_data(data, "api/get_cells_info")
        return result

    # set_cell used for setting cell commands
    # start charging: ach, start discharging: adc, stop charging: sc,
    # stop discharging: odc, Start Store Charging: asc
    # Stop Store charging: sc, Dispose Cell: dsp, Stop Dispose: odc
    # Start ESR Test: esr
    def set_cell(self, CiD, Cmd):
        data = {
            "cells": [{"CiD": CiD, "CmD": Cmd}]
        }

        result = self.set_data(data, "api/set_cell")
        return result

    def set_cell_macro(self, CiD, Cmd):
        data = {
            "cells": [{"CiD": CiD, "CmD": Cmd}]
        }

        result = self.set_data(data, "api/set_cell_macro")
        return result

    def set_pid(self, Kp, Ki, Kd):
        data = {
            "cells": [{"Kp": Kp, "Ki": Ki, "Kd": Kd, "CiD": 0, "CmD": "setPID"}]
        }

        result = self.set_data(data, "api/set_pid")
        return result

    def set_hardware_config(self, temp_source, cell_to_group, cell_per_group, data_feed_type):
        data = {"tempSource": temp_source, "cellsToGroup": cell_to_group, "maxCellPerGroup": cell_per_group, "dataFeedType": data_feed_type}

        result = self.set_data(data, "api/set_hw_conf")
        return result

    def get_config(self):
        data = {}
        result = self.get_data(data, "api/get_config_info")
        return result

    def set_config(self, config):
        result = self.set_data(config, "api/set_config_info")
        return result

    def set_cell_chemistry(self, config):
        result = self.set_data(config, "api/set_chemistry")
        return result

    def get_data(self, data, api_addr):
        req_uri = "http://" + self.ip + "/" + api_addr
        req = requests.post(req_uri, data=json.dumps(data), headers=self.headers)
        return req.json()

    def set_data(self, data, api_addr):
        req_uri = "http://" + self.ip + "/" + api_addr
        req = requests.post(req_uri, data=json.dumps(data), headers=self.headers)
        return req.content


    @staticmethod
    def send_data_api(address, api_addr, data):
        req_uri = address + "/" + api_addr
        headers = {'content-type': 'application/json'}

        req = requests.post(req_uri, data=json.dumps(data), headers=headers)
        return req.text



