import os
import requests
from colorama import Fore, Style
from urllib.parse import urlparse
from bs4 import BeautifulSoup

os.system('cls' if os.name == 'nt' else 'clear')

def get_unique_filename(filename):
    base_name, extension = os.path.splitext(filename)
    counter = 1
    unique_filename = filename
    while os.path.exists(unique_filename):
        unique_filename = f"{base_name}_{counter}{extension}"
        counter += 1
    return unique_filename

def extract_websites_from_zone_xsec():
    url_template = 'https://zone-xsec.com/archive/page={}'

    first_page = int(input('\n' + Fore.GREEN + "Enter the first page number: "))
    last_page = int(input('\n' + Fore.GREEN + "Enter the last page number: "))

    urls = []
    for page in range(first_page, last_page + 1):
        url = url_template.format(page)
        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        for text in soup.stripped_strings:
            if '.' in text:
                if not text.startswith('http://') and not text.startswith('https://'):
                    text = 'http://' + text
                parsed_url = urlparse(text)
                domain_name = parsed_url.netloc.split(':')[0]
                domain_parts = domain_name.split('.')
                if len(domain_parts) >= 2:
                    tld = domain_parts[-1]
                    if len(tld) <= 3:
                        domain_name = '.'.join(domain_parts[-2:])
                    else:
                        domain_name = '.'.join(domain_parts[-3:])
                if domain_name not in urls:
                    urls.append(domain_name)
                    print('\n' + Fore.MAGENTA + "Extracted domain: " + Style.RESET_ALL.format(domain_name))

    output_file = 'zonexecweb.txt'
    output_file = get_unique_filename(output_file)

    with open(output_file, 'w') as file:
        for url in urls:
            file.write(url + '\n')

    print(f"Grabbing completed! Results are stored in '{output_file}'")

def extract_websites_from_zone_h():
    phpssid = input('\n' + Fore.GREEN + "Enter the PHPSESSID: ")
    zhe_cookie = input('\n' + Fore.GREEN + "Enter the ZHE cookie: ")
    number_of_pages = int(input('\n' + Fore.GREEN + "Enter the number of pages: "))

    cookie = {"ZHE": zhe_cookie, "PHPSESSID": phpssid}

    nfrs = []

    print("Fetching notifiers from 'https://zone-h.org/archive/published=0/page=', please wait...")

    for page_number in range(number_of_pages):
        response = requests.get('https://zone-h.org/archive/published=0/page=' + str(page_number + 1), cookies=cookie).content

        if 'If you often get this captcha when gathering data' in response.decode('utf-8'):
            input("\nPlease verify the CAPTCHA and then press 'Enter'.")
            response = requests.get('https://zone-h.org/archive/published=0/page=' + str(page_number + 1), cookies=cookie).content

        soup = BeautifulSoup(response, 'html.parser')
        links = soup.findAll('a')

        for link in links:
            href = link.get('href')
            if href and '/archive/notifier=' in href:
                notif = href.split('/archive/notifier=')[1].split('">')[0]
                if notif not in nfrs:
                    nfrs.append(notif)
                    open('notifiers.txt', 'a+').write(notif + '\n')

    print('Total notifiers:', len(nfrs))

    sts = []

    for notifier in nfrs:
        print('Grabbing sites from:', notifier)

        for page_number in range(50):
            response = requests.get('http://www.zone-h.org/archive/notifier=' + notifier + '/page=' + str(page_number + 1), cookies=cookie).content

            if 'If you often get this captcha when gathering data' in response.decode('utf-8'):
                input("\nPlease press 'Enter' after verifying the CAPTCHA")
                response = requests.get('http://www.zone-h.org/archive/notifier=' + notifier + '/page=' + str(page_number + 1), cookies=cookie).content

            soup = BeautifulSoup(response, 'html.parser')
            links = soup.findAll("td", {"class": "defacepages"})

            if '<strong>0</strong>' in str(links[0]):
                break
            else:
                response = response.decode('utf-8')
                pages = re.findall('<td>(.*)\n							</td>', response)

                for page in pages:
                    new_url = 'http://' + str(page.split('/')[0])

                    if new_url not in sts:
                        sts.append(new_url)
                        retless = '\t\t' + new_url
                        open('zonehWeb.txt', 'a+').write(new_url + '\n')
                        print('\n' + Fore.CYAN + retless + Style.RESET_ALL)

    output_file = 'zonehWeb.txt'
    output_file = get_unique_filename(output_file)

    with open(output_file, 'w') as file:
        for url in sts:
            file.write(url + '\n')

    print(f"Grabbing completed! Results are stored in '{output_file}'")

def main():
    banner = '''
=======================================================================
  _____                  _____           _     
 |  __ \                / ____|         | |    
 | |__) |_      ___ __ | |  __ _ __ __ _| |__  
 |  ___/\ \ /\ / / '_ \| | |_ | '__/ _` | '_ \ 
 | |     \ V  V /| | | | |__| | | | (_| | |_) |
 |_|      \_/\_/ |_| |_|\_____|_|  \__,_|_.__/ 
=======================================================================                                             
[+] Hit-List Scraper | SICARIO 2023 | 1337 [+] 
-----------------------------------------------------------------------                                      
'''
    menu = '''
[1] Extract websites from Zone-Xsec
[2] Extract websites from Zone-H
'''

    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED + banner + Style.RESET_ALL)
    print(Fore.YELLOW + menu + Style.RESET_ALL)

    try:
        ztbot = input('\n' + Fore.GREEN + "Enter the option (1 or 2): ")

        if ztbot == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.RED + banner + Style.RESET_ALL)
            extract_websites_from_zone_xsec()
        elif ztbot == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.RED + banner + Style.RESET_ALL)
            extract_websites_from_zone_h()
        else:
            print("\n\t\t[!] This is the wrong number")

    except KeyboardInterrupt:
        print('\n\nKeyboardInterrupt: Stopping the execution.')

if __name__ == '__main__':
    main()

