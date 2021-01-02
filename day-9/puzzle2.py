from puzzle1 import read_file
from puzzle1 import main as find_invalid_number

def find_numbers(file_name):

    invalid_number = find_invalid_number(file_name)
    content = read_file(file_name)

    for i in range(len(content)):
        _sum = content[i]
        numbers = [content[i]]
        for j in range(i+1, len(content), 1):
            k = content[j]
            _sum += k
            numbers.append(k)
            if _sum == invalid_number and len(numbers) >= 2:
                return numbers
            if _sum > invalid_number:
                break
    return []
    
if __name__ == "__main__":
    file_name = "input-9.txt"
    numbers = find_numbers(file_name)
    print(min(numbers) + max(numbers))
