import re


def check_rules(line):
    rules_list = open('../resources/rulepack').readlines()
    for rule in rules_list:
        rule = rule.strip()
        if "char:" in rule:
            rule = rule.split(":")[1] + "."
            if rule in line:
                return True

        if "regex:" in rule:
            regex_rule = rule.split(":")[1]
            p = re.compile(regex_rule)
            if "java" in line:
                return False
            if p.findall(line):
                return True
            if p.match(line):
                return True

    return False


print(check_rules("public String h = 123;"))
print(check_rules("public String password"))

print(check_rules("public String h;"))
print(check_rules("public String password"))


print(check_rules("final class a extends a.e.a {"))
print(check_rules("final class pwutils extends passwordclass {"))


print(check_rules("import a.b.c;"))
print(check_rules("package com.tencent.beacon.cover;"))


print(check_rules("f.a(\"W\", \"context is null!\", new Object[0]);"))
print(check_rules("get_password(\"W\", \"context is null!\", new Object[0]);"))
