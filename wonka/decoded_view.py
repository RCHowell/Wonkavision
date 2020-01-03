from PIL import Image, ImageDraw

width = 16 # width of grid
height = 11 # height of grid
block_size = 75
# Grid to compose images onto
grid = Image.new('RGB', (width * block_size, height * block_size))


for i in range(0, height):
  for j in range(0, width):
    n = i * width + j + 1
    filename = f'./assets/frames/compressed/{n}.png'
    data = Image.open(filename, 'r')
    grid.paste(data, (j * block_size, i * block_size))

grid.save(f'./output/decoded.png')
