"Do the job."
import csv
from PIL import Image, ImageDraw, ImageFont


def load_data(file):
    "Loads the file."
    with open(file, 'r', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=";", quoting=csv.QUOTE_ALL)
        return list(reader)

def write_image(info):
    "Do the image job."
    font = ImageFont.truetype('arial.ttf', 30)
    for index, data in enumerate(info):
        try:
            with Image.open('dizimo.png') as im:
                pencil = ImageDraw.Draw(im)
                pencil.text((190, 630), fill="#000", font=font, text=data[1])
                pencil.text((190, 760), fill="#000", font=font, text=data[2])
                pencil.text((480, 880), fill="#000", font=font, text=data[0])
                pencil.text((1220, 880), fill="#000", font=font, text="2021")
                im.save(f'{index}.png')
        except OSError:
            print("ooops")



if __name__ == '__main__':
    l = [Image.open(f'{i}.png') for i in range(100)]
    c = [i.convert('RGB') for i in l]
    c[0].save('uhet.pdf', save_all=True, append_images=c)
