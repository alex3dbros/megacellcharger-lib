import socket
import struct

# Setup UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.1.224', 8886)

# Send "join" command
sock.sendto(b"join", server_address)


def unpack_data(data):
    # Update format string according to C++ struct types
    format_string = '<I i i i i i f H H i i i i B 20s'
    size = struct.calcsize(format_string)

    unpacked_data = struct.unpack(format_string, data[:size])
    fields = ['cellID', 'voltage', 'current', 'dischargeCap', 'chargeCap', 'esr', 'totalRuntime',
              'setDischargeCycles', 'completedDischargeCycles', 'temperature', 'maxVolt', 'storeVolt',
              'minVolt', 'cellGroupID', 'status']

    data_dict = {fields[i]: unpacked_data[i] for i in range(len(fields))}

    # Decode status assuming it is null-terminated
    status = data_dict['status'].split(b'\x00', 1)[0].decode('utf-8')
    data_dict['status'] = status

    return data_dict


# Listen for incoming data
while True:
    print("Waiting for data...")
    data, address = sock.recvfrom(4096)  # buffer size is 4096 bytes
    # print(f"Received {len(data)} bytes: {data}")

    if len(data) > 8:  # Validate that we have exactly 8 bytes
        # Unpack the data

        result = unpack_data(data)
        print(result)

    else:
        print(f"Unexpected data length: {len(data)}")




