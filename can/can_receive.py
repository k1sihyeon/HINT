import can

can_bus = can.Bus(interface='kvaser', channel=0, bitrate=1000000)

while True:
    can_msg = can_bus.recv()
    
    if can_msg:
        print(f"Message received: {can_msg}")

        
# Message received: Timestamp: 1790561696.872106    ID: 123    S Rx   DL: 8    00 19 00 01 03 01 04 01     Channel: 0
