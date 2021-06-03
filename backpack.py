#%%

DEBUG = True

def debug(msg):
    if DEBUG:
        print("DEBUG: ", str(msg).replace('\n', '\n' + (' '*8)))

class Backpack:
    
    def __init__(self, max_weight):
        """ Creates a Backpack with given max_weight.

            - if max_weight is negative, raises ValueError
        """
        if max_weight < 0:
            raise ValueError("Expected a non-zero weight, got instead: %s "  % max_weight)

        self._elements = []
        self._max_weight = max_weight
        self._current_weight = 0
        

    def size(self):
        """ RETURN the number of items in the backpack

            - MUST run in O(1)
        """
        return len(self._elements)
        
    
    def max_weight(self):
        """ Return the maximum allowed weight
        """
        return self._max_weight

    def weight(self):
        """  Return the backpack total current weight

             ************  MUST RUN IN O(1)  ***************
        """
        return self._current_weight

    def is_empty(self):
        """ RETURN True if the backpack empty, False otherwise

            - MUST run in O(1)
        """
        return self._elements == []

    def __str__(self):
        """ Return a string like  
        
                Backpack: weight=8 max_weight=10 elements=[('a',5), ('b',3)]
        """
        return f'Backpack: weight={self._current_weight} max_weight={self._max_weight} elements = {self._elements}'


    def peek(self):
        """ RETURN the top element in the stack (without removing it!)
            
            - if stack is empty, raise IndexError
            - Must run in O(1)  

        """
        if self._elements == []:
            raise IndexError('Backpack is empty')

        return self._elements[-1]


    def push(self, item, w):
        """ Adds item of weight w on the top of the backpack.
            
            - if w is negative, raises ValueError
            - if w is heavier than topmost item, raises ValueError
            - if max_weight is exceeded, raises ValueError
            - MUST run in O(1)
            
        """
        if w < 0:
            raise ValueError('Cannot push an element with weight < 0')

        if self._elements != [] and w > self.peek()[1]:
            raise ValueError('Cannot push an element heavier than the current top')

        if self._current_weight + w > self._max_weight:
            raise ValueError('Cannot push an element which exceed the maximum weight')

        self._current_weight += w
        self._elements.append((item, w))
        
        

    def pop(self):
        """ Removes the top element in the backpack and RETURN it
            as a tuple (element_id, weight) like ('a', 3)

            - if backpack is empty, raise IndexError
            - MUST run in O(1)
        """
        if self._elements == []:
            raise IndexError('the Backpack is empty')

        x = self._elements.pop()
        self._current_weight -= x[1]
        return x


# NOTE: this function is implemented *outside* the class !

def remove(backpack, el):
    """
        Remove topmost occurrence of el found in the backpack, 
        and RETURN it (as a tuple name, weight)
        
        - if el is not found, raises ValueError        

        - DO *NOT* ACCESS DIRECTLY FIELDS OF BACKPACK !!!
          Instead, just call methods of the class!

        - MUST perform in O(n), where n is the backpack size

        - HINT: To remove el, you need to call Backpack.pop() until
                the top element is what you are looking for. You need 
                to save somewhere the popped items except the one to 
                remove, and  then push them back again.
    
    """
    to_ret = None

    reinsert = []

    while not backpack.is_empty():
        curr = backpack.peek()
        if curr[0] == el:
            to_ret = backpack.pop()
            break
        else:
            x = backpack.pop()
            reinsert.append(x)

    for i in reversed(reinsert):
        backpack.push(i[0], i[1])

    if to_ret:
        return to_ret

    raise ValueError('Item not found')