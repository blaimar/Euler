import time
start = time.process_time()

# ------------------------------------------------------------------------------------------

last = [1,2]
soluce = 2

while True:
    new_number = sum(last)
    if new_number > 4000000:
        break
    last[0] = last[1]
    last[1] = new_number
    if new_number%2 == 0 :
        soluce += new_number

print(soluce)

# ------------------------------------------------------------------------------------------

end = time.process_time()  - start
print(end)
