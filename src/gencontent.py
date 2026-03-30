from markdown_blocks import markdown_to_html_node
import os
from pathlib import Path
def generate_page(from_path, template_path, dest_path, basepath):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')


    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)

def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")





def generate_pages_recursive(content_dir, template_path, destination_dir, basepath):
    # Convert strings to Path objects if they aren't already
    content_root = Path(content_dir)
    dest_root = Path(destination_dir)

    for entry in content_root.iterdir():
        # Skip hidden files/folders (optional but recommended)
        if entry.name.startswith('.'):
            continue

        # Create corresponding destination path
        dest_path = dest_root / entry.name

        if entry.is_dir():
            dest_path.mkdir(parents=True, exist_ok=True)
            generate_pages_recursive(entry, template_path, dest_path, basepath)
            
        elif entry.suffix == ".md":
            # with_suffix specifically changes the extension only
            html_dest = dest_path.with_suffix(".html")
            generate_page(str(entry), str(template_path), str(html_dest), basepath)