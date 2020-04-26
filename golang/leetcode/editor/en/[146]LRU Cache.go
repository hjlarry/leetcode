//Design and implement a data structure for Least Recently Used (LRU) cache. It 
//should support the following operations: get and put. 
//
// get(key) - Get the value (will always be positive) of the key if the key exis
//ts in the cache, otherwise return -1. 
//put(key, value) - Set or insert the value if the key is not already present. W
//hen the cache reached its capacity, it should invalidate the least recently used
// item before inserting a new item. 
//
// The cache is initialized with a positive capacity. 
//
// Follow up: 
//Could you do both operations in O(1) time complexity? 
//
// Example: 
//
// 
//LRUCache cache = new LRUCache( 2 /* capacity */ );
//
//cache.put(1, 1);
//cache.put(2, 2);
//cache.get(1);       // returns 1
//cache.put(3, 3);    // evicts key 2
//cache.get(2);       // returns -1 (not found)
//cache.put(4, 4);    // evicts key 1
//cache.get(1);       // returns -1 (not found)
//cache.get(3);       // returns 3
//cache.get(4);       // returns 4
// 
//
// 
// Related Topics Design

package main

// 一、双向链表加哈希表的解决方案
//type Node struct {
//	key   int
//	value int
//	prev  *Node
//	next  *Node
//}
//type LRUCache struct {
//	cap  int
//	head *Node
//	tail *Node
//	keys map[int]*Node
//}
//
//func Constructor(capacity int) LRUCache {
//	cache := LRUCache{
//		cap:  capacity,
//		keys: make(map[int]*Node),
//	}
//	cache.head = &Node{}
//	cache.tail = &Node{}
//	cache.head.next = cache.tail
//	cache.tail.prev = cache.head
//	return cache
//}
//
//func (this *LRUCache) Get(key int) int {
//	node, exist := this.keys[key]
//	if !exist {
//		return -1
//	}
//
//	node.prev.next = node.next
//	node.next.prev = node.prev
//
//	this.head.next.prev = node
//	node.next = this.head.next
//	this.head.next = node
//	node.prev = this.head
//
//	return node.value
//}
//
//func (this *LRUCache) Put(key int, value int) {
//	node, exist := this.keys[key]
//	if !exist {
//		new_node := Node{
//			key:   key,
//			value: value,
//			prev:  this.head,
//			next:  nil,
//		}
//		this.keys[key] = &new_node
//		tmp := this.head.next
//		this.head.next = &new_node
//		new_node.next = tmp
//		tmp.prev = &new_node
//		if len(this.keys) > this.cap {
//			need_del := this.tail.prev
//			need_del.prev.next = this.tail
//			this.tail.prev = need_del.prev
//			delete(this.keys, need_del.key)
//		}
//	} else {
//		node.value = value
//		node.prev.next = node.next
//		node.next.prev = node.prev
//
//		this.head.next.prev = node
//		node.next = this.head.next
//		this.head.next = node
//		node.prev = this.head
//	}
//}
import "container/list"

type kv struct {
	key int
	val int
}

type LRUCache struct {
	cap  int
	data map[int]*list.Element
	hits *list.List
}

func Constructor(capacity int) LRUCache {
	cache := LRUCache{
		cap:  capacity,
		data: make(map[int]*list.Element),
		hits: list.New(),
	}
	return cache
}

func (this *LRUCache) Get(key int) int {
	node, exist := this.data[key]
	if !exist {
		return -1
	}
	this.hits.MoveToFront(node)
	return node.Value.(kv).val
}

func (this *LRUCache) Put(key int, value int) {
	node, exist := this.data[key]
	if exist{
		node.Value = kv{
			key: key,
			val: value,
		}
		this.hits.MoveToFront(node)
		return
	}

	if this.hits.Len() == this.cap{
		last := this.hits.Back()
		delete(this.data, last.Value.(kv).key)
		this.hits.Remove(last)
	}
	this.data[key] = this.hits.PushFront(kv{
		key: key,
		val: value,
	})
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
//leetcode submit region end(Prohibit modification and deletion)
