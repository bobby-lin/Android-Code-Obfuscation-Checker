import os
import pprint
import re


def get_all_files(directory_path):
    list_files = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".java"):
                list_files.append(os.path.join(root, file))
    return list_files


def check_rules(line):
    rules_list = open('resources/rulepack').readlines()
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


def check_filename_rules(line):
    rules_list = open('resources/rulepack-filename').readlines()
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


def check_file(file_path):
    try:
        file = open('%s' % file_path).read()

        i = 1
        num_obfuscated_line = 0

        file_json = {"total_lines": len(file), "filename": file_path.split('/')[-1], "is_filename_obfuscated": False,
                     "obfuscated_code": [], "num_of_obfuscated_line": 0, "filepath": file_path}

        file = open('%s' % file_path)

        if check_filename_rules(file_path.split('/')[-1]):
            file_json['is_filename_obfuscated'] = True

        for line in file.readlines():
            i = i + 1
            if check_rules(line):
                code = {"line": i, "code": line.strip().replace('\n', ' ')}
                file_json['obfuscated_code'].append(code)
                num_obfuscated_line = num_obfuscated_line + 1

        file_json['num_of_obfuscated_line'] = num_obfuscated_line

        pprint.pprint(file_json)

    except UnicodeDecodeError as e:
        print(e)

    except IOError as e:
        print(e)


def run_checker(app_loc, appcode, code_dir):
    run_decompilation(app_loc, appcode)
    list_java_files = get_all_files(code_dir)
    for filepath in list_java_files:
        check_file(filepath)


def run_decompilation(app_loc, appcode):
    JADX_LOC = "resources/jadx-0.8.0/bin/jadx"
    APK_LOC = app_loc
    OUTPUT_LOC = "Decompiled/" + appcode
    command = JADX_LOC + " " + APK_LOC + " -d " + OUTPUT_LOC
    os.system(command)


# This is a demo using GRAB APK
run_checker("apk/com.grabtaxi.passenger.apk", "GRAB", "Decompiled/GRAB/sources/com/grabtaxi")
