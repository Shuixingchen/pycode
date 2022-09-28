from binhex import binhex, hexbin
from web3 import Web3
import json
DEPLOYER = "0xe725D38CC421dF145fEFf6eB9Ec31602f95D8097"
CONTRACTADDR = "0xfF06b40b853b2700Afa5019aBE084469F10b63a5"
PRIVATERKEY = "19935d89cb5c67657c64a6383d601e30f04eb179a0369227403e5343bba22107"

IMCTokenAddr = "0x17eb0d548306372293C67A7DAD5c6bCBfE5593F8"

pubkey = ""
withdrawal_credentials = ""
signature = ""
deposit_data_root = ""

def getABI(contract):
    with open("./build/"+contract+".json") as f:
        metaData = json.load(f)
        return metaData["abi"]

def sendTransation(tx_dic):
    nonce = w3.eth.getTransactionCount(PRIVATERKEY)
    tx_dic["nonce"] = nonce
    tx_dic['gasPrice'] = w3.eth.gasPrice
    sign_tx = w3.eth.account.signTransaction(tx_dic, private_key=PRIVATERKEY)
    return w3.eth.sendRawTransaction(sign_tx.rawTransaction)


def sendTransationWithMoreGas(tx_dic, gwei):
    nonce = w3.eth.getTransactionCount(PRIVATERKEY)
    tx_dic["nonce"] = nonce
    tx_dic['gasPrice'] = w3.eth.gasPrice + w3.toWei(gwei, 'gwei')
    sign_tx = w3.eth.account.signTransaction(tx_dic, private_key=PRIVATERKEY)
    return w3.eth.sendRawTransaction(sign_tx.rawTransaction)


## 组装原始的rawTx
def getRawTransaction(web3obj, fromAddr, toAddr,value,contractObj):
    tx = contractObj.functions.transfer(toAddr,value).buildTransaction({
        'nonce': web3obj.eth.getTransactionCount(fromAddr),
        'gas': 6600000,
        'gasPrice': web3obj.toWei('2', 'gwei'),
        'chainId': web3obj.eth.chain_id
    })
    return tx

## 用fromAddr的私钥对rawTx进行签名
def signTransaction(web3obj, rawTx, privKey):
    signTx = web3obj.eth.account.sign_transaction(rawTx, privKey)
    txHash = web3obj.eth.sendRawTransaction(signTx.rawTransaction).hex()
    return txHash

def depositTx(web3obj, contractObj, privKey):
    rawTx = contractObj.functions.deposit(pubkey,withdrawal_credentials,signature,deposit_data_root).buildTransaction({
        'nonce': web3obj.eth.getTransactionCount(DEPLOYER),
        'gas': 6600000,
        'gasPrice': web3obj.toWei('2', 'gwei'),
        'chainId': web3obj.eth.chain_id
    })
    signTx = web3obj.eth.account.sign_transaction(rawTx, privKey)
    txHash = web3obj.eth.sendRawTransaction(signTx.rawTransaction).hex()
    return txHash

w3 = Web3(Web3.HTTPProvider("https://eth-goerli.g.alchemy.com/v2/22yeINZOnCEtAWJjw31sa7al_eP4NLGW"))

balance = w3.eth.get_balance(DEPLOYER)
dContrarct = w3.eth.contract(address=CONTRACTADDR, abi=getABI("DepositContract"))
ImToken = w3.eth.contract(address=IMCTokenAddr, abi=getABI("IMCToken"))

# 调用可读合约方法
# print(dContrarct.all_functions())
count = dContrarct.caller().get_deposit_count()
root = dContrarct.caller().get_deposit_root()
print(int.from_bytes(count, byteorder='little', signed=False))
print(root.hex())

# 调用合约写方法
# print(ImToken.caller().balanceOf("0xD9478B7cf6C4ACD11e90701Aa6C335B93a2C2368"))
rawTx = getRawTransaction(w3,DEPLOYER,"0xD9478B7cf6C4ACD11e90701Aa6C335B93a2C2368",1000,ImToken)
txHash = signTransaction(Web3, rawTx, PRIVATERKEY)
print(txHash)
print(ImToken.caller().balanceOf("0xD9478B7cf6C4ACD11e90701Aa6C335B93a2C2368"))