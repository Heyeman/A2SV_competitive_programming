def count_substring(string, sub_string):
    counter = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i] == sub_string[0]:
            j = 1
            while j < len(sub_string):
                if string[i+j] != sub_string[j]:
                    break
                else:
                    j += 1
                    if j == len(sub_string) -1:
                        counter += 1
    
                 
                
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
