
while True:
    p2 = input('enter a temperature: ')

    try:
        p1 = int(p2)
    except:
        print('error occurred')
        quit()
    if p1 < 20:
        print('cold')
    elif p1 > 37:
        print('hot')
    elif p1 >= 20 or p1 <= 37:
        print('neither hot nor cold')
    else:
        print('an error occurred')
