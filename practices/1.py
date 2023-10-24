import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

def fun(n, o, c, l: list, s: str):
    if o > n:
        return
    if(o == c and o == n):
        l.append(s)
        return
    
    s += '('
    fun(n, o + 1, c, l, s)
    s = s[:-1]
    if o > c:
        s += ')'
        fun(n, o, c + 1, l, s)


l = list()
fun(3, 0, 0, l, "")
print(l)