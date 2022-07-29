from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://rpc-mumbai.maticvigil.com/v1/0aef2a33937a03dc04746e653c2e985d8246174f"))

w3.eth.get_block(12345)