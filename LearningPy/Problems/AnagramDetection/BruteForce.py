# coding=utf-8
'''
A brute force technique for solving a problem typically tries to exhaust all possibilities. For the anagram detection problem, we can simply
generate a list of all possible strings using the characters from s1 and then see if s2 occurs. However, there is a difficulty with this approach.
When generating all possible strings from s1, there are n possible first characters, n−1n−1 possible characters for the second position,
n−2 for the third, and so on. The total number of candidate strings is nx(n−1)x(n−2)x...x3x2x1, which is n!. Although some of the
strings may be duplicates, the program cannot know this ahead of time and so it will still generate n!n! different strings.

It turns out that n!n! grows even faster than 2n2n as n gets large. In fact, if s1 were 20 characters long, there would be
20!=2,432,902,008,176,640,00020 possible candidate strings. If we processed one possibility every second, it would
still take us 77,146,816,596 years to go through the entire list. This is probably not going to be a good solution.

'''