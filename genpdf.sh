#!/bin/sh

pandoc README.md -s -f markdown-implicit_figures -V geometry:margin=1in -V geometry:paperheight=2800px -o README.pdf