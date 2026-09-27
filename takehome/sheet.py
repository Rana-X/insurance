import sys, glob
from PIL import Image
name, start, end = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
files = [f"build/{name}-{i:02d}.png" for i in range(start, end+1)]
imgs = [Image.open(f) for f in files if __import__('os').path.exists(f)]
w, h = imgs[0].size
cols = min(3, len(imgs)); rows = (len(imgs)+cols-1)//cols
sheet = Image.new("RGB", (cols*w, rows*h), "white")
for k, im in enumerate(imgs):
    sheet.paste(im, ((k%cols)*w, (k//cols)*h))
sheet.save(f"build/sheet-{name}-{start}-{end}.png")
print(f"build/sheet-{name}-{start}-{end}.png", sheet.size)
