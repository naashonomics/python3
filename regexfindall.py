import re

zipRegex = re.compile(r"\d\d\d\d\d")
address = """  340 Sunnyvale CA 94086
			san jose 94086
			bnagalore 560086
		 """
print(zipRegex.findall(address))
