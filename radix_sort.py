def radixSort(array):
    
    """
    Least Significant First Radix Sort Implementation. Only sorts whole-number part of number.
    Input: Single or multidimensional array of numeric types.
    Output: Single array of ordered items
    
    """
    try:
        
        # Functionality to allow a multidimensional list as input
        
        try:
            
            # Trim fractional part of number
            # Bottleneck, but this implementation can only handle ints
            
            numbers = [int(item) for item in array]
        except:
            
            # Place all the items in all the lists into a single list
            
            flattened_array = [item for sublist in array for item in sublist]
            numbers = [int(item) for item in flattened_array]
            
        # Error Checking for negative numbers        
                
        for item in numbers:
            if item < 0:
                message = 'Function expects positive numbers only'
                return message
            
        if len(numbers) == 0:
            message = 'No items to sort'
            return message

        # Set radix for base10 input
        radix = 10
        
        # Initialise for selecting LSD on first loop
        position_value = 1
        
        # Initialise max number. For break loop condition when position_value
        # outranks than max.
        
        max_digit = max(numbers)

        # loop init and break condition
        while position_value < max_digit:
            
            # buckets initialised as multidimensional empty list
            # select the position_value digit
            # add number with the position_value digit to the bucket for that digit
            
            buckets = [[] for _ in range(radix)]
            for num in numbers:
                temp = int((num / position_value) % radix)
                buckets[temp].append(num)

            # reorder the original list based on bucket order
            # initialise a, index for original list
            # for each bucket in range (i.e. radix)
            # place the item in the bucket at index a of the original list
            # increment a, for next position
            
            a = 0
            for b in range(radix):
                bucket = buckets[b]
                for item in bucket:
                    numbers[a] = item
                    a += 1
                    
            # move to the second-least significant digit, continue until break condition
            position_value *= radix

        return numbers
    
    except (ValueError, TypeError) as error:
        print(error)