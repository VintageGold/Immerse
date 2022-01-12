import web3
from eth_account import account

class Wallet:
    
    def create_wallet(parse=True):
        
        acc = account.Account().create()
        
        if parse:
            return acc.address,acc.key
        
        return acc