
'''
Zach Aubry
zaubry@uwo.ca
251307316
This code is assignment 1 for Cs 1026, it analyzes the Collatz Conjecture for various user inputs of positive integers
'''

## The Collatz Conjecture goes as follows;
    # even if n % 2 = 0
    # odd if n % 2 = 1

    # The conjecture causes all integers to converge to 1, which is where the sequence will end

n = float(input("Enter a number: ")) # User input becomes this value

even = "" # List for even numbers produced
odd = "" # List for odd numbers produced
prime = "" # List for prime numbers produced

total = "" # List for all number produced

max_n = -1 # Will use as starting point when finding the max number produced

even_count = 0 # Will be used to keep track of each new even number the conjecture generates
odd_count = 0 # Will be used to keep track of each new odd number the conjecture generates
n_count = 0 # Will be used to keep track of the total numbers the conjecture generates

total = odd + even # All numbers obtained from the sequence in one list

if n > 1:
    while n >= 1: # Performing the Sequence in the following loop
        n = int(n)

        if (n % 2) == 0: # Checks if the user input is even
            even += f"{n},"
            total += f"{n},"
            even_count += 1
            n_count += 1

            if n == 2:
                prime += f"{n}," # 2 is the only even number that is prime

            if n > max_n: # Used to update the largest number we get in the sequence
                max_n = n

            n = n/2 

        elif ((n % 2) == 1) and (n != 1): # Checks if the user input is odd, and not equal to 1
            odd += f"{n},"
            total += f"{n},"
            odd_count += 1
            n_count += 1

            for i in range(2, n): # Considering all integers between 2 and n-1, and dividing n by each one to see if n is an integer
                if (n % i != 0):
                    continue
                if (n % i == 0): # Means that n canot be a prime number
                    break
            else: # Will execute if no i in [2, n-1] can divide n, which means n is a prime number
                prime += f"{n},"

            if n > max_n: 
                max_n = n

            n = 3*n + 1 

        elif n == 1: # Will execute when the end of the conjecture has been reached
            odd += f"{n},"
            total += f"{n},"
            odd_count += 1
            n_count += 1

            if n > max_n: 
                max_n = n

            ## Outputs corresponding to the user input if n >= 1
            print("\nAll Numbers: ", total)
            print("Prime numbers encountered: ", prime)
            print(f"Maximum number: {max_n}")
            print("Even numbers: ", even_count)
            print("Odd numbers: ", odd_count)
            print(f"Total numbers: {n_count}") 
            exit() 

else:
    print("The value of n must be greater than 1") # Executes if input is not a positive integer
    exit() 









### Extra Code

# for i in range(2, int(n)-1):
        #     #print(f"{i} hi!!")
        #     if n % i == 1:
        #         print(f"{n} is prime")
        
        # for n in range[2, n-1]:
        #     if not(((n % 2) == 0) and ((n % n -1) == 0)):
        #         print(f"{n} is a prime number")
        #         prime.append(n)


# if (n % i != 0):
                #     print(f"{n} % {i}  has an integer remainder not equal to 0")

# print(f"{n} % {i}  has an integer remainder equal to 0")
                    # print(f"{n} is not prime")

