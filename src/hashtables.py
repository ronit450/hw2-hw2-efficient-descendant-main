import random
from typing import Any

class MySet(object):
    '''An abstract class that provides a set interface which is just sufficient
    for the implementation of this assignment.
    '''

    def __init__(self, elements: [Any]) -> None:
        """Initializes this set with elements.

        Each element in elements must be hashable by python.

        Args:
        - self: manadatory reference to this object.
        - elements: this set is populated with these elements.

        Returns:
        None
        """
        # self.size = len(elements)
        # self.table = self.size * [None]
        # self.n = 0  # number of entries in the map
        # self.prime = sympy.randprime(0,self.size)  # prime for MAD compression
        # self.scale = 1 + random.randint(0,self.prime-1)  # scale from 1 to p-1 for MAD
        # self.shift = random.randrange(self.prime)
    #
    # def hash_function(self, k):
    #     return (hash(k)* self.scale + self.shift) % self.prime % len(self.table)

    def add(self, element: Any) -> None:
        """Adds element to this set.

        element must be hashable by python.

        Args:
        - self: manadatory reference to this object.
        - element: the element to add to this set

        Returns:
        None
        """



    def discard(self, element: Any) -> None:
        """Removes element from this set.

        there is noting to be done if element is not present in this set.

        Args:
        - self: manadatory reference to this object.
        - element: the element to remove from this set

        Returns:
        None
        """


    def __iter__(self)-> "MySet":
        """Makes this set iterable.

        There are many different ways to implement this. Choose one that works
        for you.

        Args:
        - self: manadatory reference to this object.
        """

    def __next__(self):
        '''
        So this is a followup for iter function which makes our class items itertable.
        '''
        ''''Iterator function to return the next value from this list.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        the next value in this list since the last iteration.
        '''
    def get(self, index):
        '''Returns the value at index, i.

        Alternate to use of indexing syntax.

        Parameters:
        - self: mandatory reference to this object
        - i: the index from which to retrieve the value.

        Returns:
        the value at index i.
        '''


class ChainedSet(MySet):
    '''Overrides and implementes the methods defined in MySet. Uses a chained
    hash table to implement the set.
    '''
    def __init__(self, elements: [Any]) -> None:
        """Initializes this set with elements.

        Each element in elements must be hashable by python.

        Args:
        - self: manadatory reference to this object.
        - elements: this set is populated with these elements.

        Returns:
        None
        """


        self.size = len(elements)
        self.table = [[] for i in range(self.size)]
        for i in elements:
            self.add(i)


    def hash_function(self, element_to_map):
        # self.prime = sympy.randprime(self.size,1000)  # prime for MAD compression
        # self.scale = 1 + random.randint(0, self.prime - 1)  # scale from 1 to p-1 for MAD
        # self.shift = random.randrange(self.prime)
        # return ((hash(element_to_map)* self.scale + self.shift) % self.prime) %len(self.table)
        return hash(element_to_map) % self.size


    def add(self, element: Any) -> None:
        """Adds element to this set.

        element must be hashable by python.

        Args:
        - self: manadatory reference to this object.
        - element: the element to add to this set

        Returns:
        None
        """
        key = self.hash_function(element)
        if element not in self.table[key]:
            self.table[key].append(element)


    def discard(self, element: Any) -> None:
        """Removes element from this set.

        there is noting to be done if element is not present in this set.

        Args:
        - self: manadatory reference to this object.
        - element: the element to remove from this set

        Returns:
        None
        """

        key = self.hash_function(element)
        if element in self.table[key]:
            self.table[key].remove(element)


    # def resize(self):
    #     self.size = self.size*2
    #     temp_lst = []
    #     for i in self.table:
    #         if i != [None]:
    #             temp_lst.append(i)
    #
    #     print("This is temp_lst", temp_lst)
    #     self.table = [[None] for i in range(self.size)]
    #     self.num_elements_inserted = 0  # number of entries in the map
    #     for i in temp_lst:
    #         print("these are from temp_lst",i[0])
    #         # self.add(i)

    def __iter__(self):
        """Makes this set iterable.

        There are many different ways to implement this. Choose one that works
        for you.

        Args:
        - self: manadatory reference to this object.
        """ 
        self._iter_index: int = 0
        self.bucket: int = 0
        while True:
            if self._iter_index < len(self.table):
                value = self.table[self._iter_index]
                if self.bucket < len(value):
                    val_from_bucket = value[self.bucket]
                    self.bucket += 1
                    yield val_from_bucket
                else:
                    self._iter_index += 1
                    self.bucket = 0
            else:
                break


