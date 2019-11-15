from pathlib import Path
from urllib.request import urlretrieve

tmp = Path('/tmp')
timings_log = tmp / 'pytest_timings.out'
if not timings_log.exists():
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/pytest_timings.out',
        timings_log
    )
def timings():
    with open(timings_log) as f:
        return f.readlines()
for _ in timings():
    print(_)


def get_bite_with_fastest_avg_test(timings: list) -> str:
    """Return the bite which has the fastest average time per test"""
    dict_test = {}
    for item in timings:
        if "no tests ran" in item:
            continue
        splited_item = item.split(" ")
        if "warnings" not in item:
            dict_test[splited_item[0]] = (float(splited_item[5]) / (int(splited_item[2])))
        else:
            dict_test[splited_item[0]] = (float(splited_item[7]) / (int(splited_item[2]) + (int(splited_item[4]))))



    #splited_list = {x.split(" ")[0] : (float(x.split(" ")[5]) / (int(x.split(" ")[0]))) for x in timings}
    return sorted(dict_test.items(), key=lambda x: x[1])[0][0]

print(get_bite_with_fastest_avg_test(timings()))