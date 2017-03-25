# -*- coding: utf-8 -*-
"""
Created on Mon Jul 04 16:25:11 2016

@author: Sagar
"""

import numpy as np
def adx(adx_calc,pd=14):
    r = pd
    adx_calc['p_dm1'] = 0.0
    adx_calc['m_dm1'] = 0.0
    adx_calc['trr'] = 0.0
    adx_calc['p_dmr'] = 0.0
    adx_calc['m_dmr'] = 0.0
    adx_calc['p_dir'] = 0.0
    adx_calc['m_dir'] = 0.0
    adx_calc['p_di_dif'] = 0.0
    adx_calc['p_di_sum'] = 0.0
    adx_calc['dx'] = 0.0
    adx_calc['adx_'+str(r)] = 0.0   
    adx_calc['tr'] =0.0
    for i in range(1,len(adx_calc)): 
        adx_calc.loc[i,'tr'] = max(adx_calc.loc[i,'High'] - adx_calc.loc[i,'Low'],np.absolute(adx_calc.loc[i,'High']-adx_calc.loc[i-1,'Close']),np.absolute(adx_calc.loc[i,'Low']-adx_calc.loc[i-1,'Close']))
        adx_calc.loc[i,'p_dm1'] = adx_calc.loc[i,'High'] - adx_calc.loc[i-1,'High'] if (adx_calc.loc[i,'High'] - adx_calc.loc[i-1,'High']>0 and (adx_calc.loc[i,'High'] - adx_calc.loc[i-1,'High']>adx_calc.loc[i-1,'Low'] - adx_calc.loc[i,'Low'])) else 0
        adx_calc.loc[i,'m_dm1'] = adx_calc.loc[i-1,'Low'] - adx_calc.loc[i,'Low'] if (adx_calc.loc[i,'Low'] - adx_calc.loc[i-1,'Low']<0 and (adx_calc.loc[i,'High'] - adx_calc.loc[i-1,'High']<adx_calc.loc[i-1,'Low'] - adx_calc.loc[i,'Low'])) else 0    
        if i==r:        
            adx_calc.loc[i,'trr'] = adx_calc['tr'][1:r+1].sum()
            adx_calc.loc[i,'p_dmr'] = adx_calc['p_dm1'][1:r+1].sum()
            adx_calc.loc[i,'m_dmr'] = adx_calc['m_dm1'][1:r+1].sum()
        elif i>r:
            adx_calc.loc[i,'trr'] = adx_calc.loc[i-1,'trr'] + adx_calc.loc[i,'tr'] - adx_calc.loc[i-r,'tr']
            adx_calc.loc[i,'p_dmr'] = adx_calc.loc[i-1,'p_dmr'] + adx_calc.loc[i,'p_dm1'] - adx_calc.loc[i-r,'p_dm1']
            adx_calc.loc[i,'m_dmr'] = adx_calc.loc[i-1,'m_dmr'] + adx_calc.loc[i,'m_dm1'] - adx_calc.loc[i-r,'m_dm1']
        adx_calc.loc[i,'p_dir'] = 100.0*adx_calc.loc[i,'p_dmr']/float(adx_calc.loc[i,'trr']) if (adx_calc.loc[i,'trr']>0) else 0
        adx_calc.loc[i,'m_dir'] = 100.0*adx_calc.loc[i,'m_dmr']/float(adx_calc.loc[i,'trr']) if (adx_calc.loc[i,'trr']>0) else 0
    adx_calc['p_di_dif'] = np.absolute(adx_calc['p_dir'] - adx_calc['m_dir'])
    adx_calc['p_di_sum'] = adx_calc['p_dir'] + adx_calc['m_dir']
    adx_calc['dx'] = 100*adx_calc['p_di_dif']/adx_calc['p_di_sum']
    for i in range(r,len(adx_calc)):
        if i==2*r-2:
           adx_calc.loc[i,'adx_'+str(r)] = adx_calc['dx'][r-1:2*r-1].mean()
        elif i>2*r-2:
            adx_calc.loc[i,'adx_'+str(r)]= (adx_calc.loc[i-1,'adx_'+str(r)]*(r-1)+ adx_calc.loc[i,'dx'])/float(r)
    del adx_calc['p_dm1'] 
    del adx_calc['m_dm1']
    del adx_calc['trr'] 
    del adx_calc['p_dmr'] 
    del adx_calc['m_dmr'] 
    del adx_calc['p_dir'] 
    del adx_calc['m_dir'] 
    del adx_calc['p_di_dif'] 
    del adx_calc['p_di_sum'] 
    del adx_calc['dx'] 
    del adx_calc['tr']
    return adx_calc