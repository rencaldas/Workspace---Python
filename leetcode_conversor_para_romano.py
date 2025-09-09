#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.
import os

def exercicio1():
    class Solution(object):
        def twoSum(self, nums, target):
            mapa = {}

            for i, num in enumerate(nums):
                complemento = target - num
                if complemento in mapa:
                    return [mapa[complemento], i]
                mapa[num] = i

    sol = Solution()
    print(sol.twoSum([3, 3], 6))

def exercicio2():
    def intPraRomano(num: int) -> str:
        valores = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        resultado = ""
        for valor, simbolo in valores:
            while num >= valor:
                resultado += simbolo
                num -= valor
        return resultado
    
    while True:
        entrada = int(input("Insira um número para converter em romano: "))
        print(f"O número {entrada} em romano é: {intPraRomano(entrada)}")

os.system('cls')
escolha = int(input("Qual exercício deseja visualizar? "))
if escolha == 1:
    exercicio1()
elif escolha == 2:
    exercicio2()
