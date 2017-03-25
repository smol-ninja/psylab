# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 02:31:24 2016

@author: Sagar
"""

def stochastic(stch_d,pd=7,r=3):
    win = pd
    stch_d['HighestH'] = 0.0
    stch_d['LowestL'] = 0.0
    stch_d['FastK'] = 0.0
    stch_d['FastD'] = 0.0
    stch_d['SlowK'] = 0.0
    stch_d['SlowD_'+str(win)] =0.0
    for i in range(win,len(stch_d)): 
        stch_d.loc[i,'HighestH'] = stch_d['High'][i-win:i+1].max()
        stch_d.loc[i,'LowestL'] = stch_d['Low'][i-win:i+1].min()

    stch_d['FastK'] = 100*(stch_d['Close'] -stch_d['LowestL'])/(stch_d['HighestH']-stch_d['LowestL'])
    for i in range(r-1,len(stch_d)):
        stch_d.loc[i,'FastD'] = stch_d['FastK'][i-r:i+1].mean()
        stch_d.loc[i,'SlowK'] = stch_d['FastK'][i-r:i+1].mean()
        stch_d.loc[i,'SlowD_'+str(win)] = stch_d['SlowK'][i-r:i+1].mean()
    
    del stch_d['HighestH'] 
    del stch_d['LowestL'] 
    del stch_d['FastK'] 
    del stch_d['FastD'] 
    del stch_d['SlowK'] 
    
    return stch_d