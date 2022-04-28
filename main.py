# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 17:17:01 2022

@author: Pinnacle
"""

def main():
    n = 10
    for i in range(n):
        print("*" * i)
    
    for i in range(n, 0, -1):
        print("*" * i)

if __name__=='__main__':
    main()