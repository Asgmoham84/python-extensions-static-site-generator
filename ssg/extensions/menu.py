from ssg import hooks, parsers


files = []
@hooks.register("collect_files")
def collect_files (source, site_parser):
    valid = not (lambda p: p.isinstance(parsers.ResourceParser))
    for path in source.rglob("*"):
        for parser in list(filter(valid, site_parser)):
            if parser.valid_file_ext(path.suffix):
                files.append(path)

@hooks.register("generate_menu")
def generate_menu(html, ext):
    template = '<li><a href="{}{}">{}</a></li>'
    menu_item = lambda name, ext: template.format(name, ext, "Name")
    menu = [menu_item(path.stem, ext) for path in files]
    "\n".join(menu)
    return "<ul>\n{}<ul>\n{}".format(menu, html)





