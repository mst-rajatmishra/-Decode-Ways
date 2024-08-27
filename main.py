class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: There's 1 way to decode an empty string
        dp[1] = 1  # Base case: There's 1 way to decode a non-zero single character
        
        for i in range(2, n + 1):
            one_digit = int(s[i-1:i])
            two_digits = int(s[i-2:i])
            
            # Check if the one-digit substring is valid
            if 1 <= one_digit <= 9:
                dp[i] += dp[i-1]
            
            # Check if the two-digit substring is valid
            if 10 <= two_digits <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]

# Example usage:
sol = Solution()
print(sol.numDecodings("12"))   # Output: 2
print(sol.numDecodings("226"))  # Output: 3
print(sol.numDecodings("06"))   # Output: 0
