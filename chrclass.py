import re

testRegex = re.compile(r"[a-dA-P]")
print(testRegex.findall("Peter Piper Picked A Peck of Pickled Peppers."))
