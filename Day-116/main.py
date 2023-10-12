from win10toast import ToastNotifier
import time

if __name__ == "__main__":
    toaster = ToastNotifier()
    while True:
        toaster.show_toast("*** TAKE REST ***", "You need to rest; you're working too much", duration=5)
        time.sleep(60*60)
