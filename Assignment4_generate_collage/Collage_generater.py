#!/usr/bin/env python
# coding: utf-8

# In[45]:


import requests
from PIL import Image
from io import BytesIO

API_KEY = '6AUPv90T0JfvcB5HoIuo95PCOei9eqjhjsRor6HqFWpvm6c21yyoHRrt'
BASE_URL = 'https://api.pexels.com/v1/'

def fetch_image_urls(keyword, num_images=5):
    api_key=API_KEY
    headers = {'Authorization': api_key}
    params = {'query': keyword, 'per_page': num_images}
    response = requests.get(BASE_URL + 'search', headers=headers, params=params)
    data = response.json()
    photo_urls = [photo['src']['large'] for photo in data.get('photos', [])]
    return photo_urls

def download_images(urls):
    images = []
    for url in urls:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        images.append(img)
    return images

def resize_images(images, target_width, target_height=None):
    resized_images = []
    for img in images:
        aspect_ratio = img.width / img.height
        new_height = int(target_width / aspect_ratio) if target_height is None else target_height
        img_resized = img.resize((target_width, new_height), Image.ANTIALIAS)
        resized_images.append(img_resized)
    return resized_images

def create_collage(images, num_images_per_row=3, spacing=10):
    num_images = len(images)
    rows = (num_images + num_images_per_row - 1) // num_images_per_row
    width, height = images[0].size
    collage_width = width * num_images_per_row + spacing * (num_images_per_row - 1)
    collage_height = height * rows + spacing * (rows - 1)
    collage = Image.new('RGB', (collage_width, collage_height), (255, 255, 255))
    
    for i in range(rows):
        for j in range(num_images_per_row):
            index = i * num_images_per_row + j
            if index < num_images:
                x = j * (width + spacing)
                y = i * (height + spacing)
                collage.paste(images[index], (x, y))
    
    return collage

def main():
    keyword = 'nature'
    num_images = 6
    resize_width = 500

    image_urls = fetch_image_urls(keyword, num_images=num_images)
    print(f"Fetched {len(image_urls)} image URLs for {keyword}")
    
    images = download_images(image_urls)
    print(f"Downloaded {len(images)} images for {keyword}")

    resized_images = resize_images(images, target_width=resize_width)
    print(f"Resized {len(resized_images)} images for {keyword}")

    collage = create_collage(resized_images, spacing=10)
    collage.show()

if __name__ == "__main__":
    main()


# In[ ]:




