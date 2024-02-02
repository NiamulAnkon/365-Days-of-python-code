import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile']).decode('utf-8', errors='backslashreplace').split("\n")
profiles = [i.split(":")[1][1:-1] for i in data if "All user profile" in i]

for profile in profiles:
    try:
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8', errors='backslashreplace').split("\n")
        ssid = profile
        password_line = [line.split(":")[1][1:] for line in result if "Key Content" in line]
        password = password_line[0].strip() if password_line else "No Password Set"
        print("{:<30}| {:<}".format(ssid, password))
    except subprocess.CalledProcessError:
        print("{:<30}| {:<}".format(profile, "Encoding Error"))

input("Press Enter to exit")
