# Sistema de Alertas vía Telegram usando AWS Lambda y SNS

Este proyecto proporciona una plantilla lista para desplegar notificaciones automáticas a Telegram utilizando AWS Lambda y SNS. Incluye:

- Función Lambda que envía mensajes a Telegram desde un Topic SNS.
- Función Lambda de ejemplo que publica mensajes en el Topic.
- Scripts de despliegue automatizados.
- Eventos de prueba y documentación clara.

---

## Estructura del Proyecto
telegram-alert-template/
│
├── lambda_notifier/
│   ├── lambda_function.py
│   ├── requirements.txt  # requests
│   ├── build_and_deploy.sh
│
├── lambda_publisher_example/
│   ├── lambda_function.py
│   └── build_and_deploy.sh
│
└── README.md 


---

### Crear un Bot de Telegram

- Conecta con [@BotFather](https://t.me/BotFather) en Telegram
- Crea un bot y guarda el **TOKEN**
- Inicia una conversación con el bot desde tu cuenta
- Usa una petición como `https://api.telegram.org/bot<TOKEN>/getUpdates` para obtener tu `chat_id`

### 2. Despliega la Lambda Notifier

Entra en el directorio `lambda_notifier/` y ejecuta:

./build_and_deploy.sh

# Asegúrate de tener configurado AWS CLI con las credenciales correctas

Variables de entorno necesarias:
- TOKEN → Token de tu bot de Telegram
- CHAT_ID → chat_id al que enviar alertas

### Crea y conecta el SNS Topic
- Crea un Topic SNS
- Suscribe la función TelegramNotifier como target
- Otorga permisos para que Lambda(s) puedan publicar en el Topic
Ejemplo de política (IAM) para publicar:
{
  "Effect": "Allow",
  "Action": "sns:Publish",
  "Resource": "arn:aws:sns:REGION:ID_CUENTA:NOMBRE_DEL_TOPIC"
}

