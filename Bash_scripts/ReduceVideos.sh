for i in *.mkv; do
    ffmpeg -i "$i" "${i%.*} reduzido.mp4"
done
for i in *.mp4; do
    ffmpeg -i "$i" "${i%.*} reduzido.mp4"
done
