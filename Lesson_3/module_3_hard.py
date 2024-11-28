def isfloat(string):
  try:
    float(string)
    return True
  except ValueError:
    return False


def calculate_structure_sum(*structures):
    summa = 0
    for elem in structures:
      if isinstance(elem, int) or isinstance(elem, str) and elem.isdigit():
        summa += int(elem)
      elif isinstance(elem, float) or isinstance(elem, str) and isfloat(elem):
          summa += float(elem)
      elif isinstance(elem, str):
        summa += len(elem)
      elif isinstance(elem, dict):
        summa += calculate_structure_sum(*elem, elem.values())
      else:
        summa += calculate_structure_sum(*elem)
    return summa

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)