all:
	echo "use `make copy` to copy the paper to the root directory."
	make copy
	open ./paper.pdf

latexInit:
	sudo apt -y update
	sudo apt -y install texlive-full
	sudo apt -y install texlive-lang-chinese texlive-fonts-recommended

build:
	mkdir -p .out
	xelatex -file-line-error -halt-on-error -interaction=nonstopmode -output-directory=.out main.tex

count:
	# echo "Counting the number of words in the paper."
	# echo "should use `go install github.com/leon123858/latex-directory-counter@latest` first."
	latex-directory-counter ./contents

copy:
	cp ./.out/main.pdf ./paper.pdf