class LinearSet(MySet): #this is linear probing
    '''Overrides and implementes the methods defined in MySet. Uses a linear
    probing hash table to implement the set.
    '''
    def __init__(self, elements: [Any]) -> None:
        """Initializes this set with elements.

        Each element in elements must be hashable by python.

        Args:
        - self: manadatory reference to this object.
        - elements: this set is populated with these elements.

        Returns:
        None
        """
        self.size = 1000
        self.load_factor = 0.5
        self.decreaseFactor = 0.1
        self.table = [None for i in range(self.size)]
        self.num_elements_inserted = 0  # number of entries in the map
        for i in elements:
            self.add(i)


    def hash_function(self, element_to_map):
        # self.prime = sympy.randprime(self.size,1000)  # prime for MAD compression
        # self.scale = 1 + random.randint(0, self.prime - 1)  # scale from 1 to p-1 for MAD
        # self.shift = random.randrange(self.prime)
        # return ((hash(element_to_map)* self.scale + self.shift) % self.prime) %len(self.table)
        return hash(element_to_map) % self.size

    def resize(self, check):
        # print("Calling resize")
        if check:
            self.size = self.size*2
        else:
            self.size = self.size//2
        self.num_elements_inserted = 0  # number of entries in the map
        temp_lst = self.table
        self.table = [None for i in range(self.size)]
        for i in temp_lst:
            if i != None and i != -1:
                self.add(i)
        # print("Going from resize")

    def check_existence(self, element):
        hash_key = self.hash_function(element)
        while True:
            if hash_key < len(self.table):
                if self.table[hash_key] == element:
                    return False
                if self.table[hash_key] == None:
                    return True
                hash_key += 1
            else:
                hash_key = 0





    def add(self, element: Any) -> None:
        """Adds element to this set.

        element must be hashable by python.

        Args:
        - self: manadatory reference to this object.
        - element: the element to add to this set

        Returns:
        None
        """
        # print("Calling add")
        if self.num_elements_inserted/self.size >= (self.load_factor):
            self.resize(True)


        if self.check_existence(element):
            key = self.hash_function(element)
            while True:
                if key < len(self.table):
                    value = self.table[key]
                    if value == None or value == -1:
                        self.table[key] = element
                        self.num_elements_inserted += 1
                        break
                    else:
                        key +=1
                else:
                    key = 0


        # print("going from add")
        # print(element)
        # print(self._my_set_)
        # self.my_set.append()


    def discard(self, element: Any) -> None:


        """Removes element from this set.

        there is noting to be done if element is not present in this set.

        Args:
        - self: manadatory reference to this object.
        - element: the element to remove from this set

        Returns:
        None
        """
        # print("coming in discard")
        if not self.check_existence(element):
            # if (self.num_elements_inserted / self.size) < self.decreaseFactor:
            #     self.resize(False)
            key = self.hash_function(element)
            while True:
                if key < len(self.table):
                    if self.table[key] == None:
                        break
                    if self.table[key] == element:
                        self.table[key] = -1
                        self.num_elements_inserted -= 1
                        break
                    key +=1
                else:
                    key = 0

        # print("going from discard")

    def __iter__(self):
        """Makes this set iterable.

        There are many different ways to implement this. Choose one that works
        for you.

        Args:
        - self: manadatory reference to this object.
        """
        # self._iter_index: int = 0
        # return self
        lst = [i for i in self.table if i != None and i != -1]
        return iter(lst)

    # def __next__(self):
    #     if self._iter_index < len(self.table):
    #         value = self.table[self._iter_index]
    #         self._iter_index += 1
    #         if value != -1 and value != None:
    #             return value
    #         return self.__next__()
    #     else:
    #         self._iter_index = 0
    #         raise StopIteration



