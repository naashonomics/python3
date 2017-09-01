#zip code format=12345-6789
#pattern = r"/d/d/d/d/d-/d/d/d/d"
import re
zipCodeRegex= re.compile(r"(\d\d\d\d\d)-(\d\d\d\d)")
zip_match= zipCodeRegex.search("My Zip code is 12345-6789 and 98765-4321")
#prints entire zipcode
print(zip_match.group())
#prints first 5 digits of zipcode
print(zip_match.group(1))
#prints last 4 digits of zipcode
print(zip_match.group(2))
