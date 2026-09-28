import can
import cantools
import time
import random

can_bus = can.Bus(interface='kvaser', channel=1, bitrate=1000000)
can_db = cantools.database.load_file('project.dbc')
messages_to_send = [message for message in can_db.messages if 'ECU1' in message.senders]

while True:
    for msg in messages_to_send:
        data  = {}
        
        for  sig in msg.signals:
            sig_info = {
                'name' : sig. name, 'start' : sig.start, 'length' : sig.length,
                'byte_order' : 'little_endian' if sig.byte_order == 'little_endian' else 'big_endian',
                'minimum' : sig.minimum, 'maximum' : sig.maximum
            }
            
            print(f"Signal Info: {sig_info}")
            
            value = random.randint(sig.minimum or 0, sig.maximum or (2**sig.length - 1))
            data[sig.name] = value
            
        can_msg = can.Message(arbitration_id=msg.frame_id, data=msg.encode(data), is_extended_id=False)
        
        try:
            can_bus.send(can_msg)
            print(f"Message sent: {can_msg}")
            
        except can.CanError:
            print("Message NOT sent")
            
        time.sleep(0.5)
        

# Signal Info: {'name': 'ECU1_GST_TP_Sig1', 'start': 7, 'length': 64, 'byte_order': 'big_endian', 'minimum': None, 'maximum': None}
# Message sent: Timestamp:        0.000000    ID:      705    S Rx                DL:  8    9e fc 9c ab 38 8d 98 47
# Signal Info: {'name': 'ECU1_Msg_GW1_Sig1', 'start': 7, 'length': 8, 'byte_order': 'big_endian', 'minimum': None, 'maximum': None}
# Signal Info: {'name': 'ECU1_Msg_GW1_Sig2', 'start': 15, 'length': 8, 'byte_order': 'big_endian', 'minimum': None, 'maximum': None}
# Message sent: Timestamp:        0.000000    ID:      055    S Rx                DL:  8    d1 9e 00 00 00 00 00 00
# Signal Info: {'name': 'ECU1_Msg_TP2_Sig1', 'start': 0, 'length': 64, 'byte_order': 'little_endian', 'minimum': None, 'maximum': None}
# Message sent: Timestamp:        0.000000    ID:      704    S Rx                DL:  8    32 e5 ba 94 be 5e ab be
# ...