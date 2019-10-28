package linklist

type node struct {
	next  *node
	value interface{}
}

type singleLinkList struct {
	root     *node
	maxSize  int
	length   int
	tailNode *node
}

func NewSingleLinkList(maxSize int) *singleLinkList {
	sentinel := new(node)
	return &singleLinkList{
		root:     sentinel,
		maxSize:  maxSize,
		length:   0,
		tailNode: sentinel,
	}
}

func (s *singleLinkList) append(value interface{}) bool {
	if s.length > s.maxSize {
		return false
	}
	newNode := node{value: value}
	s.tailNode.next = &newNode
	s.tailNode = &newNode
	s.length++
	return true
}

func (s *singleLinkList) appendLeft(value interface{}) bool {
	if s.length > s.maxSize {
		return false
	}
	tmpNode := s.root.next
	newNode := node{next: tmpNode, value: value}
	s.root.next = &newNode
	s.length++
	return true
}

func (s *singleLinkList) insert(k int, value interface{}) bool {
	if k > s.length || k < 0 {
		return false
	}
	if k == s.length {
		return s.append(value)
	}
	if k == 0 {
		return s.appendLeft(value)
	}
	cur := s.root
	for i := 0; i < k; i++ {
		cur = cur.next
	}
	tmpNode := cur.next
	newNode := node{next: tmpNode, value: value}
	cur.next = &newNode
	s.length++
	return true
}

func (s *singleLinkList) findByIndex(k int) *node {
	if k > s.length || k < 0 {
		return nil
	}
	cur := s.root
	for i := 0; i < k; i++ {
		cur = cur.next
	}
	return cur
}

func (s *singleLinkList) remove(k int) bool {
	if k > s.length || k < 0 {
		return false
	}
	cur := s.root.next
	pre := s.root
	for i := 0; i < k; i++ {
		cur = cur.next
		pre = pre.next
	}
	if k == s.length {
		s.tailNode = pre
	}
	pre.next = cur.next
	s.length--
	return true
}
