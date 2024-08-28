name = ''
password = ''
while name != 'Joe':
    print('Who are you?')
    name = input()
    if name == 'Joe':
        while password != 'swordfish':
            print('Hello, Joe. What is the password? (It is a fish.)')
            password = input()
            if password == 'swordfish':
                print('Access granted.')
                break