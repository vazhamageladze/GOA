string = [
    "apple,banana,grape",
    "one-two-three",
    "hello world",
    "a;b;c;d",
    "2024/07/30",
    "name:John|age:30",
    "split@this@string",
    "comma,separated,values",
    "pipe|separated|values",
    "text-with-dashes"
]

delimiters = [',', '-', ' ', ';', '/', ':', '|', '@']

for s in string :
    print(f"Original string: {s}") 
    for delimiter in delimiters:
        if delimiter in s :
            split_result = s.split(delimiter)
            print(f"Split by '{delimiter}': {split_result}")
print()
