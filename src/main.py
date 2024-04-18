bat_charge_start_threshold = open("/sys/class/power_supply/BAT0/charge_control_start_threshold", "w")
bat_charge_start_threshold.write("75")

bat_charge_end_threshold = open("/sys/class/power_supply/BAT0/charge_control_end_threshold", "w")
bat_charge_end_threshold.write("85")


