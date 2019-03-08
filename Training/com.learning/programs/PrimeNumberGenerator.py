__author__ = 'aganiger'


lower=900
upper=1000

for i in range(lower,upper):
    counter=0
    for j in range(2,i):
        if (i%j) == 0:
            counter=1
            break
    if counter == 0:
        print(i, "is a prime number")

