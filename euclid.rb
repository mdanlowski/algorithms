def largest_common_divisor(a, b)
  if a < b
    swap = a
    a = b
    b = swap
  end
  
  while a % b > 0
    temp = b
    b = a % b
    a = temp
  end
  
  return b
end