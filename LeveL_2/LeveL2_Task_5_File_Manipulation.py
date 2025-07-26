
#File Manipulation
with open('LeveL_2\Task_five.txt','r')as f:
    lines = f.readlines()
    d={}
    for i in lines:
        words = i.split()
        for word in words:
            word = word.lower().strip('.,!?;:"\'()[]{}')
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
    for word in sorted(d):
        print(f"{word}: {d[word]}", end=' ')

