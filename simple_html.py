from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum sit amet. Consectetur edipiscim elit.</p>
<p>Here's another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Joser</li>
</ul>
</body>
</html>
'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

print(simple_soup.find('h1').string)