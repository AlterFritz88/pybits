def generate_affiliation_link(url):
    url = url.split('/')
    return 'http://www.amazon.com/dp/' + url[5] + '/?tag=pyb0f-20'

original = 'https://www.amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/?keywords=war+of+art'
print(generate_affiliation_link(original))