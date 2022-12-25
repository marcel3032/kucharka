import jinja2
import yaml
import os

recipes_dir = 'recipes'
out_dir = '..'+os.sep+'output_recipes'
tex_filname_extension = '.tex'

environment = jinja2.Environment(loader = jinja2.FileSystemLoader('./'))

template = environment.get_template("00_template.tex")

for dir in list(os.listdir(recipes_dir)):
  print(f"dir {repr(dir)}:")
  for recipe in os.listdir(recipes_dir+os.sep+dir):
    print(f"  recipe {repr(recipe)}")
    recipe_filename = recipes_dir+os.sep+dir+os.sep+recipe

    assert recipe_filename[-4:]=='.yml'
    values = yaml.safe_load(open(recipe_filename, 'r', encoding='utf-8'))
    with open(out_dir+os.sep+dir+os.sep+recipe[:-4]+tex_filname_extension, 'w', encoding='utf-8') as fout:
      print(template.render(values), file=fout)