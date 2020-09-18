
'''
find_and_replace('story.txt', 'Alice', 'Colt') 
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
'''

def find_and_replace_v_Oleg(filename, to_replace, replacement):
    with open(filename) as file:
        content = file.read()
    
    new_content = content.replace(to_replace, replacement)
    
    with open(filename, "w") as file:
        file.write(new_content)
            

def find_and_replace_v_Colt(file_name, old_word, new_word):
    with open(file_name, "r+") as file:
        text = file.read()
        new_text = text.replace(old_word, new_word)
        file.seek(0)
        file.write(new_text)
        file.truncate()