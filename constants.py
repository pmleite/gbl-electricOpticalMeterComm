# TOOL to interaction with COM - cuteCom

# COM defs
DEVICE      = '/dev/ttyUSB0'
BAUD        = 300
DATA        = 7
PARITY      = 'E'
TIMEOUT     = 20 
PROTO       = 'IEC-62056-21'
SLEEP_DELAY = 0.2
ACK_DELAY   = 1

# Software defs  (Working Modes - READ and TEST)
MODE        = 'READ' # READ, CONFIG, TEST 
GUI         = False   # True or False
LANGUAGE    = 'PT'   # PT or EN  
VERBOSE     = True   # True or False
APP_NAME    = 'meterReader'
VER         = '0.1'

# Escape Sequences
NULL= '\x00'   # Null
SOH = '\x01'   # Start of Header
STX = '\x02'   # Start of Text
ETX = '\x03'   # End of Text
EOT = '\x04'   # End of Transmission
ENQ = '\x05'   # Enquiry
ACK = '\x06'   # Acknowledge
LF  = '\x0A'   # Line Feed
CR  = '\x0D'   # Carriage Return
ESC = '\x1B'   # Escape
EXC = '\x21'   # Exclamation Mark

# Messages Strings
ME172_INIT_STRING = '\x2F\x3F\x21\x0D\x0A' # '/?!\r\n' Init Reqeust

# Modelos e Marcas de Leitores
BRANDS_MODELS = { 
                 '/ISk5ME172':          { 'brand' : 'ISKRA',
                                          'model' : 'ME172',
                                          'urlIMG': 'https://cdn.ecommercedns.uk/files/5/209935/7/17206817/spwis172-image.jpg'
                                        },
                 '/ISk5MT174':          { 'brand' : 'ISKRA',
                                          'model' : 'MT174',
                                          'urlIMG': 'https://cdn.ecommercedns.uk/files/5/209935/7/17206817/spwis172-image.jpg'
                                        },
                 '/LGZ4\\2ZMD3102400':  { 'brand' : 'LANDIS',
                                          'model' : 'E650',
                                          'urlIMG': 'https://cdn.ecommercedns.uk/files/5/209935/7/17206817/spwis172-image.jpg'
                                        },
                }

# Dicionário para guardar os dados recolhidos   
DATA_COLLECTED = {} 

# Mensagens de Informação PT/EN
INFO_MESSAGES = {'PT': {'START': 'Iniciando comunicação com o dispositivo...',
                        'INFO': 'Informação do dispositivo recebidas com sucesso!',    
                        'ERROR': 'Erro ao coletar dados! Verifique o dispositivo, reinicie e tente novamente!',
                        'COLLECTING': 'Iniciando a Recolha de dados, por favor aguarde!',
                        'HOLD': 'Por favor aguarde!',
                        'STX_ERROR': 'STX não encontrado!',
                        'SUCCESS': 'Dados recolhidos com sucesso!',
                        'TEST': 'Teste de leitura do Dispositivo!',
                        'COLLEDTED': 'Dados recolhidos:',
                        'CSV': 'Exportado para CSV...',
                        'INVALID_TYPE': 'Tipo de exportação inválido!',
                        'READ': 'Modo de Leitura!',
                        'CONFIG': 'Modo de Configuração!',
                        'TESTMOD': 'Modo de Teste!',
                        'LER': 'Ler Contador',
                        'SAIR': 'Sair',
                        'IMAGE': 'Imagem do Dispositivo',
                        'MARCA': 'Marca',
                        'MODELO': 'Modelo',
                        'ID': 'ID'},

                # English
                'EN':  {'START': 'Starting communication with the device...',
                        'INFO': 'Device information received successfully!',
                        'ERROR': 'Error collecting data! Check the device, restart and try again!',
                        'COLLECTING': 'Starting collecting data, please wait!',
                        'HOLD': 'Please wait!',
                        'STX_ERROR': 'STX not found!',
                        'SUCCESS': 'Data collected successfully!',
                        'TEST': 'Device reading test!',
                        'COLLEDTED': 'Data collected:',
                        'CSV': 'Exported to CSV...',
                        'INVALID_TYPE': 'Invalid export type!',
                        'READ': 'Read Mode!',
                        'CONFIG': 'Configuration Mode!',
                        'TESTMOD': 'Test Mode!',
                        'LER': 'Read Counter',
                        'SAIR': 'Exit',
                        'IMAGE': 'Device Image',
                        'MARCA': 'Brand',
                        'MODELO': 'Model',
                        'ID': 'ID'},

                # French       
                'FR':  {'START': 'Démarrage de la communication avec le dispositif...',
                        'INFO': 'Informations du dispositif reçues avec succès!',
                        'ERROR': 'Erreur de collecte de données! Vérifiez le dispositif, redémarrez et réessayez!',
                        'COLLECTING': 'Démarrage de la collecte de données, veuillez patienter!',
                        'HOLD': 'Veuillez patienter!',
                        'STX_ERROR': 'STX introuvable!',
                        'SUCCESS': 'Données collectées avec succès!',
                        'TEST': 'Test de lecture du dispositif!',
                        'COLLEDTED': 'Données collectées:',
                        'CSV': 'Exporté vers CSV...',
                        'INVALID_TYPE': 'Type d\'exportation invalide!',
                        'READ': 'Mode de lecture!',
                        'CONFIG': 'Mode de configuration!',
                        'TESTMOD': 'Mode de test!',
                        'LER': 'Lire le compteur',
                        'SAIR': 'Sortie',
                        'IMAGE': 'Image du dispositif',
                        'MARCA': 'Marque',
                        'MODELO': 'Modèle',
                        'ID': 'ID'}, 
                
                # Spanish 
                'ES':  {'START': 'Iniciando comunicación con el dispositivo...',
                        'INFO': 'Información del dispositivo recibida con éxito!',
                        'ERROR': 'Error al recopilar datos! Verifique el dispositivo, reinicie y vuelva a intentarlo!',
                        'COLLECTING': 'Iniciando la recopilación de datos, espere por favor!',
                        'HOLD': 'Por favor espere!',
                        'STX_ERROR': 'STX no encontrado!',
                        'SUCCESS': 'Datos recopilados con éxito!',
                        'TEST': 'Prueba de lectura del dispositivo!',
                        'COLLEDTED': 'Datos recopilados:',
                        'CSV': 'Exportado a CSV...',
                        'INVALID_TYPE': 'Tipo de exportación no válido!',
                        'READ': 'Modo de lectura!',
                        'CONFIG': 'Modo de configuración!',
                        'TESTMOD': 'Modo de prueba!',
                        'LER': 'Leer contador',
                        'SAIR': 'Salida',
                        'IMAGE': 'Imagen del dispositivo',
                        'MARCA': 'Marca',
                        'MODELO': 'Modelo',
                        'ID': 'ID'}
                }
