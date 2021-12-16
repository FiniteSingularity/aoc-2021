import pprint


def process_packet(dat, start=0):
    packet = {}
    version = int(dat[0:3], 2)
    type_id = int(dat[3:6], 2)
    length = 0
    if type_id == 4:
        # literal value
        print('literal value')
        packet['type'] = 'literal_value'
        packet['type_id'] = type_id
        packet['version'] = version
        value_dat = dat[6:]
        length = 6
        idx = 0
        value_str = ''
        while True:
            length += 5
            value_str += value_dat[idx+1:idx+5]
            if value_dat[idx] == '0':
                break
            idx += 5
        packet['value'] = int(value_str, 2)
    else:
        packet['type'] = 'operator'
        packet['type_id'] = type_id
        packet['version'] = version
        packet['sub_packets'] = []
        length_type_id = dat[6]
        packet['length_type_id'] = length_type_id
        length = 7
        if length_type_id == '1':
            n_sub_packets = int(dat[7:18], 2)
            length = 18
            packet['n_sub_packets'] = n_sub_packets
            offset = 0
            for _ in range(0, n_sub_packets):
                sub_packet, sp_length = process_packet(dat[18+offset:])
                packet['sub_packets'].append(sub_packet)
                length += sp_length
                offset += sp_length
        elif length_type_id == '0':
            l_sub_packets = int(dat[7:22], 2)
            length = 22
            packet['l_sub_packets'] = l_sub_packets
            offset = 0
            while offset < l_sub_packets:
                sub_packet, sp_length = process_packet(dat[22+offset:])
                offset += sp_length
                length += sp_length
                packet['sub_packets'].append(sub_packet)
        if packet['type_id'] == 0:
            packet['value'] = 0
            for p in packet['sub_packets']:
                packet['value'] += p['value']
        elif packet['type_id'] == 1:
            packet['value'] = 1
            for p in packet['sub_packets']:
                packet['value'] *= p['value']
        elif packet['type_id'] == 2:
            packet['value'] = min([p['value'] for p in packet['sub_packets']])
        elif packet['type_id'] == 3:
            packet['value'] = max([p['value'] for p in packet['sub_packets']])
        elif packet['type_id'] == 5:
            packet['value'] = int(packet['sub_packets'][0]['value']
                                  > packet['sub_packets'][1]['value'])
        elif packet['type_id'] == 6:
            packet['value'] = int(packet['sub_packets'][0]['value']
                                  < packet['sub_packets'][1]['value'])
        elif packet['type_id'] == 7:
            packet['value'] = int(packet['sub_packets'][0]['value']
                                  == packet['sub_packets'][1]['value'])

    return (packet, length)


with open('./input', encoding='utf8') as file:
    transmission = file.readline().strip()


transmission_bin = bin(int(transmission, 16))[2:].zfill(len(transmission)*4)
print(transmission_bin)
packets, length = process_packet(transmission_bin)

pp = pprint.PrettyPrinter(width=41, compact=True)
pp.pprint(packets)


# print(transmission_bin)
