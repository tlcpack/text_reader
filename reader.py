from PIL import Image, ImageEnhance
import pytesseract

img = Image.open('image_test/amer_amnesia.jpg')

enhancer1 = ImageEnhance.Sharpness(img)
enhancer2 = ImageEnhance.Contrast(img)
img_edit = enhancer1.enhance(20.0)
img_edit = enhancer2.enhance(1.5)

img_edit.save("edited_image.png")

result = pytesseract.image_to_string(img_edit)

with open('text2.txt', mode='w') as file:
    file.write(result)
    print("ready!")