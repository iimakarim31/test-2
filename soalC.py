def hitung_huruf(text):
    letter_count = {}

    #iterasi setiap huruf dalam text
    for char in text:
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1

    # mengurutkan berdasarkan huruf secara abjad, case-sensitive
    sort_huruf = dict(sorted(letter_count.items()))

    return sort_huruf

# tes output
test_case = ["Hello World", "Bismillah", "MasyaAllah"]

for text in test_case:
    # tampilkan hasil outputnya
    print(f'Input: "{text}"\nOutput: {hitung_huruf(text)}\n')