# kucharka

Simple tex template for cooking recipes

## workflow for adding recipe

- add `<name>.yml` to `/input_recipes/<type>/`
- generate recipes `python input_recipes/create_recipes.py`
- add output recipe to `main.tex`
- build
	- `make.bat` on Windows (using `OEM 852` encoding)
	- or build manually:
		- build pdf e.g. (`pdfLaTeX main.tex`)
		- build html e.g. (`pandoc main.tex -s --toc -t html -o main.html --metadata title="Kuchárka"`)


## OLD workflow for adding recipe

- add `recipe_name.tex` to `/recipes`
- add recipe to `main.tex`
- build
	- `make.bat` on Windows (using `OEM 852` encoding)
	- or build manually:
		- build pdf e.g. (`pdfLaTeX main.tex`)
		- build html e.g. (`pandoc main.tex -s --toc -t html -o main.html --metadata title="Kuchárka"`)

