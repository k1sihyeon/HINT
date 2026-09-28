import can
import cantools
import time
import random

can_bus = can.Bus(interface='kvaser', channel=1, bitrate=1000000)
can_db = cantools.database.load_file('project.dbc')
messages_to_send = [message for message in can_db.messages if 'ECU1' in message.senders]

while True:
    for msg in messages_to_send:
        data = {sig.name: random.randint(sig.minimum or 0, sig.maximum or (2**sig.length - 1)) for sig in msg.signals}
        can_msg = can.Message(arbitration_id=msg.frame_id, data=msg.encode(data), is_extended_id=False)
        
        try:
            can_bus.send(can_msg)
            print(f"Message sent: {can_msg}")
            
        except can.CanError:
            print("Message NOT sent")
        
    time.sleep(3)


# Message received: Timestamp: 1790572034.928745    ID:      705    S Rx                DL:  8    db c4 83 54 d7 4d 37 26     Channel: 0
# Message received: Timestamp: 1790572034.929315    ID:      055    S Rx                DL:  8    8c 15 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790572034.929885    ID:      704    S Rx                DL:  8    6b 77 5d fd 3a 8c a4 e4     Channel: 0
# Message received: Timestamp: 1790572034.930535    ID:      200    S Rx                DL:  8    8e 22 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790572034.930895    ID:      100    S Rx                DL:  8    8a 16 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790572034.931205    ID:      701    S Rx                DL:  8    0d f4 95 03 2e 44 1c 2d     Channel: 0
# Message received: Timestamp: 1790572034.931685    ID:      602    S Rx                DL:  8    74 88 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790572034.931975    ID:      601    S Rx                DL:  8    ef ed 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790572034.932415    ID:      300    S Rx                DL:  8    23 c1 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790572034.932635    ID:      502    S Rx                DL:  8    f1 1c 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790572034.932865    ID:      501    S Rx                DL:  8    48 d0 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790572034.933235    ID:      401    S Rx                DL:  8    b1 00 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790572034.933435    ID:      102    S Rx                DL:  8    12 16 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790572034.933615    ID:      101    S Rx                DL:  8    15 63 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790572034.933815    ID:      002    S Rx                DL:  8    3a 01 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790572034.933915    ID:      001    S Rx                DL:  8    5c 20 09 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790572034.933985    ID:      004    S Rx                DL:  1    00                          Channel: 0

# Message received: Timestamp: 1790572037.934385    ID:      705    S Rx                DL:  8    b8 49 8f af e9 d1 fe 3b     Channel: 0
# Message received: Timestamp: 1790572037.934535    ID:      055    S Rx                DL:  8    c9 56 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790572037.934675    ID:      704    S Rx                DL:  8    3b 55 84 5f 01 6f 19 b0     Channel: 0
# Message received: Timestamp: 1790572037.934775    ID:      200    S Rx                DL:  8    3a 88 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790572037.934905    ID:      100    S Rx                DL:  8    da 72 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790572037.935015    ID:      701    S Rx                DL:  8    93 7d b7 c8 61 34 23 ce     Channel: 0
# Message received: Timestamp: 1790572037.935235    ID:      602    S Rx                DL:  8    34 fa 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790572037.935325    ID:      601    S Rx                DL:  8    63 a5 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790572037.935375    ID:      300    S Rx                DL:  8    98 1d 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790572037.935425    ID:      502    S Rx                DL:  8    ea eb 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790572037.935485    ID:      501    S Rx                DL:  8    56 09 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790572037.935575    ID:      401    S Rx                DL:  8    0d 00 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790572037.935645    ID:      102    S Rx                DL:  8    44 5e 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790572037.935715    ID:      101    S Rx                DL:  8    ba 4b 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790572037.935835    ID:      002    S Rx                DL:  8    39 05 13 05 02 00 00 00     Channel: 0
# Message received: Timestamp: 1790572037.935895    ID:      001    S Rx                DL:  8    fd c0 09 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790572037.935955    ID:      004    S Rx                DL:  1    01                          Channel: 0