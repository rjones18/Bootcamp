angry = True
bored = True
hungry = False
tired = False

if angry and hungry and bored:
  print('T-Rex is eating the Triceratops!')

elif tired and hungry:
    print("T-Rex is eating the Iguanadon!")

elif tired:
    print("The T-Rex is sleep.")

elif angry and bored:
    print("The T-Rex is fighting the Velociraptor!")

elif angry or bored:
    print("The T-Rex roars!!!!")

else:
    print("The T-Rex smiled!")
