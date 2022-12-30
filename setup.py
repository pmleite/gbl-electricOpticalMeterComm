from languages import INFO_MESSAGES
from brands_models import BRANDS_MODELS
from obis_codes import OBIS_CODES

# TOOL to interaction with COM - cuteCom

# COM defs (algumas podem ser passadas como argumentos no futuro)
DEVICE           = '/dev/ttyUSB0'
BAUD             = 300
DATA             = 7
PARITY           = 'E'
TIMEOUT          = 20 
PROTO            = 'IEC-62056-21'
SLEEP_DELAY      = 0.2
ACK_DELAY        = 1
DEFAULT_PASSWORD = '00000000'

# Software defs
GUI         = False   # True or False (NOT IMPLEMENTED YET)
LANGUAGE    = 'PT'   # PT, EN, FR, ES
VERBOSE     = False   # True or False
APP_NAME    = 'meterReader'

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

# Dicionário para guardar os dados recolhidos   
DATA_COLLECTED = {} 
