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
python main.py syns.txt file1.txt file2.txt 2
```

---

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
