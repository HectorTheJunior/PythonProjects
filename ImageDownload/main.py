import requests
import os


def get_extensions(image_url: str) -> str | None:
    extensions: list[str] = ['.apng', '.avif', '.gif', '.jpg', '.jpeg', '.jfif', '.pjpeg',
                             '.pjp', 'png', '.svg', '.webp']

    for ext in extensions:
        if ext in image_url:
            return ext


def download_image(image_url: str, name: str, folder: str = None):
    if ext := get_extensions(image_url):
        if folder:
            image_name: str = f'{folder}/{name}{ext}'
        else:
            image_name: str = f'{name}{ext}'
    else:
        raise Exception("Image extension could not be located.")
  
  #Check if the name is not in use. Otherwise your existing photo will be overwritten.
    if os.path.isfile(image_name):
        raise Exception("This name is already in use.")

    try:
        image_content: bytes = requests.get(image_url).content
        with open(image_name, 'wb') as image:
            image.write(image_content)
            print(f'You have just downloaded: {image_name}')
    except Exception as e:
        print(f"Error: {e}")


def main():
    input_url: str = input("Enter your url: \n")
    input_name: str = input("What would you like to call your image?:\n")
    print("Downloading...")
# Here you can change 'folder' from 'None' to your actual folder path for example 'images'
    download_image(image_url=input_url, name=input_name, folder=None)


main()
