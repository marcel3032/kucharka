REM ## WARNING: Using OEM 852 encoding to work in w7 cmd.exe ##

mkdir build

pdfLaTeX -output-directory build main.tex
pdfLaTeX -output-directory build main.tex

REM htlatex main.tex "xhtml,html5,index=3,charset=utf-8" " -cunihtf -utf8"
REM htlatex main.tex "xhtml,html5,index=3,charset=utf-8" " -cunihtf -utf8"

pandoc main.tex -s --toc -t html -o build/main.html --metadata title="Kuch rka" -c style.css
pandoc main.tex -s --toc -t html -o build/main.html --metadata title="Kuch rka" -c style.css