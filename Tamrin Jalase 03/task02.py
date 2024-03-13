# vroudi: 5 nomre tavasote karbar , khorouji: miangin , minimum maximum , variance

score01 = int(input('score number 01 is: '))
score02 = int(input('score number 02 is: '))
score03 = int(input('score number 03 is: '))
score04 = int(input('score number 04 is: '))
score05 = int(input('score number 05 is: '))
# miangin
m = (score01+score02+score03+score04+score05)/5
# variace
v = ((score01-m)**2+(score02-m)**2+(score03-m)**2+(score04-m)**2+(score05-m)**2)/5

print(m)
priny(v)


