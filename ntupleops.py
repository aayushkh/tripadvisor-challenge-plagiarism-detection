import string

class TupleOperations:

    @staticmethod
    def get_match_count(tuple_set, tuple_list):
        matches = 0
        for elem in tuple_list:
            if elem in tuple_set:
                matches += 1
                print (elem)
        return matches

    @staticmethod
    def create_tuple_list(filepath, n, syn_dic):
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
        synonym_map ={}
        with open(filepath) as contents:
            for line in contents:
                words = line.strip().lower().split(" ")
                first_word = words[0] if len(words) else None
                for word in words:
                    word = word.strip(string.punctuation)
                    synonym_map[word] = first_word
        return synonym_map