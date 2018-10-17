import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'cffcbeea'.decode('hex')
P2P_PORT = 18168
ADDRESS_VERSION = 65
RPC_PORT = 18888
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'zcoinaddress' in (yield bitcoind.rpc_help()) and
            (yield bitcoind.rpc_getblockchaininfo())['chain'] == 'test'
        ))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//210000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('Lyra2Z_scrypt').getPoWHash(data))
BLOCK_PERIOD = 600 # s
SYMBOL = 'tXZC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'zcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/zcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.zcoin'), 'zcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://testexplorer.zcoin.io/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://testexplorer.zcoin.io/address/'
TX_EXPLORER_URL_PREFIX = 'http://testexplorer.zcoin.io/tx/'

# SANE_TARGET_RANGE = (2**256//2**26//1000000 - 1, 2**256//2**26 - 1)
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
# SANE_TARGET_RANGE = (1, 2**256 - 1)
DUMB_SCRYPT_DIFF = 2**8
DUST_THRESHOLD = 0.03e8
