import os 

def decode(message_file):

    if not os.path.exists(message_file):
      return "File not found."

    print('get the file')
    number_to_word = {}

    with open(message_file, 'r') as file:
        for line in file:
            parts = line.strip().split(' ', 1)
            if len(parts) < 2:
                continue  # in case there are lines that don't fit the expected format
            number = int(parts[0])
            word = parts[1]
            number_to_word[number] = word

    print("Dictionary:", number_to_word)
    key_numbers = []
    current_sum = 0
    current_add = 1
    while current_sum + current_add in number_to_word:
        current_sum += current_add
        key_numbers.append(current_sum)
        current_add += 1

    print("Key numbers:", key_numbers) 
    message = ' '.join(number_to_word[num] for num in key_numbers if num in number_to_word)
    print("Decoded message:", message)
    return message

print("Calling decode function...")
print(decode("/Users/junyuyao/Library/Mobile Documents/com~apple~CloudDocs/1.NYU/2023 Spring/CS9053 Java/Final Project/Tandon-Spring-2024-LeetCode-Bootcamp/Week5/coding_qual_input.txt"))