/*
 * @lc app=leetcode id=95 lang=golang
 *
 * [95] Unique Binary Search Trees II
 *
 * https://leetcode.com/problems/unique-binary-search-trees-ii/description/
 *
 * algorithms
 * Medium (35.56%)
 * Likes:    1274
 * Dislikes: 115
 * Total Accepted:    141.8K
 * Total Submissions: 393.6K
 * Testcase Example:  '3'
 *
 * Given an integer n, generate all structurally unique BST's (binary search
 * trees) that store values 1 ... n.
 *
 * Example:
 *
 *
 * Input: 3
 * Output:
 * [
 * [1,null,3,2],
 * [3,2,null,1],
 * [3,1,null,null,2],
 * [2,1,3],
 * [1,null,2,null,3]
 * ]
 * Explanation:
 * The above output corresponds to the 5 unique BST's shown below:
 *
 * ⁠  1         3     3      2      1
 * ⁠   \       /     /      / \      \
 * ⁠    3     2     1      1   3      2
 * ⁠   /     /       \                 \
 * ⁠  2     1         2                 3
 *
 *
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
package golang

func genTree(first int, last int) []*TreeNode {
	if first > last {
		return []*TreeNode{nil}
	}
	trees := make([]*TreeNode, 0, last-first+1)
	for i := first; i <= last; i++ {
		leftTree := genTree(first, i-1)
		rightTree := genTree(i+1, last)

		for j := 0; j < len(leftTree); j++ {
			for k := 0; k < len(rightTree); k++ {
				node := &TreeNode{Val: i}
				node.Left = leftTree[j]
				node.Right = rightTree[k]
				trees = append(trees, node)
			}
		}
	}
	return trees
}

func generateTrees(n int) []*TreeNode {
	if n == 0 {
		return nil
	}
	return genTree(1, n)
}

// @lc code=end
