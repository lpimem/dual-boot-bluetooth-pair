# Dual Boot Bluetooth Pair

This is a tool originally created by [LondonAppDeveloper](https://github.com/LondonAppDeveloper). 

I modified it to work on _Windows 10 Home Edition_ and _Ubuntu 18.04 LTS_. 

## The Problem 

If you installed both Windows and Linux on the same machine and use the same Bluetooth devices on both OS, you may find yourself re-pairing the devices everytime you switch the OS. The instructions and scripts in this project can help you be able to pair the devices only once on each OS. 

### Reason of the problem

When a Bluetooth pairing process is done, a link key is negotiated between the device and the OS. If the device identifies the other paired party by its adapter MAC address only, it cannot distinguish between the two OS as they share the same Bluetooth adapter with only one MAC address. After pairing with the second OS, the key negotiated with the first OS will be overwritten even if the device supports multiple pairing connections. And the first OS cannot know the link key changed. 

### Solution 

First, we pair the device with Ubuntu and Windows. Now the Windows' link key is up-to-date but Ubuntu's is invalid. 
Then, we copy the link key from Windows 10 to Ubuntu so that the two OS share the same link key.

## Disclaimer

This script involves accessing and modifying system files on the Windows / Linux systems and may risk damaging your computer. 

This script is only tested on _Windows 10 Home Edition_ and _Ubuntu 18.04 LTS_. 

__Proceed with the below steps at your own risk.__

## Instructions

> Backup all config files before attempting the below steps.

The scripts in this project are intended to be executed on your Linux OS using [Python3](https://www.python.org/).

 1. Boot into Linux and pair bluetooth device(s).
 2. Reboot into Windows and pair bluetooth device(s).
 3. Download [PSExec](http://live.sysinternals.com/psexec.exe) and run the following command from a Command Prompt running __in Administator mode__:

```
psexec.exe -s -i regedit /e C:\BTKeys.reg HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\BTHPORT\Parameters\Keys
```

 4. Copy the `C:\BTKeys.reg` file to a USB key (or any place that is accessible from the Linux OS).
 5. Turn off bluetooth device(s) and boot back into Linux.
 6. Copy the `BTKeys.reg` file to your Linux filesystem.
 7. Run `clean_reg_file.py /path/to/BTKeys.reg keys.reg` to clean the file (converts encoding to UTF8 and strips quotation marks).
 8. Run `bluetooth_fix.py --reg_path keys.reg`.
 9. From a terminal with `sudo`, navigate to `/var/lib/bluetooth/<ADAPTOR_MAC_ADDRESS>/` and use `ls` to get the mac addresses similar to the bluetooth device you are trying to pair.
 10. Open `/var/lib/bluetooth/<ADAPTOR_MAC>/<DEVICE_MAC>/info` and modify the `LinkKey->Key` value as per output from step 8.
 11. Restart bluetooth with `sudo /etc/init.d/bluetooth restart`.
 12. Turn on Bluetooth device.

# Developer Notes

Contributions to this project are welcome! Feel free to fork and submit pull requests with any improvements.
