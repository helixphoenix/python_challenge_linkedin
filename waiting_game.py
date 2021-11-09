
import time
import keyboard


def waiting_game():
    print("The target time is 7 seconds")
    input("----Press ENTER to start the timer----")
    if keyboard.read_key() ==  "enter":
        print("Game started")
        t0=time.time()
            
    input("----Press ENTER to end the timer----")
    if keyboard.read_key() ==  "enter":
        print("Game over")
        t1=time.time()
    if 5<= int(t1-t0)<= 7:
        return print("Congrats")
    elif int(t1-t0)<5:
        return print(f"You are too quick")
    elif int(t1-t0)>7:
        return print(f"You are too slow")

        
      

            
            
        
waiting_game()