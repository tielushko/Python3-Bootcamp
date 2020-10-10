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

#HTML SELECTORS

#selecting all using html tags - find all returns a list with tags.
print(soup.find_all("li"))
print()

#selecting the element by id
print(soup.find(id="first"))
print()

#selecting the elements by class special. notice since class is reserved Python word we need to use the class_
print(soup.find_all(class_="special"))
print()

#selecting elements which have their data attributes set to a specific value
print(soup.find_all(attrs={"data-example" : "yes"}))
print()

#CSS SELECTORS

#select - returns the list of the id even if only one element
print(soup.select("#first"))
print()

# by class
print(soup.select(".special"))
print()

# by tag 
print(soup.select("div"))
print()

# by attribute
print(soup.select("[data-example]"))
print()


