from textnode import TextNode, TextType
import os, shutil
from copy_static import copyfilesrecursive
from gencontent import generate_pages_recursive
import sys

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"

def main():
   basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
   if not basepath.startswith("/"):
        basepath = "/" + basepath
   if not basepath.endswith("/"):
        basepath += "/"
   print(f"Basepath = '{basepath}'")

   print("Deleting public directory...")
   if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

   print("Copying static files to public directory...")
   copyfilesrecursive(dir_path_static, dir_path_public)

   print("Generating content...")
   generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)


if __name__ == "__main__":
    main()