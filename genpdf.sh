#!/bin/sh

pandoc README.md -s -f markdown-implicit_figures -V geometry:margin=1in -V geometry:paperheight=3000px -o README.pdf