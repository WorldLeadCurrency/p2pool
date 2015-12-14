from p2pool.bitcoin import networks

PARENT = networks.nets['worldleadcurrency']
SHARE_PERIOD = 10 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = '5b1e3d23ecfd2dd4'.decode('hex')
PREFIX = 'a6e1a35238aa0392'.decode('hex')
P2P_PORT = 9669
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32 - 1
PERSIST = True
WORKER_PORT = 9668
BOOTSTRAP_ADDRS = 'pool.winc-ev.com pool.winc-ev.de'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-wlc'
VERSION_CHECK = lambda v: 50700 <= v < 60000 or 60010 <= v < 60100 or 60400 <= v
