import os, sys, random, re
from random import randrange, getrandbits

def pow_x(g_base,a,p_mod):
  x=1
  bits = "{0:b}".format(a)
  for i, bit in enumerate(bits):
    if bit=='1':
        x = (((x**2)*g_base)%p_mod)
    elif bit=='0':
        x = ((x**2)%p_mod)
  return x%p_mod

def check_prime(n, k=128):

    # First need to test if n is even.
    # 2 is a safe prime that can be used.
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # To find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow_x(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow_x(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as my_file1:
        content = my_file1.readlines()
        pattern = re.findall('\d+', content[0])
        gb = int(pattern[0])

    with open(sys.argv[2], 'r') as my_file2:
        secret = my_file2.readlines()
        z = secret[0].split(',')[2]
        pattern = re.findall('\d+', z)
        a = int(pattern[0])

        #Prime P
        x = secret[0].split(',')[0]
        pattern = re.findall('\d+', x)
        big_primep = int(pattern[0])

        gab = pow_x(gb, a, big_primep)
        print(gab)
