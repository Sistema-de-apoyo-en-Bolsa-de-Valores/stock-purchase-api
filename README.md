# stock-purchase-api (Puerto 8083)

API de ejecución de órdenes de compra de acciones.

## Pasos para levantar en local

### 1. Base de datos

Crear base de datos en MySQL db_stock_market_support_system.

### 2. Configuración de variables de entorno

Es necesario configurar las variables de entorno para conectarse a la base de datos y ejecutar la aplicación correctamente. A continuación, se muestra un ejemplo de las variables necesarias:

```bash
DB_HOST=localhost
DB_PORT=3306
DB_USERNAME=root
DB_PASSWORD=123
DB_NAME=db_stock_market_support_system
```

Se colocan en el archivo .env en la raíz del proyecto.

![image](https://github.com/user-attachments/assets/dcc04051-e34e-430c-acd3-bb2aa6347a11)

### 3. Descargar librerías

```bash
pip install -r requirements.txt
```

### 4. Levantar el proyecto en el puerto 8083

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8083
```
