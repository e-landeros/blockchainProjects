#Create blockchain
#Flask==0.12.2 : pip install Flask==0.12.2
#Postman HTTP client 
import datetime
import hashlib
import json
from flask import Flask, jsonify

# Build Blockchain Architecture

class Blockchain:

    def __init__(self):
        self.chain = [] #chain containing the blocks
        self.create_block(proof = 1, previous_hash = '0')#genesis block; each block will have its own proof, previous hash. none on genesis block

    def create_block(self, proof, previous_hash):
        
        #define each block with 4 keys
        block = {'index' : len(self.chain) + 1,
                 'timestamp' : str(datetime.datetime.now()),
                 'proof' : proof,
                 'previous_hash' : previous_hash} 
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]
#proof of work is the number which the miner needs to solve. needs to be difficult to solve but ez to verify
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        #non symmetrical operation
        while check_proof is False:
            #str and encode are needed to format so that hashlib sha256 is ecnoded with b'string'
            hash_operation = hashlib.sha256(str(new_proof **2 - previous_proof **2).encode()).hexdigest()
# Mine Blockchain