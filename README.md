# Sprint Challenge: Hash Tables

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This challenge allows you to practice the concepts and techniques learned over the past sprint and apply them in a concrete project. This sprint explored hash tables. During this sprint, you studied hash functions, collision resolution, complexity analysis of hash tables, load factor, resizing, and various use cases for hash tables. In your challenge this week, you will demonstrate mastery of these skills by solving five problems related to hash tables.

The sprint challenge is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the sprint challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your TL if you need direction.

_You have **three hours** to complete this challenge. Plan your time accordingly._

## Introduction

This challenge requires you to solve algorithm problems that are amenable to being solved efficiently with a hash table.

### Commits

Commit your code regularly and meaningfully. This practice helps both you (in case you ever need to return to old code for any number of reasons) and your Team Lead as they evaluate your solution.

## Interview Questions

Be prepared to demonstrate your understanding of this week's concepts by answering questions on the following topics. You might prepare by writing down your answers beforehand.

1. Hashing functions
    A hashing function is any function that can be used to map arbitrarily-sized data to fixed-size values. It takes an input as a key, which is associated with a datum or record and used to identify it, and may be of fixed length, like an integer, or variable length, like a name. The output is a hash code used to index a hash table holding the data or records, or pointers to them.

2. Collision resolution
    Collision resolution, wherein two items hash to the same slot (the collision), is a systematic method  for placing the second item in the hash table, such as separate chaining, open addressing techniques, linear probing, etc.

3. Performance of basic hash table operations
    The average performance of hash table operations is constant time (O(1)). Worst-case scenarios, with more collisions, can result in performance of linear time (O(n)).
4. Load factor
    Load factor is the ratio of pieces of data to cells in the hash table, with the ideal load factor being 0.7, or 7 elements / 10 cells).
5. Automatic resizing
    Resizing of a hash table, while an expensive operation, can be useful if the hash table is either too large or too small for the data to be stored. In the first case, memory is wasted, while in the second, more memory would need to be allocated to accommodate the larger space required. Resizing can be set up to happen automatically whenever the load factor becomes wither too large or too small.
6. Various use cases for hash tables
    Hash tables are good whenever you want to store a large amount of data that can be searched quickly, such as a list of students at at a large school or university, which can have over 55,000 students. Using hash tables, a student record can be found very quickly by whatever key (name, ID, etc.). Duplicate elements can also be found if, for example, a student's record was mistakenly entered twice, the same ID was issued to more than one student, or more than one student has the same name. Hash tables are also used for caching, password authentication, error-checking, etc.

We expect you to be able to answer questions in these areas. Your responses contribute to your Sprint Challenge grade.

## Instructions

### Task 1: Project Set-Up

- [ ] Create a forked copy of this project
- [ ] Add your team lead as a collaborator on Github
- [ ] Clone your OWN version of the repository (Not Lambda's by mistake!)
- [ ] Create a new branch: git checkout -b `<firstName-lastName>`.
- [ ] Implement the project on your newly created `<firstName-lastName>` branch, committing changes regularly
- [ ] Push commits: git push origin `<firstName-lastName>`

### Task 2: Project Requirements

Your finished project must include all of the following requirements:

- [ ] Solve any three of the five problems

For each problem that you choose to solve, complete the following:

- [ ] Navigate into each exercise's directory
- [ ] Read the instructions for the exercise in the README
- [ ] Implement your solution in the `.py` skeleton file
- [ ] Make sure your code passes the tests running the test script with make tests

*Note: For these exercises, we expect you to use Python's built-in `dict` as a hashtable. That said, if you wish, you can attempt to solve using your own hashtable implementation, as well. All solutions should utilize a `dict` or hashtable. You should not use Sets. (Though you can make a `dict` behave like a set if you wish.)*

### Task 3: Stretch Goals

After finishing your required elements, you can push your work further. These goals may or may not be things you have learned in this module, but they build on the material you just studied. Time allowing, stretch your limits, and see if you can deliver on the following optional goals:

- [ ] Solve any four of the five problems
- [ ] Solve all five problems

## Submission format

Follow these steps to complete your project.

- [ ] Submit a Pull-Request to merge <firstName-lastName> Branch into master (student's  Repo). **Please don't merge your own pull request**
- [ ] Add your team lead as a reviewer on the pull-request
- [ ] Your team lead will count the project as complete after receiving your pull-request
