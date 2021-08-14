import random

b = [['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']]

def a():
    for i in range(3):
        for j in range(3):
            print(b[i][j], end=' ')  
        print() 
    print()
    
def c():   
    while True:
        d = int(input("satr to varied kin:))
        if 0 <= d <= 3:
            pass
        else:
            print("galatea dobare emtahan kon")
            continue 
        e = int(input("soton to varied kon"))
        if 0 <= e <= 3:
            pass
        else:
            print("galatea donate emtahan kon")
            continue
        
        if b[d - 1][e - 1] == '_':     
            b[d - 1][e - 1] = 'X'
            break
        else:
            print("Estebah kardi baraie hash dobare emtahan kon")

def f():
    while True:
        j = random.randint(1, 3)
        h= random.randint(1, 3)
        
        if game[j - 1][h - 1] == '_':
            game[j - 1][h - 1] = 'O'
            break

def k():
    for i in range(3):
        if b[i][0] == 'X' and b[i][1] == 'X' and b[i][2] == 'X':
            return 1
        if b[i][0] == 'O' and b[i][1] == 'O' and b[i][2] == 'O':
            return 2 
        
    for i in range(3):
        if b[0][i] == 'X' and b[1][i] == 'X' and b[2][i] == 'X':
            return 1
        if b[0][i] == 'O' and b[1][i] == 'O' and b[2][i] == 'O':
            return 2 
    
    if b[0][0] == 'X' and b[1][1] == 'X' and b[2][2] == 'X':
        return 1
    if b[0][0] == 'O' and b[1][1] == 'O' and b[2][2] == 'O':
        return 2
        
    return 0
      
flag = 0        
for i in range(9):
    if i % 2 == 0:
        c()
    elif i % 2 != 0:
        b()
    
    a()
    
    m= end_game()
    if m!= 0:
        flag = 1
        print('End Game')
        print m== 1:
            print('Player is Winner :)')
        print m== 2:
            print('Computer is winner :(')
        break

if flag == 0:
    print('End Game')
    print('DRAW :|')
