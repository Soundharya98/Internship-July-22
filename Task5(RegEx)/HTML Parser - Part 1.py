# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    
    def handle_starttag(self, tag, attrs):
        print ("Start :",tag)
        for n, m in attrs:
            print("->", n, ">", m)
            
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        for n, m in attrs:
            print("->", n, ">", m)
            
    def handle_endtag(self, tag):
        print ("End   :", tag)
        
parser = MyHTMLParser()
for i in range (int(input())):
    parser.feed(input())
        