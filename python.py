# declaration  Variables
from fractions import Fraction
DNA_Target_length = 50000.0
length_Fragment = 300
frag = 600
allfrag = 4
factorial_One = 300

 # creating factorial for loop
for i in range(1, allfrag):
	factorial_One = factorial_One + length_Fragment

        
FACTORIAL_ANSWER = (factorial_One/DNA_Target_length) 
print(FACTORIAL_ANSWER)

factorial_Two = 300
i = 1
 
while i <= allfrag-1:
	factorial_Two = factorial_Two  + length_Fragment
	i = i + 1

FACTORIAL_ANSWER_NEXT = (factorial_Two /DNA_Target_length)

print(FACTORIAL_ANSWER_NEXT)
