# Printing Process

## Dimensions and Dot Sizes
Here I will show the calculation for dot sizes in pixels
- DPI := 320 (px per inch)
- Image Size := 11" x 14"
  - 3,520px x 4,480px
- Dots will be bounded by a 1/16" box
  - This means 256 dots/inch^2
  - Bounding box of dot is 20px (DPI * Dot Size)
  - 3px padding leaves a 14px diameter circle
- There is space for 14x11x256 = 39,424 dots
  - Encoding characters yields ~12 pages of text
  - Encoding words yields ~80 pages of text
- This configuration gives
  - Box Size := 20
  - Boxes Wide := 176
  - Boxes Tall := 224

1/32 inch
- DPI := 640 (px per inch)
- Image Size := 11" x 14"
  - 3,520px x 4,480px
- Dots will be bounded by a 1/32" box
  - This means 1024 dots/inch^2
  - Bounding box of dot is 20px (DPI * Dot Size)
  - 3px padding leaves a 14px diameter circle
- There is space for 14x11x1024 = 157,696 dots
- This configuration gives
  - Box Size := 20
  - Boxes Wide := 352
  - Boxes Tall := 448