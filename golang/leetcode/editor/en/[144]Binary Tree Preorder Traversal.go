//Given a binary tree, return the preorder traversal of its nodes' values. 
//
// Example: 
//
// 
//Input: [1,null,2,3]
//   1
//    \
//     2
//    /
//   3
//
//Output: [1,2,3]
// 
//
// Follow up: Recursive solution is trivial, could you do it iteratively? 
// Related Topics Stack Tree

//leetcode submit region begin(Prohibit modification and deletion)
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
package main

func preorderTraversal(root *TreeNode) []int {
	res := []int{}
	helper(root, &res)
	return res
}

func helper(node *TreeNode, res *([]int)) {
	if node != nil {
		*res = append(*res, node.Val)
		helper(node.Left, res)
		helper(node.Right, res)
	}
}

//leetcode submit region end(Prohibit modification and deletion)
