import argparse
from ntupleops import TupleOperations

def main():
    parser = argparse.ArgumentParser(description='n-tuple plagiarism detector')

    # parse arguments
    parser.add_argument('syns_file', metavar = 'SYN_FILE', type = argparse.FileType('r'))
    parser.add_argument('file1', metavar = 'FILE1', type = argparse.FileType('r'))
    parser.add_argument('file2', metavar = 'FILE2', type = argparse.FileType('r'))
    parser.add_argument('-n', metavar = 'N', type = int, default=3) # optional arg
    args = parser.parse_args()

    if args.n < 0:
        print ("Error: N cannot be negative.")
        return -1

    synonym_dic = TupleOperations.create_synonym_map(args.syns_file.name)
    tuple_list1 = TupleOperations.create_tuple_list(args.file1.name, args.n, synonym_dic)
    tuple_list2 = TupleOperations.create_tuple_list(args.file2.name, args.n, synonym_dic)
    
    l1 = len(tuple_list1)
    l2 = len(tuple_list2)

    if not l1 or not l2:
        print ("Error: One of the files generated no tuples.")
        return -1

    print (l1 + args.n - 1, l2 + args.n - 1)

    if (args.n > l1 + args.n - 1) or (args.n > l2  + args.n - 1):
        print ("Error: N out of bounds.")
        return -1
    else:
        matches = TupleOperations.get_match_count(set(tuple_list2), tuple_list1)
        match_percent = (matches/l1) * 100 if l1 else 0.0
        print ("Output : ", match_percent, "%")

# To prevent this file to be used as a module, and to be able to execute this on the command line.
if __name__ == '__main__':
    main()