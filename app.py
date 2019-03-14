import requests
from bs4 import BeautifulSoup
import csv


page = requests.get('http://www3.santoandre.sp.gov.br/defesacivil/monitoramento-rios-corregos/')
soup = BeautifulSoup(page.content, 'html.parser')
cameras = soup.find_all("div", {"class": "corrego"})
cameras_list = []

for camera in cameras:
    titulo = camera.find("p").text
    details = camera.find("div")
    image = details.find("img")
    img_str = str(image.attrs['src']).split("?")[0]
    cameras_list.append({'camera': f'{titulo}', 'imagem': f'{img_str}'})

    # print("Camera: ", titulo)
    # print("Link:   ", img_str)

opcao=True
while opcao:
    print("Cameras Disponíveis:")
    print("====================")

    for opc, cam in enumerate(cameras_list):
        print(opc, cam['camera'])

    print(opc + 1, "TODAS")

    opcao=input("Escolha uma opção? ")

    if opcao == str(opc + 1):
        print(cameras_list)
    else:
        print(cameras_list[int(opcao)])