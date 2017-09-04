#!/usr/bin/env python

from flask import Flask, jsonify
import soco
import ipaddress

app = Flask(__name__)

def devices(mydevice=None):
    if not mydevice:
        devicelist = soco.discover()
        if devicelist:
            devicelist = list(devicelist)
        else:
            devicelist = []
        return devicelist
    else:
        try:
            ipaddress.ip_address(mydevice)
            print(soco.SoCo(mydevice).ip_address)
        except:
            print(mydevice)
    return 0


@app.route('/sonos/devices', methods=['GET'])
def get_devices():
    mydevices = []
    for device in devices():
        mydevices.append({'ip': device.ip_address,
                        'name': device.player_name})
    return jsonify({'devices': mydevices})

@app.route('/sonos/devices/<string:device>', methods=['GET'])
def get_device(device):
    return jsonify({'devices': device})

if __name__ == '__main__':
    app.run(debug=True)

