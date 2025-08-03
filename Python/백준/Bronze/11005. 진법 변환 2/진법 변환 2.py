n, r = map(int, input().split())
digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def to_base(n, r):
    result = ""
    while n > 0:
        n, remainder = divmod(n, r)
        result=digits[remainder]+result
    return result or "0"
print(to_base(n,r))