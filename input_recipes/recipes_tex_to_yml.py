import sys
import os
import yaml

recipes_dir = '..' + os.sep + 'recipes' + os.sep
out_dir = '..' + os.sep + 'recipes' + os.sep + 'out' + os.sep

for recipe in os.listdir(recipes_dir):
  if recipe == 'out':
    continue
  with open(recipes_dir + os.sep + recipe, 'r', encoding='utf-8') as recipe_f:
    print(f"parsing {recipe}")
    recipe_dict = {}
    lines = recipe_f.readlines()
    for i in range(len(lines)):
      lines[i] = lines[i].strip()
    for i in range(len(lines)-1):
      if lines[i]=='\\end{subingredient}' and lines[i+1]=='\\end{ingredient}':
        lines.insert(i+1, '')
        break
    i = 0

    # name
    while 'subsection' not in lines[i]:
      i += 1
    recipe_dict['name'] = lines[i][lines[i].index('subsection{') + len('subsection{'):-1]

    # picture
    while 'includegraphics' not in lines[i]:
      i += 1
    if lines[i][0] != '%':
      recipe_dict['photo'] = {
        'path': lines[i][lines[i].index(']{') + len(']{'):-1],
        'height': '5.5cm'
      }
      if 'height=5.5cm' not in lines[i]:
        print(f"  non standard height of picture: {lines[i]}")

    # portions
    while 'portions' not in lines[i]:
      i += 1
    recipe_dict['portions'] = lines[i][lines[i].index('portions{') + len('portions{'):-2]

    # ingredients
    while 'begin{main}' not in lines[i]:
      i += 1
    i += 1
    recipe_dict['ingredients'] = {}
    recipe_dict['ingredients']['main'] = []
    while 'end{main}' not in lines[i]:
      if lines[i]!='':
        # print(lines[i])
        recipe_dict['ingredients']['main'].append(lines[i][lines[i].index('item') + len('item'):].strip())
      i += 1

    recipe_dict['ingredients']['other'] = {}
    
    i += 1
    while lines[i] == '':
      i += 1
    
    # print(lines[i])
    
    while 'end{ingredient}' not in lines[i]:
      # print(lines[i])
      while 'begin{subingredient}' not in lines[i]:
        # print(lines[i])
        i += 1
      # print('koniec')
      name = lines[i][lines[i].index('begin{subingredient}{') + len('begin{subingredient}{'):-1]
      recipe_dict['ingredients']['other'][name] = []
      i += 1
      while 'end{subingredient}' not in lines[i]:
        recipe_dict['ingredients']['other'][name].append(lines[i][lines[i].index('item ') + len('item '):])
        i += 1
      i += 2

    # preparation
    while 'begin{enumerate}' not in lines[i]:
      i += 1
    i += 1

    recipe_dict['preparation'] = []
    while 'end{recipe}' not in lines[i]:
      if 'item{' in lines[i]:
        recipe_dict['preparation'].append(lines[i][lines[i].index('item{') + len('item{'):-1])
      else:
        recipe_dict['preparation'].append(lines[i])
      i += 1

    recipe_dict['notes'] = []
    
    while 'begin{notes}' not in lines[i]:
      i += 1
    i += 1
    while 'end{notes}' not in lines[i]:
      recipe_dict['notes'].append(lines[i])
      i += 1
      
    recipe_dict['notes'] = ' '.join(recipe_dict['notes'])
    
    with open(out_dir + recipe[:-4]+'.yml', 'w', encoding='utf-8') as out_f:
      yaml.safe_dump(recipe_dict, out_f, allow_unicode=True, encoding='utf-8', sort_keys=False)
