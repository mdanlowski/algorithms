# matching brackets - a VERY provisional approach
def validate(title)
  
  o_brackets = ["(", "[", "{"]
  c_brackets = [")", "]", "}"]
  stack = []
  last_br = 0
  
  title.each_char do |c|
    if stack.size > 0
      # pass
    end
    
    if o_brackets.include?(c)
      stack.push(c)
      last_br = stack.size - 1
      print stack
    end
    
    if c_brackets.include?(c) && stack.size == 0
      puts("INV - closing bracket appeared before opening bracket")
      return false
    end
    
    if c_brackets.include?(c) && o_brackets.index(stack[last_br]) != c_brackets.index(c)
      puts("INV - closing bracket of different type appeared first")
      return false
    end
    
    puts (title.index(c) - last_br)
    if c_brackets.include?(c) && title.index(c) - title.index(stack.last) < 2 
      puts("INV - met empty brackets")
      return false
    end
    
    if c_brackets.include?(c) && o_brackets.index(stack[last_br]) == c_brackets.index(c)
      stack.pop()
      last_br -= 1
      # puts("br match")
    end
    
  end
  
  if stack.size > 0
    puts("INV - unmatched bracket left")
    return false
  end
  
  puts("VALID")
  return true
  
end

validate("j(a)n[]z")
