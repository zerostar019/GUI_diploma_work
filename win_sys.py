import os, sys, platform, subprocess, multiprocessing
import GPUtil
import wmi
import psutil

# MOTHERBOARD SERIAL NUMBER
def getMachine_addr():
	os_type = sys.platform.lower()
	if "win" in os_type:
		command = "wmic bios get serialnumber"
	elif "linux" in os_type:
		command = "hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid"
	elif "darwin" in os_type:
		command = "ioreg -l | grep IOPlatformSerialNumber"
	return os.popen(command).read().replace("\n","").replace("	","").replace(" ","")

#output machine serial code: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXX

def get_processor_info():
    if platform.system() == "Windows":
        return platform.processor()
    elif platform.system() == "Darwin":
        return subprocess.check_output(['/usr/sbin/sysctl', "-n", "machdep.cpu.brand_string"]).strip()
    elif platform.system() == "Linux":
        command = "cat /proc/cpuinfo"
        return subprocess.check_output(command, shell=True).strip()
    return ""


def get_hdd():
    serials = subprocess.check_output('wmic diskdrive get SerialNumber').decode().split('\n')[1:]
    serials = [s.strip() for s in serials if s.strip()]
    return serials[0]

def get_gpu():
    c = wmi.WMI()
    gpu = c.WIN32_VideoController()[0].name
    return gpu
    
    
def get_sound():
    c = wmi.WMI()
    sound = c.WIN32_SoundDevice()[0].name
    return sound
    
def get_network():
    c = wmi.WMI()
    network = c.WIN32_NetworkAdapterConfiguration()
    for adapter in network:
        if adapter.IPEnabled:
            print(f"Network adapter: {adapter.Description}")
            
def get_RAM():
    c = wmi.WMI()
    chip = c.WIN32_PhysicalMemory()[0]
    return str(chip.manufacturer)
