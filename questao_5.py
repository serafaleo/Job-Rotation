# -*- coding: utf-8 -*-

def invert_string(string):
    new_string = ""
    for i in range(len(string)-1, -1, -1):
        new_string += string[i]
    return new_string

def main():
    string = input("Digite uma string para ser invertida: ")
    print(f"A string invertida fica da seguinte forma: {invert_string(string)}")

if __name__ == "__main__":
    main()
