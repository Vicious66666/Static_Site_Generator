import shutil
import os
from textnode import TextNode
from copy_folder import copy_directory_recursive
from gencontent  import generate_page, generate_pages_recursive  
#./main.sh
# hello world

def main():
    #my_textnode = TextNode("This is some text", "link", "https://www.pmcdm.com") 
    #print(my_textnode)
    if os.path.exists("public"):
        shutil.rmtree("public")
    copy_directory_recursive("static", "public")
    #generate_page("content/index.md", "template.html", "public/index.html")
    generate_pages_recursive("content", "template.html", "public")    
main()