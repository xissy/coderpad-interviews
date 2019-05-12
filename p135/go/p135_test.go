package main

import "testing"
import "github.com/stretchr/testify/assert"

func TestP135_1(t *testing.T) {
	root := &Node{
		Value: 10,
		Left:  nil,
		Right: nil,
	}
	assert.Equal(t, minPathSum(root), 10)
}

func TestP135_2(t *testing.T) {
	root := &Node{
		Value: 10,
		Left: &Node{
			Value: 5,
			Left:  nil,
			Right: nil,
		},
		Right: nil,
	}
	assert.Equal(t, minPathSum(root), 15)
}

func TestP135_3(t *testing.T) {
	root := &Node{
		Value: 10,
		Left:  nil,
		Right: &Node{
			Value: 5,
			Left:  nil,
			Right: nil,
		},
	}
	assert.Equal(t, minPathSum(root), 15)
}

func TestP135_4(t *testing.T) {
	root := &Node{
		Value: 10,
		Left: &Node{
			Value: 5,
			Left:  nil,
			Right: nil,
		},
		Right: &Node{
			Value: 5,
			Left:  nil,
			Right: nil,
		},
	}
	assert.Equal(t, minPathSum(root), 15)
}

func TestP135_5(t *testing.T) {
	root := &Node{
		Value: 10,
		Left: &Node{
			Value: 5,
			Left:  nil,
			Right: nil,
		},
		Right: &Node{
			Value: 5,
			Left:  nil,
			Right: &Node{
				Value: 1,
				Left:  nil,
				Right: nil,
			},
		},
	}
	assert.Equal(t, minPathSum(root), 15)
}

func TestP135_6(t *testing.T) {
	root := &Node{
		Value: 10,
		Left: &Node{
			Value: 5,
			Left:  nil,
			Right: &Node{
				Value: 2,
				Left:  nil,
				Right: nil,
			},
		},
		Right: &Node{
			Value: 5,
			Left:  nil,
			Right: &Node{
				Value: 1,
				Left:  nil,
				Right: nil,
			},
		},
	}
	assert.Equal(t, minPathSum(root), 16)
}

func TestP135_7(t *testing.T) {
	root := &Node{
		Value: 10,
		Left: &Node{
			Value: 5,
			Left:  nil,
			Right: &Node{
				Value: 2,
				Left:  nil,
				Right: nil,
			},
		},
		Right: &Node{
			Value: 5,
			Left:  nil,
			Right: &Node{
				Value: 1,
				Left: &Node{
					Value: -1,
					Left:  nil,
					Right: nil,
				},
				Right: nil,
			},
		},
	}
	assert.Equal(t, minPathSum(root), 15)
}
