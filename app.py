import os
import pandas as pd
import numpy as np










def main():
    print("starting main ...")
    sep1 = " ~ "
    strPrint = str(os.getlogin())  + sep1 + str(os.uname()[:3]) + sep1 + str(os.getenv("HOME")) + sep1 
    print(strPrint)



if __name__ == "__main__":
    main()

