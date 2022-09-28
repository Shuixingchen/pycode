### web3模块
```shell
pip3 install web3 py-solc-x
```
solc编译solidity为json文件
```shell
solc -o ./build --metadata contracts/Box.sol  # 会生成build/Box_meta.json
```

### web3.py与合约交互
```python
CONTRACTADDR = ""
ABI = ""
PRIVATERKEY = ""
w3 = Web3(Web3.HTTPProvider("https://eth-goerli.g.alchemy.com/v2/22yeINZa7al_eP4NLGW"))
dContrarct = w3.eth.contract(address=CONTRACTADDR, abi=ABI)
# 调用可读合约方法
count = dContrarct.caller().get_deposit_count()
# 调用合约transfer方法
rawTx = dContrarct.functions.transfer(toAddr,value).buildTransaction({
        'nonce': web3obj.eth.getTransactionCount(fromAddr),
        'gas': 6600000,
        'gasPrice': web3obj.toWei('2', 'gwei'),
        'chainId': web3obj.eth.chain_id
    })
signTx = web3obj.eth.account.sign_transaction(rawTx, PRIVATERKEY)
txHash = web3obj.eth.sendRawTransaction(signTx.rawTransaction).hex()
```