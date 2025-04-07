class Solution(object):
    def fib(self, n):
        """
        Calculate the nth Fibonacci number using recursion
        
        Args:
            n: int - The position in the Fibonacci sequence
            
        Returns:
            int - The nth Fibonacci number
        """

        if n == 0:
            return 0
        elif n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)