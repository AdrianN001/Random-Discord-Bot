import requests
from PIL import Image
from io import BytesIO
import numpy
import math


def clamp(num: int, min_value: int, max_value: int) -> int:
   return max(min(num, max_value), min_value)

MAX_SIZE = 140,110
MAX_VALUE = 255 * 3
BASE_CHARACTERS = ".,-~`*^)&%$#@0"

class Ascii_Image:
    img:    Image.Image
    pixels: list[list[tuple]]
    characters: str 

    def __init__(self, source, character:str = ".,-~`*^)&%$#@"): 
        
        self.source = source 

        self.characters = character

        self.img = Image.open(requests.get(source, stream=True).raw)
        print(self.img.getdata())
   
    def __resize_image(self) -> None:
        self.img.thumbnail(MAX_SIZE, Image.Resampling.LANCZOS)

        #self.img = self.img.resize((50,280))
        


    # @staticmethod()
    # def __get_aspect_ratio(image: Image) -> float: 
    #     width, height = image.size
    #     #e.g 1920, 1080 => 1920/1080 = 16/9 
    #     return width / height


   
    def __get_pixels(self) -> None: 
        # if type(list(self.img.getdata())[0]) == int:  
        #     self.img = self.img.convert("RGB")

        pixels = list(self.img.getdata())
        width, height = self.img.size
        pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
        self.pixels = pixels
    
    def __pixel_to_characters(self) -> None: 

        res = [[]] 

        for row in self.pixels:
            
            for pixl in row: 
                pixl = pixl[:2] 

                val = sum(pixl)
                print(val)

                for offset in range(self.characters.__len__()):
                    if val == clamp(val, offset * (MAX_VALUE // self.characters.__len__()) , (offset+ 1) * (MAX_VALUE // self.characters.__len__())) :

                        res[-1].append(self.characters[offset])
                        print("NIGGER")
                        break
                
            res.append([]) # line break
        print(res)
        self.result = res
        


    def create_file(self) -> list:
        ...
        self.__resize_image()
        #ratio = __get_aspect_ratio(self.img)
        self.__get_pixels()

        self.__pixel_to_characters()

        with open("src/temp.txt", "w") as file: 
            
            for row in self.result:
                file.write( "".join(row))
                file.write("\n")
            


if __name__ == "__main__":
    x = Ascii_Image("https://leetcode.com/_next/static/images/logo-dark-c96c407d175e36c81e236fcfdd682a0b.png")
    x.convert()