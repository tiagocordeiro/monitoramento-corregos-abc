import requests
from bs4 import BeautifulSoup
import csv


page = requests.get('http://www3.santoandre.sp.gov.br/defesacivil/monitoramento-rios-corregos/')
soup = BeautifulSoup(page.content, 'html.parser')
cameras = soup.find_all("div", {"class": "corrego"})

for camera in cameras:
    titulo = camera.find("p").text
    details = camera.find("div")
    image = details.find("img")
    img_str = str(image.attrs['src']).split("?")[0]

    print("Camera: ", titulo)
    print("Link:   ", img_str)
