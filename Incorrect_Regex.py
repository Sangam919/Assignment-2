import re
n = int(input())
for _ in range(n):
    regex_string = input().strip()
    try:
        re.compile(regex_string)
        print("True")
    except re.error:
        print("False")
        
        

