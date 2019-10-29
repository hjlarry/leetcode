package linklist

import "testing"

func TestSingleLinkList(t *testing.T) {
	alist := NewSingleLinkList(10)
	for i := 0; i < 10; i++ {
		alist.append(i)
	}
	t.Log(alist.elements())
	t.Log(alist.findByIndex(3))
	t.Log(alist.insert(5, 22))
	t.Log(alist.insert(5, 33))
	t.Log(alist.elements())
	t.Log(alist.remove(10))
	t.Log(alist.appendLeft(88))
	t.Log(alist.elements())
}
