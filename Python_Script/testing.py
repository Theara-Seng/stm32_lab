import can 
bus = can.interface.Bus(channel='can0', interface='socketcan',bitrate=1000000)
while True:
    message = bus.recv()
    int_byte = int.from_bytes(message.data[:2], "big")
    int_byte1 = int.from_bytes(message.data[2:4], "big")
   
    if int_byte1 > 0x7fff:
        int_byte1 = int_byte1 - 65536
    if int_byte > 0x7fff:
        int_byte = int_byte - 65536
    print(int_byte,int_byte1)
    
    # int_byte = int.from_bytes(message.data, "big")
   
   
    # print(int_byte)
    # if int_byte > 0x7fffffff:
    #     int_byte = int_byte - 4294967296
    # print("data1= %d, data2= %d, data3= %d, data4= %d"%(message.data[0],message.data[1],message.data[2],message.data[3]))
