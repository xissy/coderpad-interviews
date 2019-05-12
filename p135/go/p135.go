package main

import "fmt"
import "math"

type Node struct {
	Value int
	Left  *Node
	Right *Node
}

type NodeWithSum struct {
	Node *Node
	Sum  int
}

func (n *Node) String() string {
	return fmt.Sprintf("<Node value=%d, left=%v, right=%v>", n.Value, n.Left, n.Right)
}

func minPathSum(root *Node) int {
	var queue []*NodeWithSum
	queue = append(queue, &NodeWithSum{
		Node: root,
		Sum:  root.Value,
	})
	min := math.MaxInt64

	for len(queue) > 0 {
		nodeWithSum := queue[0]
		queue = queue[1:]

		node := nodeWithSum.Node
		currSum := nodeWithSum.Sum

		if node.Left == nil && node.Right == nil {
			if currSum < min {
				min = currSum
			}
			continue
		}

		if node.Left != nil {
			queue = append(queue, &NodeWithSum{
				Node: node.Left,
				Sum:  currSum + node.Left.Value,
			})
		}
		if node.Right != nil {
			queue = append(queue, &NodeWithSum{
				Node: node.Right,
				Sum:  currSum + node.Right.Value,
			})
		}
	}

	return min
}
