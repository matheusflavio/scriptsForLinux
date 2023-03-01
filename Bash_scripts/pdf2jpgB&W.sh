for i in *.pdf; do
    pdftoppm -jpeg -gray "$i" "${i%.*}"
done