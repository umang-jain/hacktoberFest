import time

print("\nFizzBuzz\n")
x=input("Enter a number - ")

while True:
    try:
        x=int(x)
        break
    except:
        x=input("Please enter a valid int\nEnter a number - ")

start_time = time.time()
for i in range(1,x+1):
    out=""
    if i%3 == 0: out += "Fizz"
    if i%5 == 0: out += "Buzz"
    print(out if len(out)>0 else i)

print("Program took", time.time() - start_time, "to run")
