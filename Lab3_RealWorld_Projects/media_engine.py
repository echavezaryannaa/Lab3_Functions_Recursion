
def monitor(func):
    """Decorator to log processing status."""
    def wrapper(*args, **kwargs):
        print("Processing Started")
        result = func(*args, **kwargs)
        print("Processing Completed")
        return result
    return wrapper

def signal_shutdown(power, count=0):
    """Recursive function to simulate signal shutdown."""
    # Base Case: Stop when power reaches 0
    if power <= 0:
        return count
    
    # Recursive Step: Reduce power and increment call count
    print(f"Current signal strength: {power}")
    return signal_shutdown(power - 1, count + 1)

def play_count_stream(limit):
    """Generator yielding squared even numbers up to the limit."""
    for i in range(limit):
        if i % 2 == 0:
            yield i ** 2