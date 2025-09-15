class SuperStr(str):
    def is_repeatance(self, s):
        if s:
            return self == s * (len(self) // len(s)) and len(self) % len(s) == 0
        else:
            return False

    def is_palindrom(self):
        return self.lower() == self[::-1].lower()

str1 = SuperStr("abobaabobaaboba")
print(f"Строка: {str1}")
print(f"Повторяется: {str1.is_repeatance("aboba")}")
print(f"Палиндром: {str1.is_palindrom()}")
print("")

str2 = SuperStr("")
print(f"Строка: {str2}")
print(f"Повторяется: {str2.is_repeatance("")}")
print(f"Палиндром: {str2.is_palindrom()}")
print("")

str3 = SuperStr("нетнетнетнетнет")
print(f"Строка: {str3}")
print(f"Повторяется: {str3.is_repeatance("нет")}")
print(f"Палиндром: {str3.is_palindrom()}")