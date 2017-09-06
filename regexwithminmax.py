import re
runRegex=re.compile(r"(blah){2,4}")
run_match=runRegex.search("blahblah")
print(run_match.group())
run_match=runRegex.search("blahblahblah")
print(run_match.group())
run_match=runRegex.search("blahblahblahblahblahblah")
print(run_match.group())
