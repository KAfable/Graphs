## Problem Statement

Alex wants to paint a picture but hates taking the brush off the canvas. In one stroke, Alex can only paint the same colored cells which are joined via some edge.

Given the painting, determine the minimum number of strokes to completely paint the picture.

Take for example, the canvas with height given by `h = 3` and width given by `w = 5` is to be painted with picture `picture=[“aabba”, “aabba”, “aaaca”]`, the diagram below shows the 4 strokes needed to paint the canvas.

```Strokes
Canvas  1   2  3 4
aabba   aa  bb   a
aabba   aa  bb   a
aaaca   aaa    c a
```

## Function Description

Complete the function strokesRequired in the editor below. The function must return an integer, the minimum number of strokes required to paint the canvas.
strokesRequired has the following parameter(s):

`picture[picture[0],…picture[h-1]]:` an array of strings where each string represents one row of the picture to be painted

**Constraints**

```1 ≤ h ≤ 105
1 ≤ w ≤ 105
1 ≤ h*w ≤ 105

len(picture[i]) = w (where 0 ≤ i < h)
picture[i][j] = {‘a’, ‘b’, ‘c’} (where 0 ≤ i < h and 0 ≤ j < w)
```

**Sample Input For Custom Testing**

```3
aaaba
ababa
aaaca
```

**Sample Output**
`5`

**Explanation**
The ‘a’s can be painted in 2 strokes, ‘b’s in 2 strokes and ‘c’ in 1 stroke, for a total of 5.

```py
       Strokes
Canvas  1   2 3 4 5
aaaba  aaa    b   a
ababa  a a  b b   a
aaaca  aaa      c a
```
