# kucharka

Simple tex template for cooking recipes

## workflow for adding recipe

- add `recipe_name.tex` to `/recipes`
- add recipe to `main.tex`
- build (`make.bat` on Windows) or
	- build pdf e.g. (`pdfLaTeX main.tex`)
	- build html e.g. (`htlatex main.tex "xhtml,html5,index=3,charset=utf-8" " -cunihtf -utf8"`)

