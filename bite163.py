def changed_dependencies(old_reqs: str, new_reqs: str) -> list:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    old = old_reqs.split('\n')[1:-1]
    new = new_reqs.split('\n')[1:-1]
    answer = []
    for i, item in enumerate(old):
        if int(item.split('==')[1].split('.')[0]) < int(new[i].split('==')[1].split('.')[0]):
            answer.append(item.split('==')[0])
            continue
        if int(item.split('==')[1].split('.')[0]) == int(new[i].split('==')[1].split('.')[0]):
            if int(item.split('==')[1].split('.')[1]) < int(new[i].split('==')[1].split('.')[1]):
               answer.append(item.split('==')[0])
    return answer

old_reqs = """
twilio==6.23.1
urllib3==1.21.1
Werkzeug==0.12.1
WTForms==1.19.0
"""
new_reqs = """
twilio==6.3.0
urllib3==1.21.1
Werkzeug==0.14.1
WTForms==2.1
"""

print(changed_dependencies(old_reqs, new_reqs))