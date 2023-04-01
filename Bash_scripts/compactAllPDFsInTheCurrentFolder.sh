#!/bin/bash
7z -t7z a "PDFsNegainha.7z" *.pdf -m0=lzma2:d1024m -mx=9 -aoa -mfb=64 -md=32m -ms=on