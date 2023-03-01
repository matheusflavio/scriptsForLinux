for i in *.pdf; do
    gs \
        -sDEVICE=pdfwrite \
        -dProcessColorModel=/DeviceGray \
        -dColorConversionStrategy=/Gray \
        -dPDFUseOldCMS=false \
        -o "${i%.*} B&W.pdf" \
        -f "$i"
done
