for i in *.pdf; do
    pdftoppm -jpeg "$i" "${i%.*}"
done