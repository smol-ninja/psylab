
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