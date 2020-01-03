# Wonka Vision

## Processing Frames
I guarantee somebody is going to look at this and claim it can be done in one line by chaining ffmpeg filters. I need each frame to be ~1273 bytes (in base64) so it must be VERY compressed, and I'm using png's instead of jpg's because I prefer the "compressed png posterized" look more than the "blocky jpeg" look. I need 172 = (16x11) compressed frames to fill by 32"x12" canvas with 2" QR codes.

I currently am having success fitting 75x75px images into ~1273 bytes which allows for the highest level of redundancy in the QR codes. I need to try 100x100 images or similar size.. and to fit them into ~1663 bytes for "Q" level QR code redundancy.

### Frames From Video
```{bash}
# 5 frames per second
ffmpeg -i ./video.mp4 -vf fps=5 ./frames/%04d.jpg
```

### Crop Frames to Squares
```{bash}
# Cropping 1280x720 to 720x720
# - Offset x-coordinate by (1280-720)=560
# - Convert to png 
ffmpeg -i image.jpg -vf "crop=720:720:560:0" cropped.png

# Batch Version
ls *.jpg | xargs -n 1 bash -c 'ffmpeg -i "$0" -vf crop=720:720:560:0 "${0%.jpg}.png"'
```

### Scale Cropped Frames
```{bash}
ls *.png | xargs -n 1 bash -c 'ffmpeg -i "$0" -vf scale=75:75 "scaled-$0"'
```

### Compress Image
```{bash}
# pngquant without dithering gives best compression size
ls *.png | xargs -n 1 bash -c 'pngquant --nofs --speed=1 --output="./compressed/$0" 4 "$0"' 
```

### Convert Image to base64
```
base64 ./image.png > image.txt
```

### Rename Files to Numerical Order
```{bash}
# Source https://stackoverflow.com/a/34153342/7823010
ls -v | cat -n | while read n f; do mv -n "$f" "$n.ext"; done
```

