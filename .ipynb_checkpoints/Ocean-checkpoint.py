import ocean_lib

class Ocean:
    
    def get_example_datasets():
        
        return(
               {"punks":"did:op:C9D0568838fa670baEe7195Ea443b32EfCAc2281",
                 "VladData":"did:op:72419bf07C6181dAEdc068caB0d81faa2951910e",
                 "AvgDenver":"did:op:81607300c6b50fbF0172E9A0038B6e898Fc15d82"
                 }
                )
    
    def request_ocean_dataset(did,output_fn):
        
        print("This function doesn not work")

        asset = ocean.assets.resolve(did)

        sample_link = asset.metadata['additionalInformation']['links'][0]['url']#Needs to be generalized
        ID = Path(sample_link).parts[4]

        download_dir = Path('data')
        dataset_name = f"{dataset_name}-sample"
        download_path = str(download_dir / (dataset_name + '.tgz'))
        
        return download_path