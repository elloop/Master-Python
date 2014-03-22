/*
 * 用法：
 * 1. 创建一个stash : Stash stash;
 * 2. 把要存放的指针放入栈顶 : stash.push(new X());
 * 3. 返回栈顶指针，同时弹栈 : X * px = (X*)stash.pop();
 * 4. 去栈顶元素，不弹栈 : X * px = (X*)stash.peek();
 * 5. 清空栈 : stash.cleanup();
 * =====================================================================================
 *        Class:  Stash
 *  Description:  a container simulates a link stack
 * =====================================================================================
 */

#ifndef  STASH_H_INC
#define  STASH_H_INC

class Stash {
public:
	Stash ();
	~Stash();

	void * pop();
	void * peek();
	void push ( void * data );
	void cleanup();

protected:
	struct Link {
		void * data;
		Link * link;
		void initialize ( void * data, Link * link );
	} * head;

}; /* -----  end of class Stash  ----- */

#endif   /* ----- #ifndef STASH_H_INC  ----- */
