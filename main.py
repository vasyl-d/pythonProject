# This is a sample Python script.
thous = {"",'сто',"двести","триста","четыреста","пятьсот","шестьсот","семьсот","восемьсот","девятьсот"}
ones = {'', "один"}
decs = ['', ['тысяча','тысячи','тысяч'], ['миллион','миллиона','миллионов']]

dict_lang = {"ru": [{"m":"один", "f":"одна"}, {"m":"два", "f":"две"}] }

def NumberToText(n):
   n = int(n)
   if ( n < 0 ):
      return "Minus " + NumberToText(-n)
   elif ( n == 0 ):
      return ""
   elif ( n <= 19 ):
      return  ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", 
         "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", 
         "Seventeen", "Eighteen", "Nineteen"][n-1] + " "
   elif ( n <= 99 ):
      return ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", 
         "Eighty", "Ninety"][int(n / 10) - 2] + " " + NumberToText(int(n % 10))
   elif ( n <= 199 ):
      return "One Hundred " + NumberToText(int(n % 100))
   elif ( n <= 999 ):
      return NumberToText(int(n / 100)) + "Hundreds " + NumberToText(int(n % 100))
   elif ( n <= 1999 ):
      return "One Thousand " + NumberToText(int(n % 1000))
   elif ( n <= 999999 ):
      return NumberToText(int(n / 1000)) + "Thousands " + NumberToText(int(n % 1000))
   elif ( n <= 1999999 ):
      return "One Million " + NumberToText(int(n % 1000000))
   elif ( n <= 999999999):
      return NumberToText(int(n / 1000000)) + "Millions " + NumberToText(n % 1000000)
   elif ( n <= 1999999999 ):
      return "One Billion " + NumberToText(n % 1000000000)
   else:
      return NumberToText(int(n / 1000000000)) + "Billions " + NumberToText(n % 1000000000)


str1 = input("введите число")
l = len(str1)
m = l % 3
s2 = [str1[j-3:j] for j in range(l, m, -3)]
if m != 0:
    s2 = s2 + [str1[:m]]
print(s2)

ss = [s2[x] for x in range(len(s2)-1, -1,-1)]
print(ss)

nu = int(str1)
print(NumberToText(nu))