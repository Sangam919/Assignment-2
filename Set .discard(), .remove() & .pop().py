n = int(input())
s = set(map(int, input().split()))
m = int(input())

for _ in range(m):
    command = input().split()
    op = command[0]
    if op == "pop":
        if s:
            s.remove(min(s))
    elif op == "remove":
        x = int(command[1])
        try:
            s.remove(x)
        except KeyError:
            pass
    elif op == "discard":
        x = int(command[1])
        s.discard(x)

print(sum(s))
