import can

channels = can.detect_available_configs(interfaces='kvaser')

print("Available CAN channels:")

for channel in channels:
    print(f"- {channel}")
  
  
# Available CAN channels:
# - {'interface': 'kvaser', 'channel': 0, 'device_name': 'Kvaser Virtual CAN Driver', 'serial': 0, 'dongle_channel': 1}
# - {'interface': 'kvaser', 'channel': 1, 'device_name': 'Kvaser Virtual CAN Driver', 'serial': 0, 'dongle_channel': 2}
# - {'interface': 'kvaser', 'channel': 2, 'device_name': 'Kvaser Virtual CAN Driver', 'serial': 0, 'dongle_channel': 3}
# - {'interface': 'kvaser', 'channel': 3, 'device_name': 'Kvaser Virtual CAN Driver', 'serial': 0, 'dongle_channel': 4}
# - {'interface': 'kvaser', 'channel': 4, 'device_name': 'Kvaser Virtual CAN Driver', 'serial': 0, 'dongle_channel': 5}
# - {'interface': 'kvaser', 'channel': 5, 'device_name': 'Kvaser Virtual CAN Driver', 'serial': 0, 'dongle_channel': 6}
# - {'interface': 'kvaser', 'channel': 6, 'device_name': 'Kvaser Virtual CAN Driver', 'serial': 0, 'dongle_channel': 7}
# - {'interface': 'kvaser', 'channel': 7, 'device_name': 'Kvaser Virtual CAN Driver', 'serial': 0, 'dongle_channel': 8}