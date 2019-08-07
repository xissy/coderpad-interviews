# Problem 135 [Easy]

This question was asked by Apple.

Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

```
  10
 /  \
5    5
 \     \
   2    1
       /
     -1
```

---

애플에서 출제된 문제입니다.

주어진 이진 트리에서, 루트 (최상위 노드) 에서 리프 (자식이 없는 최하위 노드) 까지의
경로를 모두 더하였을 떄 가장 작은 값을 갖는 경로를 찾고, 그 합을 반환하세요.

예를 들어, 이 트리에서 최소 값을 갖는 경로는 `[10, 5, 1, -1]` 이며, 그 합인 `15`를 반환해야 합니다.

```
  10
 /  \
5    5
 \     \
   2    1
       /
     -1
```