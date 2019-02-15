import string

class TupleOperations:

    @staticmethod
    def get_match_count(tuple_set, tuple_list):
        """
        returns the total n-tuple matches by checking if each element in the tuple_list is present in the tuple_set.
        """
        matches = 0
        for elem in tuple_list:
            if elem in tuple_set:
                matches += 1
                print (elem)
        return matches


    @staticmethod
    def create_tuple_list(filepath, n, syn_dic):
        """
        creates the tuples list.
        takes filepath, tuple size and synonym dictionary as input paramenters.
        words are striped leading and trailing spaces and converted to lowercase.
        """
        tuple_list = []
        with open(filepath) as contents:
            for line in contents:
                words = line.strip().lower().split(" ")
                for index, word in enumerate(words):
                    if word in syn_dic:
                        words[index] = syn_dic[word]
                for index in range(len(words)-n+1):
                    segment = ' '.join((words[index:index+n]))
                    tuple_list.append(segment)
        return tuple_list


    @staticmethod
    def create_synonym_map(filepath):
        """
        creates a synonym dictionary where every word is mapped to the first word synonym in the line.
        words are striped leading and trailing spaces, converted to lowercase and sentence punctuations are removed before mapping.
        """
        synonym_map ={}
        with open(filepath) as contents:
            for line in contents:
                words = line.strip().lower().split(" ")
                first_word = words[0] if len(words) else None
                for word in words:
                    word = word.strip(string.punctuation)
                    synonym_map[word] = first_word
        return synonym_map