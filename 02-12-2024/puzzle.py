from copy import deepcopy

def __check_safety(report):
  increasing = False
  decreasing = False
  for k,v in enumerate(report):
    if (k == len(report) - 1) and k > 0:
      return True
    diff = int(v) - int(report[k + 1])
    if diff == 0:
      break
    if diff > 3 or diff < -3:
      break
    if diff < 0:
      if decreasing:
        break
      else:
        increasing = True
    if diff > 0:
      if increasing:
        break
      else:
        decreasing = True
  return False

def safe_reports():
  input_file  = open('input.txt', 'r')
  lines = input_file.readlines()
  input_file.close()
  safe_reports = 0
  for line in lines:
    report = line.split(' ')
    if __check_safety(report):
      safe_reports += 1
    else:
      for k,v in enumerate(report):
        new_report = deepcopy(report)
        new_report.pop(k)
        if __check_safety(new_report):
          safe_reports += 1
          break
  return safe_reports

print(safe_reports())
