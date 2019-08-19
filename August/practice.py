x = int(input())
for tc in range(1, x+1):
    chars = input()
    a = []
    for char in chars:
        if char =='{':
            a.append(char)
        elif char =='(':
            a.append(char)            
            
        elif char =='}' :
            if len(a) == 0:
                result = 0
                break
            elif len(a) != 0 and a[-1]=='{':
                a.pop()
            else:
                result = 0
        elif char ==')':
            if len(a) == 0:
                result = 0
                break
            elif len(a) != 0  and a[-1]=='(':
                a.pop()
            else:
                result = 0    
                
        if len(a) == 0:
                result = 1
        else:
                result = 0
        
    print(f'#{tc} {result}')

