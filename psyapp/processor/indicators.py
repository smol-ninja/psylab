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

def dayHighLow(dhdl,previousDays = 1):
    dhdl['PrevHigh_'+str(previousDays)] = 0
    dhdl['PrevLow_'+str(previousDays)] = 0
    for i in range(len(dhdl)):
        if i < previousDays:
            continue
        else:
            dhdl.loc[i, 'PrevHigh_'+str(previousDays)] = dhdl.loc[i-previousDays,'High']
            dhdl.loc[i, 'PrevLow_'+str(previousDays)] = dhdl.loc[i-previousDays,'Low']
    return dhdl

def ema(ema_calc,pd = 200):
    ema_calc['ema_'+str(pd)] = 0.0
    ema_calc['ema_'+str(pd)]= ema_calc['Close'].ewm(span = pd,ignore_na=False, min_periods =0 ,adjust=True).mean()
    return ema_calc

def macd(macd_calc,sig =9,ema1= 12,ema2 = 26):
    macd_calc['EMA1'] = 0.0
    macd_calc['EMA1']= macd_calc['Open'].ewm(span = ema1,ignore_na=False, min_periods =0 ,adjust=True).mean()
    macd_calc['EMA2'] = 0.0
    macd_calc['EMA2']= macd_calc['Open'].ewm(span = ema2,ignore_na=False, min_periods =0 ,adjust=True).mean()
    macd_calc['macd'] = macd_calc['EMA1'] - macd_calc['EMA2']
    macd_calc['Signal_'+str(sig)] = 0.0
    macd_calc['Signal_'+str(sig)]= macd_calc['macd'].ewm(span = sig,ignore_na=False, min_periods =0 ,adjust=True).mean()
    del macd_calc['EMA1']
    del macd_calc['EMA2']
    return macd_calc

def mfi(mfi_d,win=9):
    mfi_d['typicalPrice'] = (mfi_d['High']+mfi_d['Low']+mfi_d['Close'])/3.0
    mfi_d['flowMoney'] = mfi_d['typicalPrice']*mfi_d['Volume']
    mfi_d['1pflow'] =0
    mfi_d['1mflow'] =0
    mfi_d['14pflow'] =0
    mfi_d['14mflow'] = 0
    for i in range(1,len(mfi_d)):
        if (mfi_d.loc[i,'typicalPrice']-mfi_d.loc[i-1,'typicalPrice']>0):
            mfi_d.loc[i,'1pflow'] = mfi_d.loc[i,'flowMoney']
        else:
            mfi_d.loc[i,'1mflow'] = mfi_d.loc[i,'flowMoney']
        if i==win:
            mfi_d.loc[i,'14pflow'] = mfi_d['1pflow'][1+i-win:1+win].mean()
            mfi_d.loc[i,'14mflow'] = mfi_d['1mflow'][1+i-win:1+win].mean()
        elif i>win:
            mfi_d.loc[i,'14pflow'] = mfi_d['1pflow'][i-win+1:i+1].mean()
            mfi_d.loc[i,'14mflow'] = mfi_d['1mflow'][1+i-win:1+i].mean()
    mfi_d['mfRatio'] = mfi_d['14pflow']/mfi_d['14mflow']
    mfi_d['mfi'] = 100.0 - 100.0/(mfi_d['mfRatio']+1)
    return mfi_d

def obv(obv_d):
    obv_d['obv'] =0
    for i in range(1,len(obv_d)):
        if (obv_d.loc[i,'Close']-obv_d.loc[i-1,'Close']>0):
            obv_d.loc[i,'obv'] = obv_d.loc[i-1,'obv']+obv_d.loc[i,'Volume']
        else:
            obv_d.loc[i,'obv'] = obv_d.loc[i-1,'obv'] - obv_d.loc[i,'Volume']
    return obv_d

def roc(roc_data, col_name, pd = 10):
    if pd<=0:
        print 'Period of ROC must be greate than 0'
        raise IOError
    else:
        roc_data['roc_'+ col_name] = 0
        for i in range(len(roc_data)):
            if i<pd:
                continue
            else:
                roc_data.loc[i, 'roc_'+ col_name] = (roc_data.loc[i, col_name] - roc_data.loc[i-pd, col_name])/float(pd)
    return roc_data

def rsi(rsi_d,pd=7):
    win = pd
    rsi_d['gain'] = 0.0
    rsi_d['loss'] = 0.0
    rsi_d['avg_g'] = 0.0
    rsi_d['avg_l'] =0.0
    rsi_d['rs']=0.0
    rsi_d['rsi_'+str(win)] =0.0
    for i in range(1,len(rsi_d)):
        if (rsi_d.loc[i,'Close']-rsi_d.loc[i-1,'Close']>0):
            rsi_d.loc[i,'gain'] = rsi_d.loc[i,'Close']-rsi_d.loc[i-1,'Close']
        else:
           rsi_d.loc[i,'loss'] = rsi_d.loc[i-1,'Close']-rsi_d.loc[i,'Close']
        if i==win:
           rsi_d.loc[i,'avg_g'] = rsi_d['gain'][0:win].mean()
           rsi_d.loc[i,'avg_l'] = rsi_d['loss'][0:win].mean()
        elif i>win:
            rsi_d.loc[i,'avg_g'] = (rsi_d.loc[i-1,'avg_g']*(win-1)+ rsi_d.loc[i,'gain'])/float(win)
            rsi_d.loc[i,'avg_l'] = (rsi_d.loc[i-1,'avg_l']*(win-1)+ rsi_d.loc[i,'loss'])/float(win)
    rsi_d['rs'] = rsi_d['avg_g']/rsi_d['avg_l']
    rsi_d['rsi_'+str(win)] = 100.0 - 100.0/(1.0+rsi_d['rs'])
    del rsi_d['gain']
    del rsi_d['loss']
    del rsi_d['avg_g']
    del rsi_d['avg_l']
    del rsi_d['rs']
    return rsi_d

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
