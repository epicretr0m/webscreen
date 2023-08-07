import argparse
import requests
from colorama import Fore, Style, init

def print_banner():
    banner = """
╦ ╦╔═╗╔╗ ╔═╗╔═╗╦═╗╔═╗╔═╗╔╗╔
║║║║╣ ╠╩╗╚═╗║  ╠╦╝║╣ ║╣ ║║║
╚╩╝╚═╝╚═╝╚═╝╚═╝╩╚═╚═╝╚═╝╝╚╝
    """
    print(Fore.CYAN + banner + Style.RESET_ALL)

def capture_screenshot(url, filename, access_key):
    base_url = "https://api.screenshotone.com/take"
    api_url = f"{base_url}?url={url}&access_key={access_key}"
    
    response = requests.get(api_url)
    
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(Fore.GREEN + f"Capture d'écran enregistrée sous le nom '{filename}'" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Erreur lors de la capture d'écran:", response.text + Style.RESET_ALL)

if __name__ == "__main__":
    init(autoreset=True)
    print_banner()
    
    parser = argparse.ArgumentParser(description="Capture d'écran d'un site web")
    parser.add_argument("-u", "--url", required=True, help="URL du site web")
    parser.add_argument("-n", "--filename", required=True, help="Nom du fichier de capture d'écran")
    args = parser.parse_args()
    
    url = args.url
    filename = args.filename
    access_key = "YOUR_API_KEY"
    
    capture_screenshot(url, filename, access_key)
