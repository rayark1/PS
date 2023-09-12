def kmp_table(pattern):
    result = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = result[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            result[i] = j
    return result

def kmp_search(text, pattern):
    table = kmp_table(pattern)
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = table[j - 1]
        if text[i] == pattern[j]:
            if j == len(pattern) - 1:
                return True
            else:
                j += 1
    return False

S = input()
P = input()

print(1 if kmp_search(S, P) else 0)
