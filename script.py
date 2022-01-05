import os, time
from sys import stdout

def red():
    RED = "\033[1;31m"
    stdout.write(RED)

def green():
    GREEN = "\033[0;32m"
    stdout.write(GREEN)

def blue():
    BLUE = "\033[1;34m"
    stdout.write(BLUE)

def yellow():
    YELLOW = "\033[1;33m"
    stdout.write(YELLOW)

def purple():
    PURPLE = "\033[1;35m"
    stdout.write(PURPLE)

def white():
    WHITE = "\033[1;37m"
    stdout.write(WHITE)


intro = '''    
      _  _  _  _         _  _  _  _  _           _  _  _           _                    _  _  _  _  _    
    _(_)(_)(_)(_)_      (_)(_)(_)(_)(_)         (_)(_)(_)         (_)                  (_)(_)(_)(_)(_)   
   (_)          (_)           (_)                  (_)            (_)                  (_)               
   (_)          (_)           (_)                  (_)            (_)                  (_) _  _          
   (_)     _    (_)           (_)                  (_)            (_)                  (_)(_)(_)         
   (_)    (_) _ (_)           (_)                  (_)            (_)                  (_)               
   (_)_  _  _(_) _            (_)                _ (_) _          (_) _  _  _  _       (_) _  _  _  _    
     (_)(_)(_)  (_)           (_)               (_)(_)(_)         (_)(_)(_)(_)(_)      (_)(_)(_)(_)(_)   

'''

def menu():
    red()
    print(intro)
    yellow()
    time.sleep(1)
    print('- Instalar mis configuraciones\n')
    time.sleep(1)
    print('- Salir\n')
    time.sleep(1)
    blue()
    opcion= int(input('¿Que quieres hacer?-> 1|2 -> '))
    if opcion == 1:
        green()
        instalar()
    elif opcion == 2:
        green()
        print('Has salido con éxito')
        exit()

def instalar():
    os.system('sudo pacman -S git python-psutil neovim zsh alacritty rofi curl udiskie feh thunar xorg-xinit pulseaudio exa bat')
    os.system('git clone https://github.com/Nimeavles/Dotfiles /home/$USER/dotfiles-nimeavles')
    os.system('cd /home/$USER/dotfiles-nimeavles')
    os.system('rm -r /home/$USER/.config/qtile')
    os.system('cp -r qtile/ /home/$USER/.config')
    os.system('cp -r alacritty/ /home/$USER/.config')
    os.system('cp -r rofi /home/$USER/.config')
    os.system('git clone https://github.com/ryanoasis/nerd-fonts /home/$USER/fonts')
    os.system('cd /home/$USER/fonts')
    os.system('./install.sh UbuntuMono')
    os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
    os.system('git clone https://github.com/romkatv/powerlevel10k.git ~/$ZSH_CUSTOM/themes/powerlevel10k')
    os.system('rm /home/$USER/.zshrc')
    os.system('git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting')
    os.system('git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions')
    os.system('cp .zshrc /home/$USER')
    os.system('cp .xsession /home/$USER')
    os.system('chmod u+x /home/$USER/.xsession')

menu()
