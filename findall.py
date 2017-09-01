import re
ssnRegex= re.compile(r"\d\d\d-\d\d\-\d\d\d\d")
print(ssnRegex.findall("The two ssns's you are looking for are 123-19-9501 and 321-54-9876."))
