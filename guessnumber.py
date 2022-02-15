s=4
guess_n=0
guess_l=3
while guess_n<guess_l:
    guess=int(input('guess: '))
    guess_n += 1
    if guess==s:
        print('you Win!')
        break
else:
    print('you failed!')    