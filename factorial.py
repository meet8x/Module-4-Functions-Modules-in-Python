
def facto():
    val = int(input("Eneter a Number:"))
    if val < 2:
        return 1
    else:
        ans = 1
        while (val>=1):
           ans =ans*val
           val = val - 1
    return("Factorial of",val, "is:",ans)
ans1 = facto()
print(ans1)

