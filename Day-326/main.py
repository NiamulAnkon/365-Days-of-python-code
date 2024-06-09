def find_sens(edpi, dpi):
    sens = edpi / dpi
    print(f"Your valorant sensitivity is: {sens}")

edpi = 280
dpi = int(input("Enter your dpi: "))
if dpi:
    find_sens(edpi, dpi)
else:
    print("Something went wrong")