class MyDict(object):
    '''An abstract class that provides a dictionary interface which is just
    sufficient for the implementation of this assignment.
    '''

    def __init__(self) -> None:
        """Initializes this dictionary.

        Args:
        - self: manadatory reference to this object.

        Returns:
        none
        """

        self._dic_for_hash = {}
    
    def __setitem__(self, key: Any, newvalue: Any) -> None:
        """Adds (key, newvalue) to the dictionary, overwriting any prior value.

        dunder method allows assignment using indexing syntax, e.g.
        d[key] = newvalue

        key must be hashable by pytohn.
        
        Args:
        - self: manadatory reference to this object.
        - key: the key to add to the dictionary
        - newvalue: the value to store for the key, overwriting any prior value 

        Returns:
        None
        """
        if any(key):
            self._dic_for_hash[key] = newvalue
    
    def get(self, key: Any, default: Any = None) -> Any:
        """Returns the value stored for key, default if no value exists.

        key must be hashable by pytohn.
        
        Args:
        - self: manadatory reference to this object.
        - key: the key whose value is sought.
        - default: the value to return if key does not exist in this dictionary

        Returns:
        the stored value for key, default if no such value exists.
        """
        if any(key):
            for index, item in self._dic_for_hash.items():
                if index == key:
                    return item
        return default

    def items(self) -> [(Any, Any)]:
        """Returns the key-value pairs of the dictionary as tuples in a list.
        
        Args:
        - self: manadatory reference to this object.

        Returns:
        the key-value pairs of the dictionary as tuples in a list.
        """
        self._lst_of_tuple = []
        for key, value in self._dic_for_hash.items():
            temp_tupple = (key, value)
            self._lst_of_tuple.append(temp_tupple)
        return self._lst_of_tuple

    def clear(self) -> None:
        """Clears the dictionary.

        Args:
        - self: manadatory reference to this object.

        Returns:
        None.
        """
        self._dic_for_hash.clear()

class ChainedDict(MyDict):
    '''Overrides and implementes the methods defined in MyDict. Uses a chained
    hash table to implement the dictionary.
    '''

    def __init__(self) -> None:
        """Initializes this dictionary.

        Args:
        - self: manadatory reference to this object.

        Returns:
        none
        """
        self.size = 100
        self._dic_for_hash = [[] for i in range(self.size)]
    def hash_function(self, element_to_map):
        # self.prime = sympy.randprime(self.size,1000)  # prime for MAD compression
        # self.scale = 1 + random.randint(0, self.prime - 1)  # scale from 1 to p-1 for MAD
        # self.shift = random.randrange(self.prime)
        # return ((hash(element_to_map)* self.scale + self.shift) % self.prime) %len(self.table)
        return hash(element_to_map) % self.size

    def __setitem__(self, key: Any, newvalue: Any) -> None:
        """Adds (key, newvalue) to the dictionary, overwriting any prior value.

        dunder method allows assignment using indexing syntax, e.g.
        d[key] = newvalue

        key must be hashable by pytohn.

        Args:
        - self: manadatory reference to this object.
        - key: the key to add to the dictionary
        - newvalue: the value to store for the key, overwriting any prior value

        Returns:
        None
        """
        hash_value = self.hash_function(key)
        for i in self._dic_for_hash[hash_value]:
            if (i[0]) == key:
                self._dic_for_hash[hash_value].remove(i)
                break
        self._dic_for_hash[hash_value].append((key,newvalue))

    def get(self, key: Any, default: Any = None) -> Any:
        """Returns the value stored for key, default if no value exists.

        key must be hashable by pytohn.

        Args:
        - self: manadatory reference to this object.
        - key: the key whose value is sought.
        - default: the value to return if key does not exist in this dictionary

        Returns:
        the stored value for key, default if no such value exists.
        """
        hash_value = self.hash_function(key)
        if self._dic_for_hash[hash_value] == []:
            return default
        else:
            for i in self._dic_for_hash[hash_value]:
                if key == i[0]:
                    return i[1]
        return default

    def items(self) -> [(Any, Any)]:
        """Returns the key-value pairs of the dictionary as tuples in a list.

        Args:
        - self: manadatory reference to this object.

        Returns:
        the key-value pairs of the dictionary as tuples in a list.
        """
        lst_of_tuple = []
        for i in self._dic_for_hash:
            for j in i:
                lst_of_tuple.append(j)
        return lst_of_tuple

    def clear(self) -> None:
        """Clears the dictionary.

        Args:
        - self: manadatory reference to this object.

        Returns:
        None.
        """
        self._dic_for_hash = [[] for i in range(self.size)]


