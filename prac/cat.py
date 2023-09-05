'''
i = 0
while i < 3:
    print("Meow")
    i += 1

for _ in range(3): # _ is a variable that is not in use
    print("meow")

print ("meow\n" * 3, end="")
'''

while True: # this deliberately induces a loop that goes on infinite times
    n = int(input ("what's n?"))
    if n > 0:
        break
for _ in range(n):
    print("meow")