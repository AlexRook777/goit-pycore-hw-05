def caching_fibonacci():
    """
    A function that returns a Fibonacci function with caching capabilities. 
    The returned function computes the Fibonacci number for a given n,
    caching the results to avoid redundant calculations.
    """
    cache = {}

    def fibonacci(n):
        """        Computes the nth Fibonacci number using recursion with caching."""
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            # If the result is already cached, return it
            # and print a message indicating that the value is fetched from cache. 
            print(f"Fetching fib({n}) from cache...")
            return cache[n]
        else:
            # If the result is not cached, compute it recursively,
            # store it in the cache, and print a message indicating that the value is being calculated. 
            result = fibonacci(n - 1) + fibonacci(n - 2)
            cache[n] = result
            print(f"Calculating fib({n}) and storing in cache.")
            return result


    return fibonacci

# Creating an instance of the caching Fibonacci function 
fib_with_cache = caching_fibonacci()

# Testing the caching Fibonacci function with various inputs
print(f"fib(5) = {fib_with_cache(5)}")
print(f"fib(7) = {fib_with_cache(7)}") 
print(f"fib(8) = {fib_with_cache(8)}") 
print(f"fib(10) = {fib_with_cache(10)}") 
print(f"fib(15) = {fib_with_cache(15)}") 