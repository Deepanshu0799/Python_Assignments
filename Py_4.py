altitude = int(input("Hey Pilot Enter Your Current Altitude : "))

if altitude == 1000:
    print("Pilot, you are safe to land. ")
elif altitude <  1000:
    print("Pilot, land the plane. ")
elif altitude>1000 and altitude<5000:
    print("Pilot, bring down to 1000ft. ")
elif altitude > 5000 :
    print("Pilot, turn around. ")
else:
    print("Give another input ")


#OUTPUT
#Hey Pilot Enter Your Current Altitude : 1000
#Pilot, you are safe to land. 
#Hey Pilot Enter Your Current Altitude : 4500
#Pilot, bring down to 1000ft. 
#Hey Pilot Enter Your Current Altitude : 6500
#Pilot, turn around. 