import random

def prime_test(N, k):
	# This is main function, that is connected to the Test button. No need to modify.
	return fermat(N,k), miller_rabin(N,k)

# Method implements exponentiation.
def mod_exp(x, y, N): # x^y (mod N)    Time Complexity: O(n^3)   n = stack frame 
    if (y == 0) : 
        return 1
    z = mod_exp(x, y//2, N)# y//2 = math.floor (y/2) O(n)
    if (y % 2 == 0) :
        return (z**2) % N 
    else :
        return (x * (z**2)) % N  # O(n^2) for multiplication and ??? for Exponential
	

# Method computes Fermat primality test pseudocode.
def fermat(N,k): # primality    Time Complexity: O(n^3)  ??? n^4
    for _ in range(k): # O(n) = n  ??? K
        a = random.randint(2, N-1) # O(1)
        if (mod_exp(a, N-1, N) != 1): # a^(N-1) != 1 (mod N)   O(n^3)
            # if mod_exp return a value other than 1 we know that the number is composite.
            return "composite"
    # after running all k random number and all of them were 1 mod (N) then number might be prime  
    # if mod_exp returns 1 there is the probability that the number is prime.
    return "prime" # a^(N-1) = 1 (mod N)


# Method computes the probability that k Fermat trials gave the correct answer.
def fprobability(k): # (1/2^k) is the probability that the Fermat trials are wrong.
    return 1 - (1/2**k) # Then, 1 - (1/2^k) gives probability of k Fermat trials being right.


# Method implements the Miller-Rabin primality test.
def miller_rabin(N,k):
    for _ in range(k):
        a = random.randint(2, N-1)
        x = mod_exp(a, N-1, N) # a^(N-1)(mod N)   O(n^3 * n)
        if (x != 1) : return "composite"
        m = 1
        y = (N - 1)
        while(m == 1) :
            y = y//2 #floor
            m = mod_exp(a, y, N)
            if (m != 1) : 
                if (m == N - 1) : break # -1 (mod N) = N-1 (mod N). If we get here it means a passed so we break to try another random a.
                else : return "composite"
            if (y % 2 == 1) : break
    return "prime"

# Method computes the probability that k Miller-Rabin trials gives the correct answer.
def mprobability(k): # (1/4)^k is the probability that Miller-Rabin trial are wrong.
    return 1 - ((1/4)**k) # This gives probability of k Miller-Rabin trials is correct.