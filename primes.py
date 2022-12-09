"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes < 0:
        raise ValueError('Negative number of primes does not make any sesne..')
    elif number_of_primes == 0:
        raise ValueError('You requested an empty list!')
    else:
        list = []
        if len(list)==0:
            list.append(2)
        while len(list) < number_of_primes:
            max_num = max(list)
            n = max_num

            next_prime_found = False 
            while not next_prime_found:
                n = n+1
                n_is_prime = True
                for j in range(2,n):
                    if n % j == 0:
                        n_is_prime = False 
                        break 
                if(n_is_prime):
                    list.append(n)
                    next_prime_found = True 
    return list
