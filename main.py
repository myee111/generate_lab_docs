import argparse                                                                                                                                      
                                                                                                                                                     
def process_arguments():                                                                                                                             
    parser = argparse.ArgumentParser(description='Process command-line arguments')                                                                   
    parser.add_argument('-f', '--file', required=True, help='Input file path')                                                                       
    parser.add_argument('-o', '--output', required=True, help='Output file path')                                                                    
    args = parser.parse_args()                                                                                                                       
    return args

def main():                                                                                                                                          
    args = process_arguments()                                                                                                                       
    print(f'Input file: {args.file}')                                                                                                                
    print(f'Output file: {args.output}')                                                                                                             
                                                                                                                                                     
if __name__ == '__main__':                                                                                                                           
    main()