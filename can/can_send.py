import can
import time

can_bus = can.Bus(interface='kvaser', channel=1, bitrate=1000000)
can_msg = can.Message(arbitration_id=0x123, data=[0, 25, 0, 1, 3, 1, 4, 1], is_extended_id=False)

while True:
    try:
        can_bus.send(can_msg)
        print(f"Message sent: {can_msg}")
    
    except can.CanError:
        print("Message NOT sent")
    
    time.sleep(1)


# Message sent: Timestamp: 0.000000    ID: 123   S Rx  DL: 8   00 19 00 01 03 01 04 01