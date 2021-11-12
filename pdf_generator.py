"Generates a pdf with envelopes images filled with people data."
import csv
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

def load_data(file):
    "Loads the csv file."
    with open(file, 'r', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=";", quoting=csv.QUOTE_ALL)
        return list(reader)

def months_pixels_coords():
    "Generates the pixels coordinates for the months table."
    return [(175 + (i * 130), 1180) for i in range(13)]

def generate_pdf_without_saving_images(people_data, file_name):
    "Generates the pdf file with the envelope images fill with people data."
    font = ImageFont.truetype('arial.ttf', 30)
    images = []
    m_pixels = months_pixels_coords()
    for data in people_data:
        person_id, name, phone = data
        for i in range(13):
            with Image.open('envelope_template.png') as png_image:
                pencil = ImageDraw.Draw(png_image)
                pencil.text((190, 630), fill="#000", font=font, text=name)
                pencil.text((190, 760), fill="#000", font=font, text=phone)
                pencil.text((480, 880), fill="#000", font=font, text=person_id)
                pencil.text((1220, 880), fill="#000", font=font, text="2021")
                pencil.text(m_pixels[i], fill="#000", font=font, text="X")
                tmp = BytesIO()
                png_image.save(tmp, format='png')
                images.append(tmp)
    images = [Image.open(img).convert('RGB') for img in images]
    first_image = images.pop(0)
    first_image.save(file_name)
    first_image.close()
    for image in images:
        image.save(file_name, append=True)
        image.close()

def generate_pdf_saving_images(people_data, file_name):
    "Generates the pdf by saving images before creating pdf file."
    font = ImageFont.truetype('arial.ttf', 30)
    m_pixels = months_pixels_coords()
    tmp_file_counter = 0
    print(" -- Generating images -- ")
    for data in people_data:
        person_id, name, phone = data
        for i in range(13):
            tmp_file_counter += 1
            with Image.open('envelope_template.png') as png_image:
                pencil = ImageDraw.Draw(png_image)
                pencil.text((190, 630), fill="#000", font=font, text=name)
                pencil.text((190, 760), fill="#000", font=font, text=phone)
                pencil.text((480, 880), fill="#000", font=font, text=person_id)
                pencil.text((1220, 880), fill="#000", font=font, text="2021")
                pencil.text(m_pixels[i], fill="#000", font=font, text="X")
                png_image.save(f'/tmp/{tmp_file_counter}.png')

    print(" -- Generating PDF file -- ")
    images = [Image.open(f'/tmp/{file_number}.png').convert('RGB')
                            for file_number in range(1, tmp_file_counter + 1)]
    images[0].save(file_name, save_all=True, append_images=images[1:])

    print(" -- Closing all images -- ")
    for image in images:
        image.close()

if __name__ == '__main__':
    csv_data = load_data("fake_data.csv")
    generate_pdf_saving_images(csv_data, 'envelopes.pdf')
