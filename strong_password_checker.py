def strongPasswordChecker(self, password: str) -> int:
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    password_copy = password
    
    steps = 0
    
    for i in range(len(password)):
        if i> len(password)-3:
            break
        if password[i] == password[i+1] and password[i+1]==password[i+2]:
            origin = password[i]+password[i+1]+password[i+2]
            new = password[i]+ password[i+1] +password[i+2].swapcase() if password[i+2] in lower_case + upper_case else password[i]+ password[i+1]+str(int(password[i+2])+1)
            password = password.replace(origin,new)
            steps += 1
        continue
    
    if sum([True for d in digits if d in password])<=0:
        steps +=1
    if sum([True for c in lower_case if c in password])<=0:
        steps +=1
    if sum([True for c in upper_case if c in password])<=0:
        steps +=1
    if len(password)<6:
        steps += 6-len(password)-steps
    if len(password)>20:
        steps += len(password) - 20
    
    return steps