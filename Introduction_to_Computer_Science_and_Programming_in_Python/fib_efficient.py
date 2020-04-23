#Memoization 
dict_ = {0: 0, 1: 1}

def fib_efficient(n, dict_):
    if n in dict_:
        return dict_[n]

    else:
        ans = fib_efficient(n-1, dict_) + fib_efficient(n-2, dict_)
        dict_[n] = ans 
        return ans

if __name__ == '__main__':
    dict_ = {0: 0, 1: 1}
    print(fib_efficient(34, dict_))