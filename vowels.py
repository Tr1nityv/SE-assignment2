word = "collaboration"
vowels = "aeiou"
count = sum(1 for letter in word if letter.lower() in vowels)
print(f"There are {count} vowels in the word '{word}'.")
