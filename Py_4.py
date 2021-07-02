altitude = int(input("Hey Pilot Enter Your Current Altitude : "))

if altitude == 1000:
    print("Pilot, you are safe to land. ")
elif altitude <  1000:
    print("Pilot, land the plane. ")
elif altitude>1000 and altitude<5000:
    print("Pilot, bring down to 1000ft.")
elif altitude > 5000 :
    print("Pilot, turn around. ")
else:
    print("Give another input ")