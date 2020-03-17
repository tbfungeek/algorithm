# https://leetcode-cn.com/problems/climbing-stairs/

def climbing_stairs(n):
    if n < 3:
        return n
    f1 = 1
    f2 = 2
    f3 = 3
    for i in range(3,n + 1):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
    return f3
    

if __name__ == '__main__':
    print(climbing_stairs(4))