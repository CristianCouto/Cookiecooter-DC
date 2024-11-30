# Aqui se alojan los comandos para .gitignore - Equipo Newsan2

## Para ignorar la carpeta interim se utilizó
data/interim/
# Se elimina del control de versiones mientras se mantiene en el disco local
git rm -r --cached data/interim/
# Un commit para aplicar los cambios en el repositorio
git add .gitignore
git commit -m "Ignorar la carpeta interim"
# Se suben los cambios a GitHub
git push origin main