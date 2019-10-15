from collections import Counter

animals = ["cat", "dog", "cat", "bird", "horse", "tiger", "horse", "cat"]
animals_counter = Counter(animals)
print(animals_counter)
print(animals_counter.most_common(2))