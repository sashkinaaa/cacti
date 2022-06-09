import platform
import pandas as pd
import os
import numpy as np

def haar_1d ( n, x ):
  u = x.copy ( )
  s = np.sqrt ( 2.0 )
  v = np.zeros ( n, dtype = np.float64 )
#
#  Determine K, the largest power of 2 such that K <= N.
#
  k = 1
  while ( k * 2 <= n ):
    k = k * 2
  
  while ( 1 < k ):

    k = k // 2

    length = len(u)
    i = 0
    j = 0
    while i < length:
      v[j] = (u[i] + u[i+1])/s
      i += 2
      j += 1
      
    u = v.copy()
  return u[0]

if ( __name__ == '__main__' ):
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  
  cwd = os.getcwd()
  inboundDF = pd.read_csv(cwd + "/clientInboundTrafficWithoutAttack.csv")
  inboundtestValues = inboundDF['Value'].to_list()
  outboundDF = pd.read_csv(cwd + "/clientOutboundTrafficWithoutAttack.csv")
  outboundtestValues = outboundDF['Value'].to_list()
  totalTraffic = np.add(inboundtestValues, outboundtestValues)
  length = len(inboundDF)
  
  #print(totalTraffic.to_string())
  print(haar_1d (length, totalTraffic))