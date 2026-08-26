def main():
  movie = ['The Holy Grail', 1975, 'Terry Jones & Terry Gilliam', 91, ['Graham Chapman', ['Michael Palin', 
'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]]
 
  
  #  if isinstance(each_item, list):
    
  #   for nested_item in each_item:
   
  #    if isinstance(nested_item, list):
   
  #     for deeper_item in nested_item:
   
  #      print(deeper_item)
   
  #    else:
   
  #      print(nested_item)
  #  else:
  #   print(each_item)
  def print_lol(movie):       
     for each_item in movie:
      if isinstance(each_item, list):
   
        print_lol(each_item)
      
      else:
        print(each_item)       
                    
  print_lol(movie)
    
    
    
    
if __name__ == "__main__":
    main()