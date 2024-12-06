import re

def list_generator():
  input_file  = open('input.txt', 'r')

  count = 0
  left_list = []
  right_list = []
  for line in input_file.readlines():
    count += 1
    try:
      result = re.search("^([0-9]+)\s+([0-9]+)$", line)
    except:
      print(f"WARNING: Line {count} doesn't contain two numbers")
      continue
    left_list.append(int(result.groups()[0]))
    right_list.append(int(result.groups()[1]))
  if len(left_list) != len(right_list):
    return "Lists are mismatched, oops"
  return left_list, right_list

def difference_checker(): # Part 1
  left_list, right_list = list_generator()
  left_list.sort()
  right_list.sort()
  difference = 0
  for i in range(len(left_list)):
    individual_difference = left_list[i] - right_list[i]
    if individual_difference > 0:
      difference += individual_difference
    else:
      difference -= individual_difference
  return difference

def similarity_score():
  left_list, right_list = list_generator()
  similarity_score = 0
  for left_num in left_list:
    for right_num in right_list:
      if left_num == right_num:
        similarity_score += right_num
  return similarity_score
