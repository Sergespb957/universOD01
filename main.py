def is_palindrome(string):
  """Проверяет, является ли строка палиндромом.

  Args:
    string: Строка для проверки.

  Returns:
    True, если строка является палиндромом, иначе False.
  """

  # Преобразование строки к нижнему регистру и удаление пробелов и знаков препинания
  cleaned_string = string.lower().replace(" ", "").replace(",", "").replace(".", "")  # Можно добавить другие знаки препинания по необходимости

  # Сравнение символов с начала и конца
  left = 0
  right = len(cleaned_string) - 1
  while left < right:
    if cleaned_string[left] != cleaned_string[right]:
      return False
    left += 1
    right -= 1
  return True

string = input("Введите строку: ")
if is_palindrome(string):
    print("Строка является палиндромом.")
else:
    print("Строка не является палиндромом.")