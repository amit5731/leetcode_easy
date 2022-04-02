def isValid(s) -> bool:
       if len(s)<2:
         return False
       a={'(':')','{':'}','[':']'}
       order=[]
       for idx,data in enumerate(s):
           if a.get(data):
               order.insert(0,a[data])
           elif len(order)>0:
               if order[0]!=data:
                   return False
               order.pop(0)
           else:
              return False
       if len(order)>0:
            return False
       return True
