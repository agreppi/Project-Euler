def isPalindrome(num):
    result = True
    str_num = str(num)
    for i in range(len(str_num) // 2):
        if str_num[i] != str_num[-i-1]:
            result = False
    return result