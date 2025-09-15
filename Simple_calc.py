import math as m 

def normal_calc(num1 , num2 , options): 
          fdivision = num1 // num2  
          division = num1 / num2 
          product = num1 * num2 
          remainder = num1 % num2 # will give error if num2 is 0 so i will handle in in if condition
          addition = num1 + num2 
          subtraction = num1 - num2  #These are all the normal functions in a simple calc 
          # Time to handle the options 
          if options == '1':
                  return f" The floor division of {num1} and {num2} is {fdivision}" 
          elif options == '2':
                  return f"The Quotient of {num1} and {num2} is {division}"
          elif options == '3':
                  return f" The product of {num1} and {num2} is {product}"
          elif options == '4':
                  if num2 > 0 and num1 > 0:
                          return f"The remainder of {num1} and {num2} is {remainder}" 
                  else:
                          return "Modulo division by 0"
          elif options == '5':
                  return f"Sum of  {num1} and {num2} is {addition}" 
          elif options == '6':
                  return f"Difference of {num1} and {num2} is {subtraction}" 
#Now lets continue making the scientific parts 

def scientific(num1 , num2 , options):
        ceil1 = m.ceil(num1) #rounding off number 1 
        ceil2 = m.ceil(num2) #rounding off number 2 
        factorial = m.factorial(num1 + num2) #this will take factorial of sum of both numbers.
        square = num1**2 #this will take square of number 1 
        square2 = num2**2 #this will take square of number 2 
        sqrt1 = m.sqrt(num1) 
        sqrt2 = m.sqrt(num2) #square root of num1 and num 2 
        cbrt1 = m.cbrt(num1)
        cbrt2 = m.cbrt(num2) #Cube root of num 1 and num 2 
        #Soon I will make the options part. Please wait 2 minutes I am coming
        #Ok I came back!! 
        #So any ideas what should I make in scientific section. Plz tell in the chat 
        log = m.log(num1 + num2)
        log2 = m.log2(num1 + num2) 
        log3 = m.log10(num1 + num2) 
        log4 = m.log1p(num1 + num2) 
        # All logs in python 
        sin = m.sin(num1 + num2)
        cos = m.cos(num1 + num2)
        #sin and cos of sum of num 1 and num 2  right now 
        absolute = abs(num1) 
        absolute2 = abs(num2) 
        #Absolute values abouve 
        cube = num1 ** 3 
        cube2 = num2 ** 3 
        #Cubes 
        negation = -abs(num1)
        negation2 = -abs(num2) 
        #Negation
        base_10 = 10 ** num1 
        base_10_2 = 10 ** num2 
        #base is 10 and exponent is our numbers above 
        pi = m.pi 
        # the value of pi
        e = m.e 
        #the value of e 
        j_operation = (num1 * 1j + num2) 
        #j_operation 
        #now for the tanget 
        tanget = m.tan(num1 + num2) 
        #tanget in a form of radians 
        # so now for random roots 
        roots = num1** (1 / num2) 
        #ok so i think that is it for the scientific part. lets now do the options condition
        if options == '7':
                return f" {num1} rounded is {ceil1}" 
        elif options == '7':
                return f"{num2} rounded is equal to {ceil2}" 
        elif options == '8':
                return f" the factorial of {num1 + num2} is {factorial}" 
        elif options == '9':
                return f"square of {num1} is {square}" 
        elif options == '9':
                return f"square of {num2} is {square2}"
        elif options == '10':
                return f"square root of {num1} is {sqrt1}"
        elif options == '10':
                return f"square root of {num2} is {sqrt2}" 
        elif options == "11":
                return f"The cube root of {num1} is {cbrt1}" 
        elif options == '11':
                return f"The cube root of {num2} is {cbrt2}" 
        elif options == '12':
                return f"The log of {num1 + num2} is {log}" 
        elif options == '13':
                return f"The log2 of {num1+num2} is {log2}" 
        elif options == '14':
                return f"The log10 of {num1 + num2} is {log3}"
        elif options == '15':
                return f"The log1p of {num1 + num2} is {log4}" 
        elif options == '16':
                return f"The sin of {num1 + num2} is {sin}" 
        elif options == '17':
                return f"The cos of {num1 + num2} is {cos}" 
        elif options == '18':
                return f"The absolute value of {num1} is {absolute}" 
        elif options == "18":
                return f"The absolute value of {num2} is {absolute2}"
        elif options == '19':
                return f"The cube of {num1} is {cube}"
        elif options == '19':
                return f"The cube of {num2} is {cube2}"
        elif options == '20':
                return f"The negation of {num1} is {negation}"
        elif options == '20':
                return f"The negation of {num2} is {negation2}"
        elif options == '21':
                return f"The base 10 of {num1} is {base_10}"
        elif options == '21':
                return f"The base 10 of {num2} is {base_10_2}"
        elif options == "21":
                return f"The value of pi is {pi}" 
        elif options == '22':
                return f"The value of e is {e}" 
        elif options == '23':
                return f"The value of j operation is {j_operation}"
        elif options == '24':
                return f"The tanget of  {num1 + num2} is {tanget}"
        elif options == '25':
                return f"The random roots (like square root) are {roots}" 
        else:
                return "Invalid Options"
#so till now we made normal calculator functions and scientific functions now for the additional 
#functions 

