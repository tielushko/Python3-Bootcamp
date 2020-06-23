def current_beat():
    nums = (1,2,3,4)   
    i = 0
    while True:
        if i>=len(nums): i = 0
        yield nums[i]
        i += 1

def kick_play_drum():
    if current_beat() == 1:
        play_sound()

counter = current_beat()

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
