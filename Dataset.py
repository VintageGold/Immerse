import numpy as np 


class Datasets():
    
    def create_np_ones_file(row,col,fn="data/nparray.txt"):

        np.ones((row,col)).tofile(fn,sep=",")

    def create_test_file(bytes_size,fn="data/test_data.dat"):

        with open(fn, "wb") as o: 
            o.write(np.random.bytes(bytes_size))

    #https://docs.ipfs.io/how-to/command-line-quick-start/#initialize-the-repository       
    def get_example_image_hash():

        return "QmSgvgwxZGaBLqkGyWemEDqikCqU52XxsYLKtdy3vGZ8uq"