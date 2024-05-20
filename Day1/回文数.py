def isPalindrome(num):
    if num < 0 or (num % 10 == 0 and num != 0):
        return False
    
    reversed_half = 0
    
    while num > reversed_half:
        pop = num % 10
        num //= 10
        
        reversed_half = reversed_half*10 + pop
        
    return num == reversed_half or num == reversed_half // 10
    

print(isPalindrome(12121))