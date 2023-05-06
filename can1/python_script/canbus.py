import can 
bus = can.interface.Bus(channel='can0', interface='socketcan',bitrate=1000000)
while True:
    message = bus.recv()
    print("data1= %d, data2= %d, data3= %d, data4= %d"%(message.data[0],message.data[1],message.data[2],message.data[3]))

