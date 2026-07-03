def is_prime(n):
    """Checks if a number is prime."""
    if n < 2:
        return False
    # Only need to check divisors up to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_twin_primes(limit):
    """
    Finds all twin prime pairs up to a given limit.
    A twin prime is a pair of prime numbers that differ by 2.
    """
    twin_primes = []
    # Start checking from 3, as 2 is not part of a twin prime pair (3-2=1, not prime)
    # We only need to check odd numbers for primality after 2
    for i in range(3, limit - 1, 2):
        if is_prime(i) and is_prime(i + 2):
            twin_primes.append((i, i + 2))
    return twin_primes

def main():
    search_limit = 10000 # Define the upper limit for searching twin primes

    print(f"Searching for twin primes up to {search_limit}...\n")

    # --- Core concept: Finding twin primes ---
    # This part generates the raw data that an AI research engine would analyze
    all_twin_primes = find_twin_primes(search_limit)

    print(f"Found {len(all_twin_primes)} twin prime pairs up to {search_limit}.")
    print("First 10 twin prime pairs found:")
    for i, pair in enumerate(all_twin_primes[:10]):
        print(f"  {i+1}. {pair}")
    print("...\n")

    # --- Core concept: Demonstrating distribution (hinting at a 'law') ---
    # An AI would analyze the distribution of these numbers to find patterns.
    # Here, we show cumulative counts at different milestones to illustrate growth.
    print("Cumulative count of twin primes at various milestones:")
    milestones = [100, 1000, 5000, search_limit]
    current_count = 0
    prime_index = 0

    for milestone in sorted(milestones):
        if milestone > search_limit:
            break
        
        while prime_index < len(all_twin_primes) and all_twin_primes[prime_index][1] <= milestone:
            current_count += 1
            prime_index += 1
        print(f"  Up to {milestone}: {current_count} twin prime pairs")

    print("\nThis cumulative count illustrates how the frequency of twin primes changes as numbers get larger, providing raw data for discovering distribution laws.")

if __name__ == "__main__":
    main()
