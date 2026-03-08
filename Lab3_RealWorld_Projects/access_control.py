
def audit_log(func):
    """Decorator to log authorization status."""
    def wrapper(*args, **kwargs):
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        return result
    return wrapper

def compute_access_level(control, artist_len):
    """Calculates access level: (CONTROL_NUM * 3) + ARTIST_LEN"""
    return (control * 3) + artist_len

def validate_access(level, threshold):
    """Compares access level against threshold."""
    if level >= threshold:
        return "ACCESS GRANTED"
    else:
        return "ACCESS DENIED"