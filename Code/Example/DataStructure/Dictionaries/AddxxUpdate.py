results = {"pass": 0, "fail": 0}
print(results)   # {'pass': 0, 'fail': 0}

results["withdrawal"] = 1
print(results)   # {'pass': 0, 'fail': 0, 'withdrawal': 1}

results["pass"] = 3
results["fail"] = results["fail"] + 1
print(results)   # {'pass': 3, 'fail': 1, 'withdrawal': 1}

print(results["fail"])
print(results["pass"])
print(results["withdrawal"])

"""
{'pass': 0, 'fail': 0}
{'pass': 0, 'fail': 0, 'withdrawal': 1}
{'pass': 3, 'fail': 1, 'withdrawal': 1}
1
3
1
"""

# 将字典中的Key,value转化为表格
a = list(results.keys())
print(a)   # ['pass', 'fail', 'withdrawal']
b = list(results.values())
print(b)   # [3, 1, 1]

# 字典长度
print("The length of dic:", len(results))  # The length of dic: 3

# 判断存在与否
x = "pass"
if x in results.keys():
    print("At least one of the key in results is:", x)  # At least one of the value in results is: pass
else:
    print("None of the key in results are:", x)

if "fail" in results.keys():
    print("At least one of the key in results is fail")  # At least one of the value in results is fail
else:
    print("None of the key in results is fail")

y = 3
if y in results.values():
    print("At least one of the value in results is:", y)  # At least one of the value in results is: pass
else:
    print("None of the value in results are:", y)