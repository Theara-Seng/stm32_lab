#!/usr/bin/env python

"""
This example shows how sending a single message works.
"""

import can

bus = can.interface.Bus(channel='can0', interface='socketcan',bitrate=1000000)

def send_one():
    """Sends a single message."""




    msg = can.Message(
        arbitration_id=0x111, data=[0x10,0x50], is_extended_id=False
    )

    try:
        bus.send(msg,0.01)
        print(f"Message sent on {bus.channel_info}")
    except can.CanError:
        print("Message NOT sent")


if __name__ == "__main__":
    while True:
        send_one()