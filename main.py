class Node():
  def __init__(self,value, next_node=None):
    self.value = value
    self.next_node = next_node
    #print(self.value)
    
def print_list(lst):
  tmp=lst
  while tmp.next_node!=None:
    print (tmp.value,end='->')
    tmp=tmp.next_node
  print (tmp.value)

def print_rec(lst):#рекурсивно обращается к последующему элементу
  print (lst.value,end='')
  if lst.next_node!=None:
    print ('->',end='')
    print_rec(lst.next_node)

import confignode
def copylist(lst): #создает копию листа. создаем узел - в него данные, и т.д
  
  tmp=lst
  head=tmp.value #голова,которая пришла
  copy=Node(head)
  while tmp.next_node!=None: #если не указывает на конец
    tmp=tmp.next_node
    copy=Node(tmp.value,copy)
  if confignode.flag==True:
    return reverse(copy)
  else: return copy
    
def reverse(lst):
  confignode.flag=False
  #print_list(copylist(lst))
  return copylist(lst)

#start,middle,end  
def add_list(lst,value,location):  #lst -наш список,value -что вставить,location - куда вставить
  if location=='start':
    return Node(value,lst)
  else:
    if location=='end':
      result=Node(value,copylist(lst))
      return reverse(result)
    else:
      if location=='middle':
        count=1
        lst_copy=lst
        lst_copy2=lst
        while lst_copy.next_node!=None:
          count+=1
          lst_copy=lst_copy.next_node
        print('длина списка = ',count)
        print_list(lst)
        pos=int(count/2)+1 #вычисляем середину,куда вставлять число,ну и округляем
        print('вставить число на позицию',pos)
        res=None
        count=1
        while lst.next_node!=None:
          if pos==count:
            res=Node(value,res)#вставка нужного числа
          res=Node(lst.value,res)
          lst=lst.next_node
          count+=1
          
        res=Node(lst.value,res)
        
        
        if pos==2:
          res=Node(lst_copy2.value)
          res=Node(value,res)
          res=Node(lst.value,res)
        return reverse(res)
  
  
  
def del_list(lst,location):
  tmp=lst
  if location=='start':
    return reverse(copylist(lst.next_node))
  else:
    if location=='end':
      return copylist(reverse(tmp).next_node)
    else:
      if location=='middle':
        count=1
        lst_copy=lst
        lst_copy2=lst
        while lst_copy.next_node!=None:
          count+=1
          lst_copy=lst_copy.next_node
        print('длина списка = ',count)
        print_list(lst)
        pos=int(count/2)+1 #вычисляем середину,откуда удалять число,ну и округляем
        print('удалить число с позиции',pos)
        res=None
        count=1
        while lst.next_node!=None:
          if pos!=count:
            res=Node(lst.value,res)
          lst=lst.next_node
          count+=1
          
        res=Node(lst.value,res)
        return reverse(res)

#конкатенация      
def plus(lst,other):
  print_list(lst)
  print('+')
  print_list(other)
  print('=')
  res=reverse(lst)
  while other.next_node!=None:
    res=Node(other.value,res)
    other=other.next_node
  res=Node(other.value,res)
  return reverse(res)

#пересечение  
def intersection(lst,other):
  res = None 
  while lst!=None: 
    tmp = other 
    while tmp!=None: 
      #print('Сравниваем ',lst.value,'и',tmp.value)
      if lst.value == tmp.value:
        #print('!')
        if res!=None: #если новый список уже не пустой
          res = Node(lst.value, res)
        else: #если первый эл-т кладем в новый список
          res = Node(lst.value)
      tmp = tmp.next_node
    lst = lst.next_node
  return reverse(res)  
  
'''
def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp

def bubble_sort(lst):
  res=None
  tmp=lst
  
  cnt=0
  while tmp!=None:
    cnt+=1
    tmp=tmp.next_node
  print(cnt)
  
  j=0
  while j!=cnt-1:
    res=lst
    i=0
    while i!=cnt-1:
      lst2=lst.next_node
      if lst.value>lst2.value:
        print(lst.value,'и',lst2.value)
        lst.value,lst2.value=lst2.value,lst.value
      res=Node(lst.value,res)
      lst=lst.next_node
      i+=1
    j+=1
  return res
'''
  
  
def bubbleSort(lst,n):
  tmp=lst
  #длину списка определим
  cnt=0
  while tmp!=None:
    cnt+=1
    tmp=tmp.next_node
  #print(cnt)
  tmp=lst
  for passnum in range(cnt-1,0,-1):
    lst=tmp
    for i in range(passnum):
      lst2=lst.next_node
      if lst.value>lst2.value:
          #print(lst.value,'и',lst2.value)
          lst.value,lst2.value=lst2.value,lst.value
      lst=lst.next_node  
  if n=='ascending':
    return tmp  
  else: 
    if n=='descending':
      return reverse(tmp)
  
#Срезка по последовательности seq (start:finish:step)
def seq(lst,start,finish,step):

  print_list(lst)
  tmp=lst
  res=None
  #длину списка определим
  cnt=0
  while tmp!=None:
    cnt+=1
    tmp=tmp.next_node
  
  for i in range(cnt):
    if i%step==0 and i<=finish and i>=start:
      res=Node(lst.value,res)
    lst=lst.next_node
  
  return reverse(res)
  
    #temp=tmp.next_node #указатель на следующий
    #print_list(temp.value)
  
node5= Node(2)
node4 = Node(7,node5)
node3 = Node(0, node4)
node2 = Node(4,node3)
node1 = Node(3,node2)



#copylist(node1)
print('Исходный список:')
print_list(node1)
print('Его копия:')
print_rec(copylist(node1))

print('\nОбращение порядка списка на противоположный:')
print_rec(reverse(node1))
#_____________________________________________________
add=0
print('\n\nВставка - в начало cписка числа ',add,':')
print_list(add_list(node1,add,'start'))

print('\nВставка - в конец cписка числа ',add,':')
print_list(add_list(node1,add,'end'))

print('\nВставка - в середину cписка числа ',add,':')
print_list(add_list(node1,add,'middle'))
#_____________________________________________________
print('\n\nУдаление числа из начала cписка')
print_list(del_list(node1,'start'))
print('\nУдаление числа из конца cписка')
print_list(del_list(node1,'end'))
print('\nУдаление числа из середины cписка')
print_list(del_list(node1,'middle'))
#_____________________________________________________
print('\n\nКонкатенация')
print_list(plus(node1,node3))
#_____________________________________________________
print('\n\nПересечение')
print_list(intersection(node1,node3))
#_____________________________________________________
'''
print('\n\nСортировка пузырьком')
#ascending descending по возрастанию,по убыванию
print('\nпо возрастанию')
print_list(bubbleSort(node1,'ascending'))
print('\nпо убыванию')
print_list(bubbleSort(node1,'descending'))
'''
#_____________________________________________________
start=3
finish=4
step=1
print('\n\nСрезка с позиции',start,'по позицию',finish,'с шагом=',step)
print_list(seq(node1,start,finish,step))
