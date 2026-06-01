class Solution:
    def completePrime(self, num: int) -> bool:
        sol = {2,3,5,7,23,37,53,73,313,317,373,797,3137,3797,739397}
        return num in sol