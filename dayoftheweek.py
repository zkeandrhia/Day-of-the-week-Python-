def schedule():
    print('Enter a number that ranges from(1-7): ')
    
    while True:
        student = int(input('> '))
        if student == 1:
            print("Ugh, it's MONDAY again!")
            ask = input('Choose again? y/n: ')
            if ask != 'y':
                break
            else:
                continue
            
        elif student == 2:
            print("Go on, it's TUESDAY! ")
            ask = input('Choose again? y/n: ')
            if ask != 'y':
                break
            else:
                continue
        elif student == 3:
            print("Wash your clothes, lazy head, it's WENESDAY! ")
            ask = input('Choose again? y/n: ')
            if ask != 'y':
                break
            else:
                continue
        elif student == 4:
            print("Party night is neaarr, it's THURSDAY! ")
            ask = input('Choose again? y/n: ')
            if ask != 'y':
                break
            else:
                continue
        elif student == 5:
            print("CHUG! CHUG! TGIFRIDAY!")
            ask = input('Choose again? y/n: ')
            if ask != 'y':
                break
            else:
                continue
        elif student == 6:
            print("My head hurts, where am I? SATURDAY! ")
            ask = input('Choose again? y/n: ')
            if ask != 'y':
                break
            else:
                continue
        elif student == 7:
            print("Time to go to Church! It's SUNDAY!")
            ask = input('Choose again? y/n: ')
            if ask != 'y':
                break
            else:
                continue
        else:
            print('Invalid Input :) ')  
            ask = input('Choose again? y/n: ')
            if ask != 'y':
                break
            else:
                continue
schedule()
    
        

          
    