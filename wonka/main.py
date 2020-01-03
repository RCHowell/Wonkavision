import qrcode
from PIL import Image, ImageDraw

code_size = 2 # QR Code size in inches
box_size = code_size # This simplifies DPI logic
boxes_per_code = 177 # v40 QR Code is 177x177 boxes
width = 3 # width of grid
height = 2 # height of grid
padding = 1 # Padding size in # of boxes
# Calculate pixels per inch
# box_size * (boxes_per_code + 2 * padding) / code_size
dpi = boxes_per_code + 2 * padding
# How much room does a QR Code take up in Pixels?
block_size = code_size * dpi
# Grid to compose images onto
grid = Image.new('RGB', (width * block_size, height * block_size))

def makeCode(data, color):
  # 177 x 177 boxes
  # 2,953 bytes @ ~7% error correction
  # 2,331 bytes @ ~15% error correction
  qr = qrcode.QRCode(
      version = 40,
      error_correction = qrcode.constants.ERROR_CORRECT_H,
      box_size = box_size,
      border = padding,
  )
  qr.add_data(data)
  qr.make()
  return qr.make_image(fill_color=color, back_color="white")


for i in range(0, width):
  for j in range(0, height):
    n = i * height + j + 1
    data = open(f'./assets/small_frames/{n}.txt', 'r').read()
    code = makeCode(data, '#000000')
    grid.paste(code, (i * block_size, j * block_size))

grid.save(f'output/wonka_bar_small.png', dpi = (dpi, dpi))
