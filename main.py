# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
x = "กรักตนชัย จำเริญบุญ"
dee = list(x)
print(dee)
"""
yout = chr(ord(x) - 1)
print(yout)
print(ord("ั"))
print(chr(3631))
for x in range(3584,4000,1):
    print(x,chr(x))
"""
"""
for x in range(3585,3674,1):
    if dee[0] == chr(x):
        print("ก")
for x in range(3585,3674,1):
    if dee[1] == chr(x):
        print("ข")
"""
if (dee[0] == "ก"):
    dee[0] = "d"
elif (dee[0] == "ข"):
    dee[0] = "-"
elif (dee[0] == "ข"):
    dee[0] = "-"
print(dee)
