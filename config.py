# on rinkeby test blockchain

# from https://rpc.info/

NODE_URL = 'https://rinkeby.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161'

# deployed this contract in rinkeby testnet

QUERY_CONTRACT_ADDRESS = '0x0698deFe43C8aFf23e572f944e0e10CF229e4C5b'

BATCH_QUERY_ABI = '[{"inputs":[{"internalType":"contract UniswapV2Factory","name":"_uniswapFactory","type":"address"},{"internalType":"uint256","name":"_start","type":"uint256"},{"internalType":"uint256","name":"_stop","type":"uint256"}],"name":"getPairsByIndexRange","outputs":[{"internalType":"address[3][]","name":"","type":"address[3][]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IUniswapV2Pair[]","name":"_pairs","type":"address[]"}],"name":"getReservesByPairs","outputs":[{"internalType":"uint256[3][]","name":"","type":"uint256[3][]"}],"stateMutability":"view","type":"function"}]'

UNISWAP_FACTORY = '0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f'