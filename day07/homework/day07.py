def get_numbers():
    numbers = []
    for i in range(5):
        number = int(input(f"შემოიტანეთ რიცხვი {i + 1}: "))
        numbers.append(number)
    return numbers


def perform_operations(numbers):

    sum_result = sum(numbers)  
    prod_result = 1
    for num in numbers:
        prod_result *= num  

  
    floor_div_result = numbers[0] // numbers[1] 
    mod_result = numbers[0] % numbers[1] 


    print(f"რიცხვების ჯამი: {sum_result}")
    print(f"რიცხვების ნამრავლი: {prod_result}")
    print(f"{numbers[0]} // {numbers[1]} = {floor_div_result}")
    print(f"{numbers[0]} % {numbers[1]} = {mod_result}")

def main():
    numbers = get_numbers() 
    perform_operations(numbers)  

if __name__ == "__main__":
    main()

num  = 10
str_num = str(num)
print("10" + "20")

num = 21
str_num = str(num)
print("10" + "20")

num = 22
str_num = str(num)
print("22" + "20")

num = 8
str_num = str(num)
print("8" + "20")

num = 14
str_num = str(num)
print("14" + "20")
















