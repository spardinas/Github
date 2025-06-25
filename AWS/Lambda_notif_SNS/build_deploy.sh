#!/bin/bash

set -e

FUNCTION_NAME="Lambda_function_name"  

echo "📦 Empaquetando Lambda $FUNCTION_NAME..."

# Limpiar cualquier build previo
rm -rf build
mkdir -p build

# Copiar el código
cp lambda_function.py build/
cp requirements.txt build/

# Instalar dependencias
pip install -r requirements.txt -t build/

# Crear el zip
cd build
zip -r ../lambda.zip .
cd ..

# Subir a AWS
echo "⬆️ Subiendo lambda.zip a Lambda..."
aws lambda update-function-code \
  --function-name $FUNCTION_NAME \
  --zip-file fileb://lambda.zip

echo "✅ ¡Lambda actualizada!"