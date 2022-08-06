# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    
    def handle_starttag(self, tag, attrs):
        print(tag)
        for key, value in attrs:
            print("-> {} > {}".format(key, value))
            
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for key, value in attrs:
            print(f"-> {key} > {value}")
            
html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
Parser = MyHTMLParser()
Parser.feed(html)
Parser.close()
            