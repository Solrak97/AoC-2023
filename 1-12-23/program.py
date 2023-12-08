input_path = './input'
digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8", 
    "nine": "9"
}

numbers = []
with open(input_path) as f:
    for line in f:
        numeric = ""
        for i, c in enumerate(line):
            if c.isdigit():
                numeric += (c)
                continue
                
            for key in digits.keys():
                if line[i:].startswith(key):
                    numeric += digits[key]
        numbers.append(int(numeric[0] + numeric[-1]))


print(sum(numbers))