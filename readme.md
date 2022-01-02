#Qtile Installation Tool

Este scipt instala mis configuraciones de qtile, hay ciertas partes las cuales no las instala el script, pero te dejo los pasos a seguir por aquí.

> **_El Script esta hecho en Python con la librería Os Por lo que deberas instalar python para ejecutar el script._**

>**El script solo funciona en archlinux, si quieres ejecutarlo en otro Sistema Operativo que no este basado en archlinux, tendrás que cambiar la línea de código **`os.system('sudo pacman -S git python-psutil neovim zsh alacritty rofi curl udiskie feh thunar xorg-xinit pulseaudio')`** por el gestor de paquetes de tu distribución, por ejemplo si usas una distribución de GNU/Linux basada en debian usarás el `apt` si usas fedora usarás `dnf` y así con las demás** 

####Si usas archlinux, puedes ignorar el paso anterior.

> *Para instalar el script tendrás que seguir estos pasos:*
* `sudo pacman -S python`
* `git clone https://github.com/Nimeavles/Qtile-installation-tool /home/$USER/script-qtile`
* `cd /home/$USER/script-qtile`
* `python3 script.py`
>Automáticamente se te desplegará este menú en un programa de CLI:
![image](/home/nimeavles/script/img.png)

>*Una vez completes el script, puedes seguir con la perzonalización pero de forma manual. **El script instala zsh con mis configuraciones, qtile y mis configuraciones, la fuente Ubuntu Nerd Font, rofi con una configuracion copiada de `Antonio Sarosi` y un xsession con permisos de ejecución.** Para instalar temas puedes ir a este sitio web creado por gnome y descargar el tema gtk con sus iconos que desees, el enlace es este:*

* `https://www.gnome-look.org/browse?cat=135`

> En esa web puedes descargar el tema que quieras, una vez instalado, tendrás que descomprimir el .zip :

* `sudo pacman -S zip unzip`
* `cd /directorio/donde/hayas/descargado/el/zip`
* `unzip nombredelzip.zip`
* `sudo cp -r carpetaDescomprimida /usr/share/themes`

> El mismo procedimiento debes de hacer para los iconos con la exepción de que tienes que copiar la carpeta descomprimida en `/usr/share/icons` y tendrías instalado los temas, pero eso no es todo, también tendrás que crear unos archivos que te he dejado en mi repocitorio de github `https://github.com/Nimeavles/Dotfiles`, aquí encontrarás una carpeta llamada `gtk-3.0` que dentro contiene un archivo llamado `settings.ini`, pues esa carpeta la tienes que copiar a `/home/$USER/.config` en ese archivo, tendrás que cambiar las 2 primeras líneas y ponerle el nombre de el tema que has descargado en la primera línea, y si has descargado iconos también **(recomendable)**  pues en la 2º línea pones el nombre del tema de los iconos.

> Luego hay otro archivo llamado `.gtk-rc2.0` el cual lo tienes que copiar en `/home/$USER/` en el cual tendrás que cambiar las dos primeras líneas de código y cambiarla por el nombre de vuestro tema y iconos. Con eso terminaría el tema del `gtk`.

>Por último tienes que descargar un fondo de pantalla y ponerlo el archivo `.xsession` ubicado en /home/$USER. Hay una línea de código que dice `feh --bg-scale wallpapers/fondo1.jpg &` ahí tendrás que cambiar la ruta del archivo de el fondo de pantalla.