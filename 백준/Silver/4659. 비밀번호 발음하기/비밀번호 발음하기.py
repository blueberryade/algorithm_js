while True:
    password = input()
    if password == 'end':
        break
    
    vowel = ['a','e','i','o','u']
    x,y = 0,0
    vowel_cnt = 0
    for p in password:
        if p in vowel:    
            vowel_cnt+=1
        
    if vowel_cnt < 1:
        print(f'<{password}> is not acceptable.')
        continue
    
    for i in range(len(password)-2):
        if password[i] in vowel and password[i+1] in vowel and password[i+2] in vowel:
            x = 1
        elif (password[i] not in vowel) and (password[i+1] not in vowel) and (password[i+2] not in vowel):
            x = 1
    
    if x == 1:
        print(f'<{password}> is not acceptable.')
        continue

    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            if password[i] == 'e' or password[i] == 'o':
                continue
            else:
                y = 1
    if y == 1:
        print(f'<{password}> is not acceptable.')
        continue
        
    print(f'<{password}> is acceptable.')

   