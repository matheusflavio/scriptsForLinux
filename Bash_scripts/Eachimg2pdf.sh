for i in *.png; do
    img2pdf "$i" -o "${i%.*}.pdf"
done

dor i in *.jpg;do
    img2pdf "$i" -o "${i%.*}.pdf"

dor i in *.jpeg;do
    img2pdf "$i" -o "${i%.*}.pdf"