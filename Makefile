all:
	echo "use `make copy` to copy the paper to the root directory."
	make copy
	open ./paper.pdf
	
copy:
	cp ./.out/main.pdf ./paper.pdf