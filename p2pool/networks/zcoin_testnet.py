from p2pool.bitcoin import networks

PARENT = networks.nets['zcoin_testnet']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = '79d16c058a3a9e2f'.decode('hex')
PREFIX = 'edbd53f28c478737'.decode('hex')
P2P_PORT = 9338
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1

PERSIST = True

WORKER_PORT = 9327
BOOTSTRAP_ADDRS = '149.28.132.209 199.247.23.133'.split(' ')
# BOOTSTRAP_ADDRS = ''.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-xzc-testnet'
VERSION_CHECK = lambda v: None if 100400 <= v else 'Zcoin version too old. Upgrade to 0.13.4.2 or newer!'
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['bip65', 'csv', 'segwit'])
MINIMUM_PROTOCOL_VERSION = 1600
NEW_MINIMUM_PROTOCOL_VERSION = 1700
SEGWIT_ACTIVATION_VERSION = 17
