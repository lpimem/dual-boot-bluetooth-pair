#!/usr/bin/env python3

import configparser
import argparse

'''
    This script will parse the cleaned reg file and output the following items:
    1. Installed Bluetooth MAC address. This will also be the folder you need
       to find in /var/lib/bluetooth directory.  
    2. For each paired device:
        - MAC Address
        - Link Key

'''


def _parse_args():
    """Parse arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--reg_path', help='Path to reg file.', default='keys.reg')

    return parser.parse_args()


def _open_reg_file(file_path):
    """ Open file at given path and return as config option."""
    config = configparser.ConfigParser()
    config.read_file(open(file_path))

    return config


def _insert_mac_colons(mac):
    """ Bluetooth Mac directory file name."""
    mac = mac.upper()
    mac_parts = [mac[i:i + 2] for i in range(0, len(mac), 2)]
    # import pdb; pdb.set_trace()
    return ':'.join(mac_parts)


def _bluetooth_dir_name(section_name):
    """ Return the bluetooth directory name."""
    full_path = section_name.split('\\')
    mac = full_path[-1]
    return _insert_mac_colons(mac)


def _process_reg_file(config):
    """ Process the reg file."""
    sections = config.sections()
    for section in sections:
        if len(config[section]) == 0:
            continue
        bluetooth_dir = _bluetooth_dir_name(section)
        print("Installed BT MAC (Dirname):")
        print(bluetooth_dir)
        print("= " * 10)
        print("P A I R E D    D E V I C E S:")
        print("- " * 10)
        for mac in config[section]: 
            key =config[section][mac]
            key = key.replace("hex:", "")
            key = key.replace(",", "")
            print("MAC:", _insert_mac_colons(mac))
            print("KEY:", key)
            print("- " * 10)
        
def main():
    """ Main entrypoint to script. """
    args = _parse_args()
    config = _open_reg_file(args.reg_path)
    _process_reg_file(config)


if __name__ == '__main__':
    main()
