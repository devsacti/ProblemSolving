## template

def judge(result,depth,inequals):
  window=result[depth-1]+inequals[depth]+result[depth]
  return eval(window)

def bruteforce(result,depth,limit, inequals):
  if(depth>=limit):
    print('arrive')
    # print(result)
  else:
    for numchar in '123456789':
      result[depth]=numchar
      print(' '*depth,end='')
      print('given',result)
      print(' '*depth,end='')
      print('depth',depth)

      if(depth==0):
        bruteforce(result[:],depth+1,limit, inequals)
      
      result[depth]='*'
      print(' '*depth,end='')
      print('remove',result)
      print(' '*depth,end='')
      print('depth',depth)
      print('--')
      
        
      # else:
      #   token=judge(result,depth,inequals)
      #   print(token)
      #   if(token):
      #     bruteforce(result[:],depth+1,limit, inequals)
      #   else:
      #     return

if __name__=="__main__":
  n=int(input())
  # NOT INDEX OF COMPUTER FOR PROCESS
  inequals=[0]+input().split()
  # print(inequals)
  
  result=['*']*(n+1)
  depth=0
  print('start and depth',result,'/',depth)
  print('----')
  
  bruteforce(result,depth,(n+1),inequals)
  
  