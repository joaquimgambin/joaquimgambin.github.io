# Configuración de WordPress para el Currículum Web de Joaquim Gambín

Este documento proporciona instrucciones detalladas para configurar una versión WordPress de tu currículum web, permitiéndote realizar actualizaciones fácilmente.

## Requisitos previos

1. Un servicio de hosting que soporte WordPress (recomendados: Hostinger, SiteGround, Bluehost)
2. Un dominio (puedes usar un subdominio gratuito o comprar uno personalizado)
3. Acceso a cPanel o panel de administración similar

## Pasos para la instalación

### 1. Configuración del hosting

1. Regístrate en un servicio de hosting (muchos ofrecen planes gratuitos o económicos)
2. Accede al panel de control (generalmente cPanel)
3. Busca la sección "Instaladores de aplicaciones" o "WordPress"
4. Sigue el asistente de instalación de WordPress

### 2. Selección de tema

Para mantener la apariencia actual de tu currículum web, recomiendo estos temas minimalistas:
- Astra
- OceanWP
- GeneratePress
- Sydney

Pasos para instalar un tema:
1. Accede al panel de WordPress (`tudominio.com/wp-admin`)
2. Ve a "Apariencia" > "Temas" > "Añadir nuevo"
3. Busca uno de los temas recomendados
4. Haz clic en "Instalar" y luego en "Activar"

### 3. Estructura de páginas

Crea las siguientes páginas para mantener la estructura actual:
1. Inicio
2. Experiencia
3. Desarrollos
4. Formación
5. Contacto

Para crear una página:
1. Ve a "Páginas" > "Añadir nueva"
2. Asigna el título correspondiente
3. Usa el editor de bloques para añadir contenido
4. Publica la página

### 4. Menú de navegación

1. Ve a "Apariencia" > "Menús"
2. Crea un nuevo menú
3. Añade todas las páginas creadas
4. Asigna el menú a la posición "Menú principal"

### 5. Personalización

1. Ve a "Apariencia" > "Personalizar"
2. Ajusta los colores para mantener la paleta de azules:
   - Color primario: #2b5797
   - Color secundario: #1e3c6e
   - Color de acento: #4a7ac2
3. Sube el logo CET en la sección "Identidad del sitio"
4. Configura la página de inicio como página principal

### 6. Formulario de contacto

1. Instala el plugin "Contact Form 7" o "WPForms Lite"
2. Crea un formulario con los campos: Nombre, Email, Asunto y Mensaje
3. Añade el formulario a la página de Contacto usando el shortcode proporcionado

## Migración de contenido

Para transferir el contenido actual a WordPress:

1. Copia el texto de cada página HTML
2. Pégalo en el editor de la página correspondiente en WordPress
3. Sube las imágenes (logo y foto de perfil) a la biblioteca multimedia
4. Inserta las imágenes en las ubicaciones apropiadas

## Actualizaciones futuras

Para actualizar tu currículum web:

1. Accede al panel de WordPress
2. Ve a "Páginas" y selecciona la que deseas modificar
3. Realiza los cambios necesarios usando el editor visual
4. Haz clic en "Actualizar" para publicar los cambios

## Respaldo y seguridad

1. Instala un plugin de respaldo como "UpdraftPlus"
2. Configura respaldos automáticos semanales
3. Instala un plugin de seguridad como "Wordfence" o "Sucuri"
4. Mantén WordPress, temas y plugins actualizados

## Soporte

Si necesitas ayuda con tu sitio WordPress, puedes:
- Consultar la documentación oficial: https://wordpress.org/support/
- Buscar tutoriales en YouTube
- Contratar servicios de mantenimiento WordPress
