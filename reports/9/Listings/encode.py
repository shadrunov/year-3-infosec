""" encode """

import struct

input_file = "cat.bmp"
output_file = "cat1.bmp"

# read offset
with open(input_file, "rb") as f:
    print("Reading file...")
    f.read(2)
    print("File size:", struct.unpack("<i", f.read(4))[0])
    f.read(4)
    offset = struct.unpack("<i", f.read(4))[0]
    print("Offset:", offset)

# prepare string
s = input("Enter string to encode: ")
sb = bytearray(s, "ascii")

# read from input_file and write to output_file
with open(input_file, "rb") as f:
    with open(output_file, "wb") as output_file:
        for i in range(offset):
            output_file.write(f.read(1))  # copy beginning

        sb_len = len(sb) % 255  # byte string length

        for i in range(8):  # record each bit of length
            symbol = (sb_len >> (7 - i)) & 1  # get one bit: 0 or 1
            b = int.from_bytes(f.read(1), "little")  # read one byte
            b = b & 0b11111110  # clear LSB
            b = b | symbol  # write LSB
            output_file.write(b.to_bytes(1, "little"))  # write to file

        for ch in sb:  # record bytes from string
            for i in range(8):  # each byte bit by bit
                symbol = (ch >> (7 - i)) & 1  # get one bit: 0 or 1
                b = int.from_bytes(f.read(1), "little")  # read one byte
                b = b & 0b11111110  # clear LSB
                b = b | symbol  # write LSB
                output_file.write(b.to_bytes(1, "little"))  # write to file

        while b := f.read():  # write file till the end
            output_file.write(b)
