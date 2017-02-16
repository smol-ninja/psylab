# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 18:58:09 2017

@author: sagar
"""

import numpy as np
import scipy as sp

"""
profits_list: []
base_security_price : margin required to buy/sell 1 lot 
timeframe (str): 'daily','monthly', 'yearly'
calc_strategy_params(profits_list,base_security_price,timeframe)
return strategy parameter, strategyPass (bool)
"""
def calc_strategy_params(pnl_list,base_price=1.0,time_period = 'yearly'):
    
    #total profit, average profit
    total_profit = sum(pnl_list)
    print 'Total Profits are:', total_profit
    avg_profit = total_profit/float(len(pnl_list))
    print 'Average Profit:', avg_profit
    # Winning Percentage, Lossing Percentage
    win_perc = sum(i > 0 for i in pnl_list)/ float(len(pnl_list))
    loss_perc = sum(i < 0 for i in pnl_list)/ float(len(pnl_list))
    print 'Win Percentage:', win_perc
    print 'Loss Percentage:', loss_perc
    
    # Calculate Max Drawdown
    max_drawdown = 0
    temp_sum= 0
    for i in range(len(pnl_list)):
        if temp_sum+pnl_list[i]<0:
            temp_sum=temp_sum + pnl_list[i]
        else:
            temp_sum = 0
        if temp_sum<max_drawdown:
            max_drawdown =temp_sum
        
    print 'Max Drawdown:', max_drawdown
    print 'Max Drawdown wrt to Average Profit:', abs(max_drawdown/avg_profit)
    
    #profit Factor
    profit_only = [i for i in pnl_list if i >= 0]
    loss_only = [i for i in pnl_list if i < 0]
    profit_factor = abs(sum(profit_only)/float(sum(loss_only)))
    print 'Profit Factor:', profit_factor
    
    #Sharpe Ratio
    risk_free_ratio = 7
    if time_period == 'monthly':
        scaling_factor = 12.0
    elif time_period == 'daily':
        scaling_factor =365.0
    else:
        scaling_factor = 1.0
    std_error = np.std(pnl_list)/pow(len(pnl_list),0.5)
    sharpe_ratio = ((avg_profit/base_price)*100 - risk_free_ratio/scaling_factor)/np.std(pnl_list)
    print 'Standard Error:', std_error
    print 'Sharpe Ratio:',sharpe_ratio
    
    #K-Ratio, vami
    base_price = float(base_price)
    vami = [base_price]
    logvami  = [np.log10(vami[0])]
    for i in pnl_list:
        vami.append(vami[-1]*(1+i/base_price))
        logvami.append(np.log10(vami[-1]))
        
    m, b, r_value, p_value, std_err = sp.stats.linregress(range(len(pnl_list)+1), logvami)
    if std_err>0:
        kRatio = m/std_err
    else:
        kRatio = 'Capital Lost'
    print 'K-Ratio:', kRatio

    #Did the strategy pass?    
    strategyPass = False
    if total_profit>0 and abs(max_drawdown/avg_profit)<2.5 and profit_factor>1.5 and sharpe_ratio>0.75 and kRatio>1.5:
        strategyPass = True
    return strategyPass
