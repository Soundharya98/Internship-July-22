# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

storage = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])', input(),flags = re.I)

if storage:
      print(*storage, sep="\n")
else:
    print(-1)