from puzzle1 import read_file

def main(file_name):
    content = read_file(file_name)
    content.append(0)
    content.append(max(content) + 3)
    content_set = set(content)

    paths = [0] * (max(content_set)+1)
    paths[0] = 1

    for i in range(1, max(content_set) + 1):
        for j in range(1,4,1):
            if i - j in content_set:
                paths[i] += paths[i - j]
    
    print(str(paths[-1]))

if __name__ == "__main__":
    file_name = "input-10.txt"
    main(file_name)