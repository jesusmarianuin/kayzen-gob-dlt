# Añadir otro repositorio de GitHub como submodule

## 1. Añadir el submodule

Desde la raíz del repositorio:

```bash
git submodule add <url-del-repo> subrepos/nombre-repo
```

O, mucho mejor, si quieres elegir la carpeta y que el nombre sea el mismo que se crearía al clonar, sitúate en la carpeta concreta y clona:

```bash
cd knowledge-base/isbe
git submodule add <url-del-repo>
```

Esto clona el otro repo dentro de la carpeta indicada (`subrepos/nombre-repo` en el primer caso, `knowledge-base/isbe/nombre-repo` en el segundo) y crea o actualiza el archivo `.gitmodules` con esa información.

## 2. Confirmar el cambio en tu repo principal

Desde la raíz del repositorio:

```bash
git add .gitmodules knowledge-base/isbe/nombre-repo
git commit -m "chore: add nombre-repo submodule"
git push
```

Esto es importante: añadir el submodule no basta, hay que hacer commit para que quede registrado.

## Clonar un repo que ya tiene submodules

Para quien clone tu repo después (o tú mismo en otro PC):

```bash
git clone --recurse-submodules <tu-repo-principal>
```

Si ya lo clonaste sin esa opción, las carpetas de los submodules aparecerán vacías. Para rellenarlas, desde la raíz del repositorio:

```bash
git submodule update --init --recursive
```
