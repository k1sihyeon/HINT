import can, cantools, time, random

can_bus = can.Bus(interface='kvaser', channel=1, bitrate=1000000)
can_db = cantools.database.load_file('project.dbc')
messages_to_send = [message for message in can_db.messages if 'ECU1' in message.senders]

while True:
    for msg in messages_to_send:
        data = {sig.name: random.randint(sig.minimum or 0, sig.maximum or (2**sig.length - 1)) for sig in msg.signals}
        can_msg = can.Message(arbitration_id=msg.frame_id, data=msg.encode(data), is_extended_id=False)
        
        if (msg.send_type == 'Cyclic') and (msg.cycle_time is not None) and (msg.cycle_time > 0):
            interval = msg.cycle_time / 1000.0  # Convert milliseconds to seconds
        else:
            interval = 0.01
        
        try:
            can_bus.send(can_msg)
            print(f"Message sent: {can_msg}")
        except can.CanError:
            print("Message NOT sent")
            
        time.sleep(interval)

# Message received: Timestamp: 1790575551.556229    ID:      705    S Rx                DL:  8    23 70 dd 80 18 32 67 ea     Channel: 0
# Message received: Timestamp: 1790575551.567159    ID:      055    S Rx                DL:  8    52 3b 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790575551.577769    ID:      704    S Rx                DL:  8    69 13 31 26 bd 2e 90 e0     Channel: 0
# Message received: Timestamp: 1790575551.588529    ID:      200    S Rx                DL:  8    6e 6b 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790575551.599499    ID:      100    S Rx                DL:  8    0d cd 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790575551.800559    ID:      701    S Rx                DL:  8    81 29 c0 fb ff a1 7f 81     Channel: 0
# Message received: Timestamp: 1790575551.811909    ID:      602    S Rx                DL:  8    75 b5 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790575552.013059    ID:      601    S Rx                DL:  8    a5 5f 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790575552.214359    ID:      300    S Rx                DL:  8    16 be 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790575552.715649    ID:      502    S Rx                DL:  8    96 f9 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790575552.916349    ID:      501    S Rx                DL:  8    94 5d 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790575553.417249    ID:      401    S Rx                DL:  8    cf 00 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790575553.428549    ID:      102    S Rx                DL:  8    c2 40 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790575553.629729    ID:      101    S Rx                DL:  8    d6 f6 00 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790575553.831049    ID:      002    S Rx                DL:  8    5c 05 a2 04 0f 00 00 00     Channel: 0
# Message received: Timestamp: 1790575553.842309    ID:      001    S Rx                DL:  8    69 10 0b 00 00 00 00 00     Channel: 0
# Message received: Timestamp: 1790575553.853399    ID:      004    S Rx                DL:  1    01                          Channel: 0