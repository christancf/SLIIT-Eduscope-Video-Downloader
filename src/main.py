import requests
import json
import m3u8
import subprocess
import os
import sys
import configparser

from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from InquirerPy.utils import color_print


base_path = "https://lecturecapture.sliit.lk/archive/saved/Personal_Capture/"


def getPrefferedFolder():
    config = configparser.ConfigParser()
    config.optionxform = str
    config.read('../config.ini')

    folderNames = [Choice(value=0, name="[o] Default")]

    for key in config["folders"]:
        folderNames.append(Choice(value=key, name="[o] " + key))

    folderNames.append(Choice(value=None, name="[x] Exit"))

    folder = inquirer.select(
        message="\n\nSelect module folder:",
        choices=folderNames,
        default=None,
    ).execute()

    if folder == 0:
        return "./Downloads/"
    elif folder == None:
        exit()
    else:
        selectedDir = config["folders"][folder]
        if selectedDir[-1] != "\\" or selectedDir[-1] != "/":
            selectedDir = selectedDir + "\\"

        if os.path.exists(selectedDir):
            return selectedDir
        else:
            try:
                os.makedirs(selectedDir)
                return selectedDir
            except:
                color_print(formatted_text=[
                    ("gold", selectedDir),
                    ("red",  " <- Invalid Path")])
                sys.exit()


def get_actual_path(link):
    qualities = [
        Choice(value="_144.m3u8", name="[o] Low"),
        Choice(value="_360.m3u8", name="[o] High")
    ]

    selectedQuality = inquirer.select(
        message="\nSelect quality:",
        choices=qualities,
        default=None,
    ).execute()

    if(len(link) == 68):
        ID = link[-23:] + "&full=ZnVsbA%3D%3D"
    else:
        ID = link.replace("https://lecturecapture.sliit.lk/neplayer.php?", "")

    MAIN_URL = "https://lecturecapture.sliit.lk/webservice.php?key=vhjgyu456dCT&type=video_paths&"
    URL = MAIN_URL + ID

    session = requests.Session()

    response = session.get(URL, verify="..\cert.pem").text

    data = json.loads(response)

    video_path_prefix = data['video_1_m3u8_list']

    video_path_postfix = video_path_prefix.replace(
        "../../archive/saved/Personal_Capture/", "")
    main_path = base_path + \
        video_path_postfix.replace(".m3u8", "") + selectedQuality
    return main_path


def download_video(main_path, folderPath):
    requests.get(
        "https://api.countapi.xyz/hit/com.navindu.eduscope/download-start")
    char = ''

    main_path_length = len(main_path)
    count = main_path_length - 1
    url_cmp = ""

    for i in range(main_path_length):
        char = main_path[count]
        url_cmp += char
        if(char == "/"):
            break
        count -= 1

    fileNameInUrl = ""
    count_file_name = len(url_cmp) - 1

    while(count_file_name >= 0):
        fileNameInUrl += url_cmp[count_file_name]
        count_file_name -= 1

    file_path = folderPath
    url_info = main_path.replace(fileNameInUrl, " ")
    url_cmp = fileNameInUrl.lstrip("/")
    url_info = url_info.rstrip(" ")+"/"
    file_name = url_cmp.rstrip(".m3u8")
    url_1 = url_info + url_cmp
    r_1 = requests.get(url_1, verify="../cert.pem")
    m3u8_master = m3u8.loads(r_1.text)
    file_number = 0
    i = 0
    percentage = 0.0

    color_print(formatted_text=[
                ("green", "\nDownloading to: "),
                ("white",  file_path + "\n")])

    for segment in m3u8_master.data['segments']:
        file_number += 1

    with open(file_path + file_name + '.ts', 'wb') as f:
        for segment in m3u8_master.data['segments']:
            url = url_info + segment['uri']
            while(True):
                try:
                    r = requests.get(url, timeout=15, verify="..\cert.pem")
                except:
                    continue
                break

            f.write(r.content)
            i += 1
            percentage = i/file_number * 100
            # progress_bar.update(i/2)

            print(f"="*int(percentage/2), end="")
            print("[", end="")
            print(f"{(str(percentage))[0:5]} %", end="")
            # print("\r\x1b[20C[",end = "")
            print("]", end="")
            print("\r", end="")

    print("\n")
    color_print(formatted_text=[
        ("green", "\nDownload Complete!.")])

    requests.get(
        "https://api.countapi.xyz/hit/com.navindu.eduscope/download-complete")

    return file_name


def convert(file_name, file_path):
    requests.get(
        "https://api.countapi.xyz/hit/com.navindu.eduscope/convert-start")

    color_print(formatted_text=[("gold", "\nConverting to mp4... ")])

    infile = file_path + file_name+".ts"
    outfile = file_path + file_name + ".mp4"
    subprocess.run(['..\\ffmpeg', '-i', infile, outfile,
                   "-hide_banner", "-nostats", "-loglevel", "panic"])
    os.remove(file_path + file_name+".ts")

    color_print(formatted_text=[("green", "\nDownloading Complete")])

    requests.get(
        "https://api.countapi.xyz/hit/com.navindu.eduscope/convert-complete")


if __name__ == '__main__':
    requests.get("https://api.countapi.xyz/hit/com.navindu.eduscope/opens")
    link = ""
    if(len(sys.argv) == 2):
        link = sys.argv[1]
    else:
        link = str(input("Enter video link: "))

    color_print(formatted_text=[
                ("gold", "\nReady to download: "),
                ("white",  link + "\n")])

    path = get_actual_path(link)
    filePath = getPrefferedFolder()
    file = download_video(path, filePath)
    convert(file, filePath)
    sys.exit()
