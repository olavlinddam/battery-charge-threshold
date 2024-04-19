import os
import subprocess

import distro

def set_charging_threshold():
    bat_charge_end_threshold = open("/sys/class/power_supply/BAT0/charge_control_end_threshold", "w")
    bat_charge_end_threshold.write("85")


def set_power_profile():
    power_supply_battery_path = "/sys/class/power_supply/BAT0"

    status = ""

    status_path = os.path.join(power_supply_battery_path, "status")

    # Check if the status file exists
    if os.path.exists(status_path):
        # Read the status file
        with open(status_path, "r") as file:
            status = file.read().strip()
        

    power_saver_profile_command = "powerprofilesctl set power-saver"
    performance_profile_command = "powerprofilesctl set performance"
    if distro.id() == "pop":
        power_saver_profile_command = "system76-power profile battery"
        performance_profile_command = "system76-power profile performance"

    if status.lower() == "discharging":
        os.system(power_saver_profile_command)
    else:
        os.system(performance_profile_command)



if __name__ == "__main__":
    set_power_profile()
    set_charging_threshold()
    