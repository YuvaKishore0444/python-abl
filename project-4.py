text = "aaabbcccca"
encoded = ""
i = 0

while i < len(text):
    count = 1

    while i + 1 < len(text) and text[i] == text[i+1]:
        count += 1
        i += 1

    encoded += text[i] + str(count)
    i += 1

orig_len = len(text)
comp_len = len(encoded)

print(f"Original Text: {text} (Length: {orig_len})")
print(f"Compressed Text: {encoded} (Length: {comp_len})")
print(f"Space Reduction: {orig_len - comp_len} characters")