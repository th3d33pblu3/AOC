def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

# Ver : 3 bits
# Type: 3 bits
#       0 - Sum
#       1 - Product
#       2 - Minimum
#       3 - Maximum
#       4 - Literal
#       5 - Greater than
#       6 - Less than
#       7 - Equal to
# Len : 1 bit , 0 - 15 bits total length, 1 - 11 bits number of packets

converter = {"0": "0000", "1": "0001", "2": "0010", "3": "0011",
             "4": "0100", "5": "0101", "6": "0110", "7": "0111",
             "8": "1000", "9": "1001", "A": "1010", "B": "1011",
             "C": "1100", "D": "1101", "E": "1110", "F": "1111"}

def data_to_bits(data):
    bits = ""
    for char in data:
        bits += converter.get(char)
    return bits

class Packet:
    def __init__(self, p_ver, p_type):
        self.p_ver = p_ver
        self.p_type = p_type

    def get_version(self):
        return self.p_ver

    def get_version_sum(self):
        pass

    def get_value(self):
        pass

class Literal(Packet):
    def __init__(self, p_ver, p_type, literal):
        super().__init__(p_ver, p_type)
        self.literal = literal
    
    def get_version_sum(self):
        return super().get_version()

    def get_value(self):
        return self.literal

class Operator(Packet):
    def __init__(self, p_ver, p_type, len_type, length, packets: list[Packet]):
        super().__init__(p_ver, p_type)
        self.len_type = len_type
        self.length = length
        self.packets = packets

    def get_version_sum(self):
        sum = super().get_version()
        for packet in self.packets:
            sum += packet.get_version_sum()
        return sum

    def get_value(self):
        if self.p_type == 0:   # Sum
            result = 0
            for packet in self.packets:
                result += packet.get_value()
            return result
        elif self.p_type == 1: # Product
            result = 1
            for packet in self.packets:
                result *= packet.get_value()
            return result
        elif self.p_type == 2: # Minimum
            result = self.packets[0].get_value()
            for packet in self.packets[1:]:
                value = packet.get_value()
                if value < result:
                    result = value
            return result
        elif self.p_type == 3: # Maximum
            result = self.packets[0].get_value()
            for packet in self.packets[1:]:
                value = packet.get_value()
                if value > result:
                    result = value
            return result
        elif self.p_type == 4: # Literal
            raise Exception("Literal is not an operation.")
        elif self.p_type == 5: # Greater than
            a = self.packets[0].get_value()
            b = self.packets[1].get_value()
            return 1 if a > b else 0
        elif self.p_type == 6: # Less than
            a = self.packets[0].get_value()
            b = self.packets[1].get_value()
            return 1 if a < b else 0
        elif self.p_type == 7: # Equal to
            a = self.packets[0].get_value()
            b = self.packets[1].get_value()
            return 1 if a == b else 0

class Decoder:
    LITERAL = 4

    LEN_TYPE_0 = 0
    LEN_TYPE_1 = 1

    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __get_packet_version(self):
        bit_ver = self.data[self.index : self.index + 3]
        self.index += 3
        
        return int(bit_ver, 2)

    def __get_packet_type(self):
        bit_type = self.data[self.index : self.index + 3]
        self.index += 3
        
        return int(bit_type, 2)
    
    def __get_packet_length_type(self):
        bit_length_type = self.data[self.index]
        self.index += 1

        return int(bit_length_type)

    def __get_packet_length(self):
        packet_length = self.data[self.index : self.index + 15]
        self.index += 15

        return int(packet_length, 2)

    def __get_num_packets(self):
        num_packets = self.data[self.index : self.index + 11]
        self.index += 11

        return int(num_packets, 2)

    def __get_next_bit(self):
        bit = self.data[self.index]
        self.index += 1

        return int(bit, 2)

    def __get_next_four_bits(self):
        bits = self.data[self.index : self.index + 4]
        self.index += 4

        return bits

    def __is_literal_packet(self, packet_type):
        return packet_type == self.LITERAL

    def __read_literal(self):
        next = self.__get_next_bit()
        bits = self.__get_next_four_bits()
        while next != 0:
            next = self.__get_next_bit()
            bits += self.__get_next_four_bits()
        value = 0
        for bit in bits:
            value *= 2
            value += int(bit)
        return value

    def decode(self):
        packet_version = self.__get_packet_version()
        packet_type = self.__get_packet_type()

        if self.__is_literal_packet(packet_type):
            return Literal(packet_version, packet_type, self.__read_literal())
        else:
            packet_length_type = self.__get_packet_length_type()

            if packet_length_type == self.LEN_TYPE_0:
                packet_length = self.__get_packet_length()
                list_packets = self.__decode_fixed_length(packet_length)
                return Operator(packet_version, packet_type, packet_length_type, packet_length, list_packets)
            elif packet_length_type == self.LEN_TYPE_1:
                num_packets = self.__get_num_packets()
                list_packets = []
                for _ in range(num_packets):
                    list_packets.append(self.decode())
                return Operator(packet_version, packet_type, packet_length_type, num_packets, list_packets)
            else:
                raise Exception("Unknown packet length type.")

    def __decode_fixed_length(self, length):
        limit = self.index + length
        packets = []
        while self.index < limit:
            packets.append(self.decode())
        return packets

def solve_part_1():
    file = read_input_file()
    raw_data = file.read()
    data = data_to_bits(raw_data)
    packet = Decoder(data).decode()
    return packet.get_version_sum()

def solve_part_2():
    file = read_input_file()
    raw_data = file.read()
    data = data_to_bits(raw_data)
    packet = Decoder(data).decode()
    return packet.get_value()
    
print(solve_part_2())
