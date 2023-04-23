# What is this ?
Watermark and encrypt a pdf file for multiple targets
QuickActions did not work for me, more info on quickactions in https://www.maketecheasier.com/watermark-pdf-pages-quick-actions-macos/

# Pre-requisites
Ensure the files are executable
	chmod +x *.py
	chmod +x *.php

Modify watermarkencrypt.bash to suit your needs then run it:
	bash watermarkencrypt.bash

# Explanations
This uses MacOS builtin php and python technology to create a png file (the watermark) that will be applied to a pdf.
The pdf is then copied to a password protected version.
