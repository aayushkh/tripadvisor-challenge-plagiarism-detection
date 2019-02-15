# Plagiarism Detection

### A command-line program that performs plagiarism detection using a N-tuple comparison algorithm allowing for synonyms in the text.

### Input arguments:
**Mandatory:**
  1. Synonym file, a file containing a list of synonyms.
  2. Input File 1
  3. Input File 2
  
**Optional:**
  1. The tuple size, N. (N = 3, default)
  
**Usage example:**
```
default tuple size -
python plagiarism-detecotor.py syns.txt file1.txt file2.txt

tuple size defined -
python plagiarism-detecotor.py syns.txt file1.txt file2.txt -n 5
```

### Examples:

**Example 1:**
```
syns.txt:
run sprint jog

file1.txt:
go for a run

file2.txt:
go for a jog

> python syns.txt file1.txt file2.txt

Output:
100%

Explanation:
N = 3
Tuples from file 1: ['go for a', 'for a run']
Tuples from file 2: ['go for a', 'for a jog']
Matching Tuples: 2/2 = 100%
```


**Example 2:**
```
syns.txt:
run sprint jog

file1.txt:
go for a run

file2.txt:
went for a jog

> python syns.txt file1.txt file2.txt

Output:
50%

Explanation:
N = 3
Tuples from file 1: ['go for a', 'for a run']
Tuples from file 2: ['went for a', 'for a jog']
Matching Tuples: 1/2 = 50%
```

---

### Summary:
1. Parses the command line arguments using ```argparse```. Check Usage examples on how to run the program.
2. Creates the synonym dictionary mapping each word to the first word synonym in the line.
3. Creates a tuple lists for words in file1 and file2.
4. Convert tuple list for file2 to a set for constant lookup.
5. Checks matches in tuple list for file 1 in the set created for file2.

#### Time Complexity:
```
step 1. O(1)
step 2. O(number of words in syns.txt), say O(syn)
step 3. O(2 * number of words in file1.txt + O(2 * number of words in file2.txt), say O(f1) + O(f2)
step 4. O(number of tuples in tuples_list2), ~ O(f2)
step 5. O(number of tuples in tuples_list1), ~ O(f1)

Therefore the time complexity is 
O(syn) + O(f1) + O(f2) + O(f1) + O(f2),
which reduces to O(syn + f1 + f2)
```

---

### Assumptions:
1. Number of occurences of a tuple is not tracked, ie every time a tuple from one file is present in the other file, it counts as plagiarism.
2. The plagiarism percent is based off the file with most number of tuples.
#### For example
```
N = 3
file1 = 'go for a run'and file2 = 'go for a jog when'
since files1 produces 2 tuples and file2 produces 3 tuples.
Therefore, Plagiarism percent = matches/maxaximum tuple size of both files = (2 /3)*100 = 66.67%
```
3. Numbers can be considered as words and will be added to the tuples set created for file2.
#### For example
```
N = 3
files1 = 'I had 3 desserts' and file2 = 'I had 3 sweets'
This produces Tuple Lists as ['I had 3','had 3 sushis'] and ['I had 3','had 3 sweets'] with a 50% plagiarism.
```
4. Sentence punctuations are removed from the start and end of words. So, 'j-og' and 'jog' are two different words, but ',jog', 'jog.' and 'jog' are the same word.

---

### Error Handling :
1. **N out of bounds**: N hould be greater than the minimum number of words in both the files.
2. **N cannot be negative**: N should be less than 0.
3. **If either file is empty**: both files should generate valid tuples.
4. **Incorrect arguments**: handled by argparse.