class LinearDict(MyDict):
    '''Overrides and implementes the methods defined in MyDict. Uses a linear
    probing hash table to implement the dictionary.
    '''


    def __init__(self) -> None:
        """Initializes this dictionary.

        Args:
        - self: manadatory reference to this object.

        Returns:
        none
        """
        self.size = 1000
        self.resize_factor = 0.5
        # print('hello, i am in dict')
        self.num_elements_inserted = 0
        self._dic_for_hash = [(None,None) for i in range(self.size)]
        # print(self._dic_for_hash)

    def resize(self):
        # print("calling Resize of dict")
        self.size = self.size * 2
        self.num_elements_inserted = 0  # number of entries in the map
        temp_lst =  self._dic_for_hash
        self._dic_for_hash = [(None,None) for i in range(self.size)]
        for item in temp_lst:
            self.__setitem__(item[0],item[1])
        # print("going from resize of dict")

    def hash_function(self, element_to_map):
        # self.prime = sympy.randprime(self.size,1000)  # prime for MAD compression
        # self.scale = 1 + random.randint(0, self.prime - 1)  # scale from 1 to p-1 for MAD
        # self.shift = random.randrange(self.prime)
        # return ((hash(element_to_map)* self.scale + self.shift) % self.prime) %len(self.table)
        return hash(element_to_map) % self.size

    def __setitem__(self, key: Any, newvalue: Any) -> None:
        """Adds (key, newvalue) to the dictionary, overwriting any prior value.

        dunder method allows assignment using indexing syntax, e.g.
        d[key] = newvalue

        key must be hashable by pytohn.

        Args:
        - self: manadatory reference to this object.
        - key: the key to add to the dictionary
        - newvalue: the value to store for the key, overwriting any prior value

        Returns:
        None
        """
        # print("I am in set dict")
        # num_of_empty = 0
        # for i in self._dic_for_hash:
        #     if i == (None,None):
        #         num_of_empty +=1
        if (self.num_elements_inserted /self.size) >= self.resize_factor:
            self.resize()
        hash_value = self.hash_function(key)
        while True:
            if hash_value < len(self._dic_for_hash):
                if self._dic_for_hash[hash_value] == (None,None) or self._dic_for_hash[hash_value][0] == key:
                    if self._dic_for_hash[hash_value] == (None,None):
                        self.num_elements_inserted +=1
                    self._dic_for_hash[hash_value] = (key,newvalue)
                    break
                hash_value +=1
            else:
                hash_value = 0
        # print("hello I going from set dict")


    def get(self, key: Any, default: Any = None) -> Any:
        """Returns the value stored for key, default if no value exists.
y
        key must be hashable by pytohn.

        Args:
        - self: manadatory reference to this object.
        - key: the key whose value is sought.
        - default: the value to return if key does not exist in this dictionary

        Returns:
        the stored value for key, default if no such value exists.
        """
        hash_value = self.hash_function(key)
        while True:
            if hash_value < len(self._dic_for_hash):
                value = self._dic_for_hash[hash_value]
                if value != (None, None):
                    if value[0] == key:
                        return value[1]
                    else:
                        hash_value += 1
                else:
                    return default

            else:
                hash_value = 0

    def items(self) -> [(Any, Any)]:
        """Returns the key-value pairs of the dictionary as tuples in a list.

        Args:
        - self: manadatory reference to this object.

        Returns:
        the key-value pairs of the dictionary as tuples in a list.
        """
        temp_lst = []
        for i in self._dic_for_hash:
            if i != (None,None):
                temp_lst.append(i)
        return temp_lst



    def clear(self) -> None:
        """Clears the dictionary.

        Args:
        - self: manadatory reference to this object.

        Returns:
        None.
        """
        self._dic_for_hash = [(None,None) for i in range(self.size)]
        self.num_elements_inserted = 0






