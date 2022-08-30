from playsound import playsound
  
# for playing note.wav file

while True:
    
    A = int(input(""" Enter
              1 for HCD leakage
              2 for ESD
              3 for DYKE VALVE OPENING
              4 for FIRE ACTIVATION ALARM :
         """ ))

    W = A % 10
    X = ( A // 10) % 10
    Y = (A // 100) % 10
    Z = (A // 1000) % 10

    #for alarm

    for a in (Z , Y , X ,W):

        if a == 0 :
            continue
        elif a == 1 :
            print("HCD leakge")
            playsound('C:\\Users\\DELL\\Desktop\\Project hpcl\\hissing sound.mp3')
        elif a == 2 :
            print("ESD")
            playsound('C:\\Users\\DELL\\Desktop\\Project hpcl\\TQ7E6ZX-electricity.mp3')
        elif a == 3 :
            print("DYKE VALVE OPENED")
            playsound('C:\\Users\\DELL\\Desktop\\Project hpcl\\valve_1air-release-67255.mp3')
        else :
            print("FIRE EMERGENCY")
            playsound('C:\\Users\\DELL\\Desktop\\Project hpcl\\campfire-1.mp3')

    # for display
    
    print("\nDisplay\n")
    
    if W == 1 or X == 1 or Y == 1 or Z == 1:
        print("HCD LEAKAGE.")
    if W == 2 or X == 2 or Y == 2 or Z == 2:
        print("ESD.")
    if W == 3 or X == 3 or Y == 3 or Z == 3:
        print("DYKE VALVE OPENED.")
    if W == 4 or X == 4 or Y == 4 or Z == 4:
        print("FIRE EMERGENCY.")

    if W != 0 or X != 0 or Y != 0 or Z != 0 :
        
        #FOR RESET
            
        A1 = int(input(""" Enter updated
                  1 for HCD leakage
                  2 for ESD
                  3 for DYKE VALVE OPENING
                  4 for FIRE ACTIVATION ALARM :
             """ ))
    
        W1 = A1 % 10
        X1 = ( A1 // 10) % 10
        Y1 = (A1 // 100) % 10
        Z1 = (A1 // 1000) % 10
    
        if ( W1 or X1 or Y1 or Z1 != 1 ):
            print("HCD ISSUE RESOLVED.")
            playsound('C:\\Users\\DELL\\Desktop\\Project hpcl\\hissing sound.mp3')
            
        if ( W1 or X1 or Y1 or Z1 != 2 ):
            print("ESD OPENED.")
            playsound('C:\\Users\\DELL\\Desktop\\Project hpcl\\TQ7E6ZX-electricity.mp3')
        if ( W1 or X1 or Y1 or Z1 != 3 ):
            print("DYKW VALVE CLOSED.")
            playsound('C:\\Users\\DELL\\Desktop\\Project hpcl\\valve_1air-release-67255.mp3')
        
        if ( W1 or X1 or Y1 or Z1 != 4 ):
            print("FIRE ISSUE RESOLVED.")
            playsound('C:\\Users\\DELL\\Desktop\\Project hpcl\\campfire-1.mp3')
