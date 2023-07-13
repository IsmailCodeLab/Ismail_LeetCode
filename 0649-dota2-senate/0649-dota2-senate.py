class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        banr,band=0,0
        banned=[False]*len(senate)
        winner=set()
        while(len(winner)!=1):
          winner=set()
          for ind,per in enumerate(senate):
            if banned[ind]:
              continue
            if(per=='R'):
              if(banr>0):
                banr-=1
                banned[ind]=True
              else:
                band+=1
                winner.add('R')
            else:
              if(band>0):
                banned[ind]=True
                band-=1
              else:
                banr+=1
                winner.add('D')
        if winner.pop()=='R':
          return 'Radiant'
        else:
          return 'Dire'
