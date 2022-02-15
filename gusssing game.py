secret_number=8
guess_number=0
guess_limmit=3
while guess_number<guess_limmit:
   guess=int (input('Guess:'))
   guess_number +=1
   if guess== secret_number:
       print('you win!')
       break
else:
    print("you failed!")

