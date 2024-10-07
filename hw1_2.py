def reverse_integer(n: int) -> int:
    reversed_n = 0  
    while n > 0:  
        digit = n % 10  
        reversed_n = reversed_n * 10 + digit  
        n //= 10  
    return reversed_n

if __name__ == "__main__":
    
    input_number = int(input("請輸入一個正整數: "))
    
    
    if input_number > 0:
    
        output_number = reverse_integer(input_number)
        print(output_number)
    else:
        print("請確保輸入的是正整數。")
