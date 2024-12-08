import re
from sys import exit

input_file = open('input.txt', 'r')
lines = input_file.readlines()
input_file.close()

input = ''.join(lines).replace('\n', '')

inital = re.findall('mul\(([0-9]{1,3}),([0-9]{1,3})\)', re.search('.*?don\'t', input).group())
_do = re.findall('mul\(([0-9]{1,3}),([0-9]{1,3})\)', ''.join(re.findall('do\(\)(.*?)don\'t\(\)', input)))

all_mul = inital + _do

end_sum = 0
for sum in all_mul:
  num_1 = int(sum[0])
  num_2 = int(sum[1])
  end_sum += (num_1 * num_2)

print(end_sum)
