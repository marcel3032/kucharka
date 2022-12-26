import jinja2
import yaml
import os
import jsonschema
import json

recipes_dir = 'recipes'
out_dir = '..'+os.sep+'built_recipes'
tex_filname_extension = '.tex'

environment = jinja2.Environment(loader = jinja2.FileSystemLoader('./'))

template = environment.get_template("00_template.tex")

# create build directory
if not os.path.exists(out_dir+os.sep):
    os.makedirs(out_dir+os.sep)

for dir in list(os.listdir(recipes_dir)):
  print(f"dir {repr(dir)}:")
  
  # create output directories
  if not os.path.exists(out_dir+os.sep+dir+os.sep):
    os.makedirs(out_dir+os.sep+dir+os.sep)
  
  for recipe in os.listdir(recipes_dir+os.sep+dir):
    print(f"  recipe {repr(recipe)}")
    recipe_filename = recipes_dir+os.sep+dir+os.sep+recipe

    assert recipe_filename[-4:]=='.yml'
    values = yaml.safe_load(open(recipe_filename, 'r', encoding='utf-8'))
    schema = json.load(open('recipe-schema.json', 'r'))
    jsonschema.validate(instance=values, schema=schema)
    with open(out_dir+os.sep+dir+os.sep+recipe[:-4]+tex_filname_extension, 'w', encoding='utf-8') as fout:
      print(template.render(values), file=fout)