import re
#greedy and non greedy matching 
#greedy match
runRegex=re.compile(r"(\w){1,3}") 
#earliest match one python can find is the one that is returnted 
run_match=runRegex.search("Eyes")
print(run_match.group())
#non greddy match
runRegex=re.compile(r"(\w){1,3}?")
run_match=runRegex.search("Eyes")
print(run_match.group())