def additional_funcs(num1 , num2 , options):
        XOR = num1 ^ num2 
        AND = num1 & num2 
        OR = num1 | num2 
        #Bitwise operators XOR , AND , OR. 
        #now lets think about the new functions i will add to my calculator
        lcm = m.lcm(num1 , num2)
        gcd = m.gcd(num1 , num2)
        if options == "26":
                return f"XOR of {num1} and {num2} is {XOR}"
        elif options == "27":
                return f"AND of {num1} and {num2} is {AND}"
        elif options == "28":
                return f"OR of {num1} and {num2} is {OR}"
        elif options == "29":
                return f"LCM of {num1} and {num2} is {lcm}"
        elif options == "30":
                return f"GCD of {num1} and {num2} is {gcd}"
# additional functions done time for prime checking 

def is_prime(num1 , num2 , options):
        Sum = num1 + num2 
        factors = [ ]
        for i in range(1 , Sum + 1):
                if Sum%i == 0:
                        factors.append(i)
        if options == '31':
                if len(factors) == 2:
                        return f"{Sum} is Prime"
                elif len(factors) > 2 or len(factors) < 0:
                        return f"{Sum} is Composite"
                elif len(factors) == 0 or len(factors) == 1:
                        return f"{Sum} is Neither Prime nor Composite"


def fibonacci_seq(num1 , num2 , options):
        if options == "32":
                n = num1 + num2
                a,b = 0,1 
                print(a,b , end= " ")
                for i in range(n-2):
                        c = a+b 
                        print(c , end= " ")
                        a,b = b,c 
#fiboacci sequence created 
def sequence_of_mth_integer(num1 , num2 , options):
        if options == "33":
                n = num1 # the range we specified
                m = num2 # The difference we want in each number
                sumi = 0  
                for i in range(1 , n+1):
                        sumi += i  
                        i += m   
                        print(sumi , end= " ")
# lets test it 
# Subdera gave me idea for an 

def big_math_operation(num1 , num2 , options):
        if options == "34":
                n = num1 + num2 
                return f"The biggest operation is to add 1 in {n} which is {n+1}"

def to_binary(num1 , num2 , options):
        if options == "35":
                bin1 = list(map(int , bin(num1).split('b'))) 
                bin2 = list(map(int , bin(num2).split('b'))) 
                print(f"The binary of {num1} is" , ''.join(map(str, bin1))) 
                print(f"The binary of {num2} is" , ''.join(map(str , bin2)))
#the last thing for this part
# We will be checking whether num1 and num2 are palindromes. 
def is_palindrome(num1 , num2 , options):
        if options == "36":
                str1 = str(num1)
                str2 = str(num2)
                if str1 == str1[::-1]: #index slicing
                        print(f"{num1} is a Palindrome") 
                else:
                        print(f"{num1} is not a Palindrome")
                if str2 == str2[:: -1]: 
                        print(f"{num2} is a Palindrome")
                else:
                        print(f"{num2} is not a palindrome")

def bit_count_and_length(num1 , num2 , options):
        if options == "37":
                n = num1.bit_count()
                n2 = num2.bit_count()
                print(f" Bit count of {num1} is {n}")
                print(f" Bit count of  {num2} is {n2}")
        if options == "38":
                len1 = num1.bit_length()
                len2 = num2.bit_length()
                print(f"Bit length of {num1} is {len1}") 
                print(f" Bit length of {num2} is {len2}")

options = input("Choose your Option (1 -39): ")

match options:
        case '1' | '2' | '3' | '4' | '5' | '6':
                num1 , num2 = map(int , input("Enter two numbers separated by space: ").split())
                print(normal_calc(num1 , num2 , options))
        case '7' | '8' | '9' | '10' | '11' | "12" | "13" | "14" | "15" | "16" | "17" | "18" | "19" | "20" | "21" | "22" | "23" | "24" | "25":
                num1 , num2 = map(int , input("Enter two numbers separated by space: ").split())
                print(scientific(num1 , num2 , options))
        case "26" | "27" | "28" | "29" | "30":
                num1 , num2 = map(int , input("Enter two numbers separated by space: ").split())
                print(additional_funcs(num1  , num2 , options))
        case "31":
                num1 , num2 = map(int , input("Enter two numbers separated by space: ").split())
                print(is_prime(num1 , num2 , options))
        case "32":
                num1 , num2 = map(int , input("Enter two numbers separated by space: ").split())
                fibonacci_seq(num1 , num2 , options)
        case "33":
                num1 , num2 = map(int , input("Enter two numbers separated by space: ").split())
                sequence_of_mth_integer(num1 , num2 , options)
        case "34":
                num1 , num2 = map(int , input("Enter two numbers separated by space: ").split())
                print(big_math_operation(num1 , num2 , options))
        case "35":
                num1 , num2 = map(int , input("Enter two numbers separated by space: ").split())
                to_binary(num1 , num2 , options)
        case "36":
                num1 , num2 = map(int , input("Enter two numbers separated by space: ").split())
                is_palindrome(num1 , num2 , options) 
        case "37" | "38":
                num1 , num2 = map(int , input("Enter two numbers separated by space: ").split())
                bit_count_and_length(num1 , num2 , options)
        case "39":
                __builtins__ = None; print(eval(input("Enter Operation: ")))
        case _:
                print("Invalid Option")
