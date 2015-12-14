import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = '5b6c44a4'.decode('hex')
P2P_PORT = 55889
ADDRESS_VERSION = 0
RPC_PORT = 55888
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'worldleadcurrencyaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 0 if height < 25000 else 76293945
TITHE_FUNC = lambda height: ('1Fk9zcKLzLBgpDk2mx3M2EujL5ytUvbcQp', 7553100586) if height >= 167200 else [({
	0: '15Z36Hi5z6GRU5281QKMeTVH7zZkn6DCi4',
	1: '1E1YVXPXHTjXKNxwvPHam6PQEDkQGrdWX2',
	2: '1MAJkknQaxx6ERSbbLqrthzYsFEmFnzoKQ',
	3: '1NQKyeK7tN3wWyT2DzjdaRqEkMBr1287JE',
	4: '1AjBv2saiu8TD7zhgCLUHrKhh15rWzy69q',
	5: '14YXSLsF3RxvbPTiERApTCzupuSjpuHcuq',
	6: '1FuZFufk5L6gcsqsB3mLjW4L1qjGMAzT5t',
	7: '1MCk1vWCuURd8mthqGaYwbTCg4H9fLq35d',
	8: '198e5jtoBn4ZzDu4Cr4oVE1ikCyvdUGoKu',
	9: '1D1G2qzbG1Sb8xWWbcfgpEPsdPigQAYweD',
	10: '1KYD6pWkNs8SarMS9weeSrcnhHgxX5zrsh',
	11: '19A8XXqdTUXfJwiTQ8adMVv2qtqkNnkKf5',
	12: '1AZYUC6S2Fgkrg32sDvpprt1A4xHajkNs6',
	13: '18P7bRqf4kCRQGkBCK2T2qgaMQc5UfyA22',
	14: '1QD3pXGsrtCDW6j99RHpTJ6N7VCBJCpwtX',
	15: '1NL4vX4oWCXmuuUxaDDrXU3W3JNS9cwmkw',
	16: '14KsGmamtVKZwu8ScEZrY4Ad4DvCHLgEd6',
	17: '1J6PzQ175t1hePMLM4FZ6j8BJPJzGWsdJy',
	18: '1NY8xU183hmonjXvLcxc42qKKctjWZHoaf',
	19: '1JKetEDVcVVXZ6uopTngPjypAQRaEC3mrt',
	20: '1AG1Qw19DsuScPwM5fCBeA7rr9fqaYYZbW',
	21: '1J2onYLZeEzDa2vp6ih86fvB8sgg82bpu2',
	22: '1EkwVYTiXbsHMtHXLpvkK1mvUmPUkpb5uo',
	23: '1Fzzr3U3m3EuBbmpYZRRF7q5BsnPSw55eS',
	24: '1Fzzr3U3m3EuBbmpYZRRF7q5BsnPSw55eS',
	25: '1MtgWhHxTvBj1aa3cf6oz6fidefXscxsSQ',
	26: '1LrGEjMc6a83xoBivcrEXFRnj1uMwnhWiM',
	27: '12RwBg1KVXH6q2QVx1VHS6DmNqJkyeMov8',
	28: '196XW3MgLmML5GjD9p1MXsAKenvfGbVHpt',
	29: '17bp8CQaHectDADASqCgDsibqAjGVnFYV7',
	30: '18Yzdv9CPgSvi87oLQgTcK5brY4SVGp14M',
	31: '1Fk9zcKLzLBgpDk2mx3M2EujL5ytUvbcQp',
}[(height - 30800)/4400], 7553100586)]

POW_FUNC = data.hash256
BLOCK_PERIOD = 600 # s
SYMBOL = 'WLC'
CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Worldleadcurrency') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Worldleadcurrency/') if platform.system() == 'Darwin' else os.path.expanduser('~/.worldleadcurrency'), 'worldleadcurrency.conf')
BLOCK_EXPLORER_URL_PREFIX='http://109.73.173.118:81/Block/'
ADDRESS_EXPLORER_URL_PREFIX='http://109.73.173.118:81/Address/'
TX_EXPLORER_URL_PREFIX = 'http://109.73.173.118:81/Tx/'
SANE_TARGET_RANGE=(2**256//2**32 - 1, 2**256//2**32 - 1)
