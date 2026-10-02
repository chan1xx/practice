temp_c = float(input())
temp_f = (temp_c * 9.5) + 32
temp_k = temp_c + 273.15
print(f"{temp_c} в цельсиях = {round(temp_f, 2)} в фаренгейтах")
print(f"{temp_c} в цельсиях = {round(temp_k, 2)} в кельвинах")