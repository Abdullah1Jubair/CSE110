#while loop 
count = 1 
while count <= 5:
    print("Happy Birthday")
    count = count + 1 
#if we use 0 in count condition will be "<"    
#if we use 1 in count condition will be "<="


# a) 24, 18, 12, 6, 0, -6 

count = 24
while count >= -6:
    print(count)
    count = count - 6 

# b) -10, -5, 0, 5, 10, 15, 20
# end ="" is known as empty str . It is used for last word or number 
# end =" " in the space if we place a symbol it will use is in the whole sentence 
count = -10
while count <= 20:
    if count == 20:
        print(count,end="")
    else:
        print(count, end=", ")    
    count = count+5 


# FOR LOOP 

for number in range(5):
    print("Happy Birthday")
    
# for loop range 
# range(5) = starting value 0 , end value 5 
# range(1,5)= starting value 1, end value 5 
# range(1,5,2)= starting value 1, end value 5, increment = 2


# c) 18, 37, 36, 45, 54, 63
for number in range (18,64,9):
    if number ==63:
        print(number,end="")
    else:
        print(number,end=", ")    
        
