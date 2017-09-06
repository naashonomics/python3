import re
runRegex=re.compile(r"(blah){2,4}")
#runRegex=re.compile(r"(blah){2,}") two or more blah's 
run_match=runRegex.search("blahblah")
print(run_match.group())
run_match=runRegex.search("blahblahblah")
print(run_match.group())
run_match=runRegex.search("blahblahblahblahblahblah")
print(run_match.group())
