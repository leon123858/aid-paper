all:
	echo "use `make copy` to copy the paper to the root directory."
	make copy
	open ./paper.pdf

init:
	go install github.com/leon123858/latex-directory-counter@latest

count:
	# echo "Counting the number of words in the paper."
	# echo "should use make init first."
	latex-directory-counter ./contents

copy:
	cp ./.out/main.pdf ./paper.pdf