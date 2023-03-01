#!/bin/bash
array=( *.cia *.nds *.md *.gba *.gbc *.gb *.nes *.smc *.gg *.iso *.cso )
for i in "${array[@]}"; do
    7z a -t7z "${i%.*}.7z" "$i" -m0=lzma2:d1024m -mx=9 -aoa -mfb=64 -md=32m -ms=on
done
rm "*.7z"