from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

#gets everything inside the body as a list, notice that the list will also have the new line tags
data = soup.body.contents[1].next_sibling.next_sibling.contents
print(data)

data = soup.find(class_='special').parent
print(data)

data = soup.find(id='first').find_next_sibling()
print(data) 