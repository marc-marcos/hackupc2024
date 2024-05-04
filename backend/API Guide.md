# API Guide

### /login 

#### Campos que acepta
- `email`
- `password`

#### Campos que devuelve

### /register_invidente

#### Campos que acepta 
- `email`
- `name`
- `surname`
- `password`

### /register_vidente

#### Campos que acepta 
- `email`
- `name`
- `surname`
- `password`

### /anadir_vuelo

#### Campos que acepta

- `codigo`
- `origen`
- `destino`
- `fecha`
- `hora`

### /asociar_vuelo

#### Campos que acepta

- `email`
- `codigo`

### /ayudar

Esta llamada devuelve dado un email, todos las personas que puede ayudar (personas invidentes con las que comparte un vuelo).

#### Campos que acepta

- `email`

### /ofrecer_ayuda

#### Campos que acepta

- `email_vidente`
- `email_no_vidente`
- `codigo`

### Pedir ayuda

#### Campos que acepta 

- `email`
- `codigo`