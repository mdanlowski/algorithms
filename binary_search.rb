# frozen_string_literal: true

module Algorithms
  class Search
    def initialize
      @bin_iters = 0
    end

    def binary_search(arr, value)
      pivot = arr.size/2
      val_at_pivot = arr[pivot]
      
      puts arr.to_s
      puts "#{pivot}  |  #{val_at_pivot}"

      return @bin_iters if val_at_pivot == value
      return false if arr.size < 2

      @bin_iters +=1
      if value < val_at_pivot 
        return binary_search arr[0..pivot-1], value
      elsif value > val_at_pivot
        return binary_search arr[pivot+1..], value
      end

    end


  end

end

# Algorithms::Search.binary_search( [1,2,3,4,5,6,7,8,9], 4 )