#!/bin/bash
if [ -f *.7z ]; then 
    (7z e "*.7z" *.cia *.nds *.md *.gba *.gbc *.gb *.nes *.smc *.gg *.iso *.cso)
fi

if [ -f *.zip ]; then 
    (7z e "*.zip" *.cia *.nds *.md *.gba *.gbc *.gb *.nes *.smc *.gg *.iso *.cso)
fi

if [ -f *.rar ]; then 
    (7z e "*.rar" *.cia *.nds *.md *.gba *.gbc *.gb *.nes *.smc *.gg *.iso *.cso)
fi