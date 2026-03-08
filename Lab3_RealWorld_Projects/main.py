
from access_control import audit_log, compute_access_level, validate_access
from media_engine import monitor, signal_shutdown, play_count_stream

# ==========================================
# YOUR SPECIFIC INPUTS
# ==========================================
SEED_NUM = 1  
FAVORITE_ARTIST = "TWICE"
# ==========================================

# Core Variables
CONTROL_NUM = max(1, SEED_NUM)
ARTIST_LEN = len(FAVORITE_ARTIST)

@audit_log
def run_authorization():
    """Executes Ex 1 logic"""
    level = compute_access_level(CONTROL_NUM, ARTIST_LEN)
    threshold = CONTROL_NUM * 5
    decision = validate_access(level, threshold)
    return level, threshold, decision

@monitor
def run_media_stream(limit):
    """Executes Ex 3 logic"""
    # Converting generator to list to see the full results
    plays = list(play_count_stream(limit))
    return plays

# --- EXECUTION FLOW ---

print("--- EXERCISE 1: AUTHORIZATION ---")
acc_level, threshold, final_decision = run_authorization()

print("\n--- EXERCISE 2: RECURSIVE SHUTDOWN ---")
# Wrapping the recursive function with the audit_log decorator
decorated_shutdown = audit_log(signal_shutdown) 
initial_power = CONTROL_NUM + ARTIST_LEN
total_calls = decorated_shutdown(initial_power)

print("\n--- EXERCISE 3: MEDIA ANALYTICS ---")
stream_limit = CONTROL_NUM + ARTIST_LEN
generated_plays = run_media_stream(stream_limit)

# --- FINAL RESULTS SUMMARY ---
print("\n" + "="*40)
print("       OFFICIAL ASSESSMENT DATA       ")
print("="*40)
print(f"Computed Access Level:     {acc_level}")
print(f"Threshold Applied:         {threshold}")
print(f"Final Auth Decision:       {final_decision}")
print("-" * 30)
print(f"Initial Signal Strength:   {initial_power}")
print(f"Total Recursive Calls:     {total_calls}")
print("-" * 30)
print(f"Generated Play Counts:     {generated_plays}")
print(f"Total Plays (Sum):         {sum(generated_plays)}")
print(f"Number of Records:         {len(generated_plays)}")
print("="*40)