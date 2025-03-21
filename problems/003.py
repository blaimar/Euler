import time
start = time.process_time()

# ------------------------------------------------------------------------------------------

def isprime(nb):
    if nb < 2:
        return False
    for i in range (2,nb):
        if nb%i == 0 :
            return False
    return True

def largest_prime_factor(number_to_test):
    soluce = 0
    for i in range(2,number_to_test):
        if isprime(i):
            while True : 
                if number_to_test%i == 0:
                    number_to_test //= i
                    if i > soluce:
                        soluce = i
                else:
                    break
        if number_to_test == 1:
            break
    return soluce
        

print(largest_prime_factor(600851475143))

# ------------------------------------------------------------------------------------------

end = time.process_time()  - start
print(end)
