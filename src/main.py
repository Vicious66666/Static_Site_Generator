import shutil
import os
import sys
from textnode import TextNode
from copy_folder import copy_directory_recursive
from gencontent  import generate_pages_recursive  


def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1] 
    else:
        basepath = "/"  
    #if os.path.exists("public"):
    #    shutil.rmtree("public")
    #copy_directory_recursive("static", "public")
    if os.path.exists("docs"):
        shutil.rmtree("docs")   
    copy_directory_recursive("static", "docs")
    #generate_page("content/index.md", "template.html", "public/index.html")
    #generate_pages_recursive("content", "template.html", "public") 
    print("basepath=", basepath)
    generate_pages_recursive("content", "template.html", "docs", basepath)   
main()