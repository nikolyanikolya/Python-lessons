def Fib(n):
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    i = 0
    prev_ = 0
    next_ = 1
    ans = [0, 1]
    while i <= n - 2:
        prev_, next_ = next_, next_ + prev_
        i += 1
        ans.append(next_)
    return ans


#if __name__ == '__main__':
#    print(Fib(10))
