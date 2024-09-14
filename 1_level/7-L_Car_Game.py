command = ''
started=False
while command != 'quit':
    command=input('>')

    if command == "start" :
        if started:
            print('Car already started ')
        else :
            started = True
            print(" Car started ")

    elif command == "stop":
        if not started:
            print('car already stopped ')
        else:
            started=False
            print(" Car stopped ")
    elif command == 'help':
        print("""
         start - to start a car
         stop - to stop a car 
         quit - to quit  
                  """
              )
        
    else:
        quit()


