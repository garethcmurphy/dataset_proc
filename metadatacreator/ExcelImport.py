#!/usr/bin/env python3

import xlrd
import pandas as pd



class ExcelImporter:
    def __init__(self):
        self.filename = "/Users/garethmurphy/Documents/multigrid_metadata.xlsx"
        pass
    
    def read_excel(self) -> object:
        pd.read_excel(self.filename)
        self.x = "test1"
        
        
if __name__ == '__main__':
    ei = ExcelImporter()
    ei.read_excel()