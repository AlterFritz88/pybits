import re
output = """
                                       mohh@SERENiTY
 MMMMMMMMMMMMMMMMMMMMMMMMMmds+.        OS: Mint 19 tara
 MMm----::-://////////////oymNMd+'     Kernel: x86_64 Linux 4.15.0-34-generic
 MMd      /++                -sNMd:    Uptime: 1d 4m
 MMNso/'  dMM    '.::-. .-::.' .hMN:   Packages: 2351
 ddddMMh  dMM   :hNMNMNhNMNMNh: 'NMm   Shell: zsh 5.4.2
     NMm  dMM  .NMN/-+MMM+-/NMN' dMM   Resolution: 1366x768
     NMm  dMM  -MMm  'MMM   dMM. dMM   DE: Cinnamon 3.8.9
     NMm  dMM  -MMm  'MMM   dMM. dMM   WM: Muffin
     NMm  dMM  .mmd  'mmm   yMM. dMM   WM Theme: Linux Mint (Mint-Y)
     NMm  dMM'  ..'   ...   ydm. dMM   GTK Theme: Mint-Y [GTK2/3]
     hMM- +MMd/-------...-:sdds  dMM   Icon Theme: Mint-Y
     -NMm- :hNMNNNmdddddddddy/'  dMM   Font: Noto Sans 9
      -dMNs-''-::::-------.''    dMM   CPU: AMD A10-7400P Radeon R6, 10 Compute Cores 4C+6G @ 4x 2.5GHz [101.0°C]
       '/dMNmy+/:-------------:/yMMM   GPU: AMD KAVERI (DRM 2.50.0 / 4.15.0-34-generic, LLVM 6.0.0)
          ./ydNMMMMMMMMMMMMMMMMMMMMM   RAM: 1886MiB / 6915MiB
             \.MMMMMMMMMMMMMMMMMMM    
"""


def sysinfo_scrape(output):
    """Scrapes the output from screenfetch and returns a dictionary"""
    lines = []
    for line in output.split('\n'):
        lines.append(re.findall(r'\s\s\s[A-Za-x]+\s[A-Za-x]+:\s[a-zA-Z|\d].*', r'{}'.format(line)))
        lines.append(
           re.findall(r'\s\s\s[A-Za-z]+:\s[a-zA-Z|\d].*', r'{}'.format(line)))
        lines.append(re.findall(r'[A-Za-x]+@[A-Za-x]+', r'{}'.format(line)))
    lines = [x[0] for x in lines if x != []]
    answer = {}
    for item in lines:
        if re.findall(r'[A-Za-x]+@[A-Za-x]+', r'{}'.format(item)) != []:
            answer['Name'] = item
        else:
            item = item.split(': ')
            answer[item[0][3:]] = item[1]
    return answer



print(sysinfo_scrape(output))