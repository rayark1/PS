sound = list(map(int, input().split()))

sorted_sound = sorted(sound)
if sound == sorted_sound:
    print('ascending')
elif sound == sorted_sound[::-1]:
    print('descending')
else:
    print('mixed')