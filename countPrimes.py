class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        # Assume all numbers are prime
        isPrime = [True] * n

        # remove 0 and 1 which are by definition not prime
        isPrime[0] = isPrime[1] = False

        # Start from 2 till sqrt(n)
        for i in range(2, int(n ** 0.5) + 1):
            # if current number is prime then mark all its multiples not prime
            if isPrime[i]:

                # Mark multiples
                for j in range(i * i, n, i):
                    isPrime[j] = False
        # Finally we have all primes marked as True just sum as True becomes value 1 
        return sum(isPrime)