def pattern_count(text, pattern):
    if not pattern:
        return 0 #Jika polanya kosong berarti tidak ada pola yang bisa dicari
    
    count = 0
    text_length = len(text)
    pattern_length = len(pattern)

    # lakukan iterasi melalui text untuk mencari kemunculan polanya
    for i in range(text_length - pattern_length + 1):
        if text[i:i + pattern_length] == pattern:
            count += 1

    return count

# tes output
test_case = [
    ("palindrom", "ind"),
    ("abakadabra", "ab"),
    ("hello", ""),
    ("ababab", "aba"),
    ("aaaaaa", "aa"),
    ("hell", "hello")
]

for text, pattern in test_case:
    # tampilkan hasil outputnya
    print(f'pattern_count("{text}","{pattern}") = {pattern_count(text, pattern)}')