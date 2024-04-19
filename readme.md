### This script will set the charging threshold for your laptop and set the power profile on startup.
It will set the power profile to either performance or battery, depending on whether your laptop is on AC or not. It will also set the charging threshold, but that will only work if your laptop supports it.

#### Making the script run automatically
To automate running this script create a config file at:

```bash
touch /etc/systemd/system/battery.service
```

in the file, paste the following content:

```
[Unit]
Description=Battery threshold script

[Service]
Type=oneshot
ExecStart=/usr/bin/python3 /path_to_script/script_name.py

[Install]
WantedBy=multi-user.target
```

replace `/path_to_script/script_name.py` with the path to your script and its name.

To make the script run every time a user logs in, run this:

```bash
sudo systemctl enable battery.service
```


### Setting a new threshold value
To change the threshold, edit the values of:

```python
bat_charge_end_threshold.write("85")
```
