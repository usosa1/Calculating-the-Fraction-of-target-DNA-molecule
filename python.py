# declaration  Variables
from fractions import Fraction
DNA_Target_length = 50000.0
length_Fragment = 300
frag = 600
allfrag = 4
fact_One = 300

 # METHOD 1: Calc using for loop
for i in range(1, allfrag):
	fact_One = fact_One + length_Fragment

        
FACT_ANSWER = (fact_One/DNA_Target_length) 
print("Fraction: ",  Fraction(FACTORIAL_ANSWER))
print("Percent: ", FACTORIAL_ANSWER  * 100,"%")


# Method 2: Calc using while loop
fact_Two = 300
i = 1
 
while i <= allfrag-1:
	fact_Two = fact_Two  + length_Fragment
	i = i + 1
FACT_ANSWER_NEXT = (fact_Two /DNA_Target_length)

print("Fraction: ",Fraction( FACT_ANSWER_NEXT))
print("Percent: ", FACT_ANSWER_NEXT * 100,"%")
