from PIL import Image
import time

# Load the original image
original_image = Image.open('chapter1.png')
width, height = original_image.size

# Generate a random number
current_time = int(time.time())
generated_number = (current_time % 100) + 50
if generated_number % 2 == 0:
    generated_number += 10

modified_image = Image.new('RGB', (width, height))
for x in range(width):
    for y in range(height):
        r, g, b = original_image.getpixel((x, y))
        r_new = min(r + generated_number, 255)
        g_new = min(g + generated_number, 255)
        b_new = min(b + generated_number, 255)
        modified_image.putpixel((x, y), (r_new, g_new, b_new))

modified_image.save('chapter1out.png')
red_sum = sum(r for r, _, _ in modified_image.getdata())
print(red_sum)


