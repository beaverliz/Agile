#!C:\Users\Professional\AppData\Local\Programs\Python\Python38-32\python.exe
import sys
import json

def compare_two_numbers(m, n):
    m_str = str(m)
    n_str = str(n)

    position_match_count = 0
    value_match_count = 0

    m_letters = {}
    n_letters = {}

    for i in range(len(m_str)):
        if m_str[i] == n_str[i]:
            position_match_count += 1
        else:
          if n_str[i] not in n_letters:
              n_letters[n_str[i]] = 1
          else:
              n_letters[n_str[i]] += 1
          if m_str[i] not in m_letters:
              m_letters[m_str[i]] = 1
          else:
              m_letters[m_str[i]] += 1

    intersection = set(m_letters) & set(n_letters)
    for l in intersection:
        value_match_count += min([m_letters[l], n_letters[l]])

    return position_match_count, value_match_count

def compare_many_numbers(number, *numbers):
    x_list = []
    y_list = []

    for n in numbers:
        result1, result2 = compare_two_numbers(number, n)
        x_list.append(result1)
        y_list.append(result2)

    return x_list, y_list

result = compare_many_numbers(sys.argv[1], *map(int, sys.argv[2:]))
print(json.dumps(result))
