import re


def check_filename_rules(line):
    rules_list = open('../resources/rulepack-filename').readlines()
    for rule in rules_list:
        rule = rule.strip()
        if "char:" in rule:
            rule = rule.split(":")[1] + "."
            if rule in line:
                return True

        if "regex:" in rule:
            regex_rule = rule.split(":")[1] + ".java"
            p = re.compile(regex_rule)
            if p.findall(line):
                return True
            if p.match(line):
                return True

    return False


print(check_filename_rules("helloworld.java"))
print(check_filename_rules("a.java"))
print(check_filename_rules("aa.java"))
print(check_filename_rules("aabb.java"))
print(check_filename_rules("aaaaaaaa.java"))
print(check_filename_rules("zzzzzzzzzzzz.java"))
print(check_filename_rules("UserActionProxy.java"))
