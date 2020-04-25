# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    if len(sequence) == 1:
        return sequence

    else:
        #hold out the first char 
        first_char = sequence[0]

        permutation_for_the_rest = get_permutations(sequence[1:])

        res = list()

        for item in permutation_for_the_rest:
            temp = list()
            for i in range(len(sequence)):
                temp.append(item[:i] + first_char + item[i:])
            res.extend(temp)

        return res 



if __name__ == '__main__':
#    #EXAMPLE
   example_input = 'abc'
   print('Input:', example_input)
   print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
   print('Actual Output:', get_permutations(example_input))
    


    

