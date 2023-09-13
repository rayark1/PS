def check_quality(password):
    vowels = "aeiou"
    
    # 조건 1: 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
    if not any(v in password for v in vowels):
        return False
    
    # 조건 2: 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
    vowel_count = 0
    consonant_count = 0
    for char in password:
        if char in vowels:
            vowel_count += 1
            consonant_count = 0
        else:
            consonant_count += 1
            vowel_count = 0

        if vowel_count == 3 or consonant_count == 3:
            return False

    # 조건 3: 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
    for i in range(len(password)-1):
        if password[i] == password[i+1] and password[i] not in ["e", "o"]:
            return False

    return True

while True:
    string = input()
    if string == 'end':
        break
    if check_quality(string):
        print(f"<{string}> is acceptable.")
    else:
        print(f"<{string}> is not acceptable.")