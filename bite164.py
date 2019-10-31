import sys
import subprocess

INTERNAL_LINKS = ('pybit.es', 'codechalleng.es')


def make_html_links():
    result = subprocess.check_output(['cat']).decode("utf-8")
    links = []
    for item in result.split('\n'):
        if 'https://' in item:
            site = item.split(',')
            print(site[0].strip())
            if any(ext in site[0].strip() for ext in INTERNAL_LINKS):
                links.append('<a href="{}">{}</a>'.format(site[0].strip(), site[1].strip()))
            else:
                links.append('<a href="{}" target="_blank">{}</a>'.format(site[0].strip(), site[1].strip()))

    for link in links:
        print(link)



if __name__ == '__main__':
    make_html_links()