# Cómo incluir nombres y dos apellidos españoles compuestos en el PID (DIP) de la Cartera IDUE (EUDI Wallet)

Post: <https://inza.blog/2026/09/17/como-incluir-nombres-y-dos-apellidos-espanoles-compuestos-en-el-pid-dip-de-la-cartera-idue-eudi-wallet/>

Fecha: 2026-09-17

El PID, definido en el [CIR 2024/2977](https://eur-lex.europa.eu/eli/reg_impl/2024/2977/oj/spa) y en el [PID Rulebook](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/latest/annexes/annex-3/annex-3.01-pid-rulebook/) del [ARF 3.0](https://eudi.dev/3.0.0/), tiene un único campo `family_name` de texto libre. Con dos apellidos que pueden ser compuestos, "García de la Torre Martín" no se puede descomponer sin ambigüedad. Eso afecta, por ejemplo, al cotejo transfronterizo de identidades ([CIR 2025/846](https://eur-lex.europa.eu/eli/reg_impl/2025/846/oj/spa)).

La propuesta separa la presentación de la estructura:

- `family_name` conserva la forma natural del nombre
- Como solución provisional, la estructura viaja en banda con una barra inclinada entre el primer y el segundo apellido, normalizada en NFC y con escape por porcentaje; la barra sobrevive a CBOR y JSON y, si no se interpreta, se lee sin problema
- Como solución definitiva, un subcampo `family_name_unit` con `first` y `second`, divulgable por separado, con ejemplos en mdoc, [SD-JWT VC](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/) y W3C VC

El post analiza la zona de lectura mecánica de los pasaportes ([ICAO Doc 9303](https://www.icao.int/sites/default/files/publications/DocSeries/9303_p3_cons_en.pdf)), que tiene la misma ambigüedad. Pide que el Rulebook incorpore subcampos de nombre por posición, no por linaje, con reglas de normalización y un perfil español.

En una frase: el PID no distingue los dos apellidos españoles, y el post propone una barra provisional y subcampos estructurados en el Rulebook.

---
