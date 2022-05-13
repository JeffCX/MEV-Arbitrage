from web3 import Web3, HTTPProvider
from config import *
import time
import json
import binascii
import traceback
from web3.middleware import geth_poa_middleware
import time

class Operator:

    def __init__(self):

        self.w3 = Web3(HTTPProvider(NODE_URL))
        address = Web3.toChecksumAddress(QUERY_CONTRACT_ADDRESS)
        self.query_contract = self.w3.eth.contract(address=address, abi=BATCH_QUERY_ABI)

    def get_pair_market(self, factory_address, start, end):
        data = self.query_contract.functions.getPairsByIndexRange(
            factory_address, 
            start, 
            end
        ).call()
        market_address = [entry[2] for entry in data]
        return data, market_address

    def get_markets_reserves(self, markets):
        data = self.query_contract.functions.getReservesByPairs(markets).call()
        print(data)

if __name__ == "__main__":

    start_time = time.time()
    operator = Operator()

    data, markets = operator.get_pair_market(UNISWAP_FACTORY, 1, 1000)

    print(data)
    print('take times to get markets', time.time() - start_time)

    market_reservse = operator.get_markets_reserves(markets)
    print(market_reservse)
    
