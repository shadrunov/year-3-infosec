""" decode """

import struct

input_file = "cat1.bmp"

with open(input_file, "rb") as f:
    print("Reading file...")
    f.read(2)
    print("File size:", struct.unpack("<i", f.read(4))[0])
    f.read(4)
    offset = struct.unpack("<i", f.read(4))[0]
    print("Offset:", offset)

sb = bytearray("", "ascii")  # prepare string

with open(input_file, "rb") as f:
    f.read(offset)  # skip offset

    # get string length from file
    sb_len = 0
    for i in range(8):
        symbol = f.read(1)
        symbol = int.from_bytes(symbol, "little")
        symbol = symbol & 1  # get LSB
        sb_len = (symbol << (7 - i)) | sb_len  # construct byte from LSB

    # get string from file
    for j in range(sb_len):
        ch = 0
        for i in range(8):
            symbol = f.read(1)
            symbol = int.from_bytes(symbol, "little")
            symbol = symbol & 1  # get LSB
            ch = (symbol << (7 - i)) | ch  # construct byte from LSB
        sb.append(ch)  # add byte to string

print("Decoded string is:", sb.decode("ascii"))
