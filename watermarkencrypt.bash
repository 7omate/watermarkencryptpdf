#!/bin/bash

passwords=("user1@mail.com" "user2@mail.com")

file="ex.pdf"


for p in ${passwords[@]}; do
	# Create watermark
	./text2img.php text=$p
	# Apply watermark
	./watermark.py --input $file --output $file-wtrmk $p.png
	# Encrypt file
	./pdfpassword.py --input $file-wtrmk --password $p --output $file.$p.pdf
	# Cleanup
	echo "Removing working files"
	rm -v $file-wtrmk $p.png
done
