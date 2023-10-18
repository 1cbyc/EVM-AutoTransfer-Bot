from decimal import Decimal
from eth_utils.conversions import to_hex
from web3 import Web3
import config
import time
bsc='https://bsc-dataseed.binance.org/'
web3=Web3(Web3.HTTPProvider(bsc))
while True:
    balanceWei = web3.eth.get_balance(config.addressFrom)
    balanceReadable= web3.fromWei(balanceWei,'ether')
    nonce= web3.eth.getTransactionCount(config.addressFrom)
    print("My Amount of BNB is " + str(balanceReadable) + " BNB, Transfer is Initiated once BNB is more than 0.000105")
    
    if balanceReadable > 0.000105 :
        print("Amount is " + str(balanceReadable) +
              " BNB, Transfer Instance Initialized")
        maxTransfer = balanceReadable-Decimal(0.000105)
        # To Send Transaction
        # First, Create The Transaction Dictionary

        tx = {
            'nonce' : nonce,
            'to' : config.addressTo,
            'value' : web3.toWei(maxTransfer,'ether'),
            'gas' : 21000,
            'gasPrice' : web3.toWei('5', 'gwei'),
        }
        # Second, Sign the Transaction

        txSign = web3.eth.account.signTransaction(tx,config.private_key4)
        # Send the Signed Transaction
        txHash=web3.eth.sendRawTransaction(txSign.rawTransaction)

        print("Here Your TxHash Down Here")
        print(web3.toHex(txHash))
        print(".")
        print("..")
        print("...")
        print("....")
        print(".....")
        print("......")
        print(".......")
        print("......")
        print(".....")
        print("....")
        print("...")
        print("..")
        print(".")
        print("Transfer instance Completed and Closed")
        print(".......")
        time.sleep(10)
        