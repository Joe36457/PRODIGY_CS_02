from PIL import Image
import random

class ImageShuffler:
    def __init__(self, image_path):
        self.img = Image.open(image_path)
        self.width, self.height = self.img.size
        self.pixel_count = self.width * self.height
        self.key = list(range(self.pixel_count))
        random.shuffle(self.key)

    def encrypt(self, output_path):
        pixels = list(self.img.getdata())
        swapped_pixels = [None] * self.pixel_count
        for i in range(self.pixel_count):
            swapped_pixels[self.key[i]] = pixels[i]
        self.img.putdata(swapped_pixels)
        self.img.save(output_path)

    def decrypt(self, output_path):
        inverted_key = sorted(range(len(self.key)), key=lambda k: self.key[k])
        pixels = list(self.img.getdata())
        swapped_pixels = [None] * self.pixel_count
        for i in range(self.pixel_count):
            swapped_pixels[inverted_key[i]] = pixels[i]
        self.img.putdata(swapped_pixels)
        self.img.save(output_path)

# Example usage
image_shuffler = ImageShuffler(r'C:\Users\Admin\Desktop\Prodigy\pythonProject7\ACMirage_BasimLandscape.png')

image_shuffler.encrypt(r'C:\Users\Admin\Desktop\Prodigy\pythonProject7\encrypted_image.png')
image_shuffler.decrypt(r'C:\Users\Admin\Desktop\Prodigy\pythonProject7\decrypted_image.png')
