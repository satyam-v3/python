n=int(input("\033[33mEnter the number to check if the no is multiple of both 5 and 7 \n\033[0m"))
if n%5==0 and n%7==0:
    print("\33[32m", "Multiple of both 5 & 7", "\033[0m")
else :
    print("\033[31m", "Not multiple of 5" , "\033[0m")