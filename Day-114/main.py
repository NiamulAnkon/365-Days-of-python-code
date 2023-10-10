import datetime
import time

end_time = datetime.datetime(2023,10,11)
site_block = ["www.ucc.com.bd/geforce-rtx-30-series", "https://computerimporter.com/product/gigabyte-geforce-rtx-3060-ti-oc-8gb-gpu-price-in-bd/"]
host_path = "C:/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"

while True:
    if datetime.datetime.now()< end_time:
        print("Blocking started")
        with open(host_path, "r+") as host_file:
            contetn = host_file.read()
            for web in site_block:
                if web not in contetn:
                    host_file.write(redirect + " " + web+"\n")

                else:
                    pass
    else:
        with open(host_path, "r+") as host_file:
            contetn = host_file.readlines()
            host_file.seek(0)
            for line in contetn:
                if not any(web in line for web in site_block):
                    host_file.write(line)

            host_file.truncate()
            
        time.sleep(5)