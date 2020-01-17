def count_substring(string, sub_string):
    k = string.count(sub_string)
    return k



if __name__ == '__main__':
    string = input()
    sub_string = input()

    count = count_substring(string, sub_string)
    print(count)
