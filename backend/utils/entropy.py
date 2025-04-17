import math
from collections import Counter

def calculate_entropy(text):
    if not text:
        return 0.0
    counter = Counter(text)
    total_chars = len(text)
    entropy = -sum((count / total_chars) * math.log2(count / total_chars) for count in counter.values())
    return entropy
