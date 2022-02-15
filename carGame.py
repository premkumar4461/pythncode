from distutils import command


comman=""
started=False
while True:
    comman=input("> ").lower()
    if comman=="start":
        if started:
            print("car is alredy started")
        else:
            started=True
            print("car is started...")
    elif comman=="stop":
        if not started:
            print("car is alredy stopped")
        else:
            started= False
            print("car is stoped")  
    elif comman=="quit":
        break       
    elif comman=="help":
        print("""
start-car is start
stop-car is stop
quit- to quit
        """)
        
    else:
         print("i dont understand what did you say")    
    