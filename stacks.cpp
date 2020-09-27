#include <iostream>
#include <cmath>
using namespace std;
const int MAX = 100;

class Stack{
private:
	size = 0;
	int stack[MAX];
public:
	Stack()
	{top = 0;}
	~Stack()
	{}
	void push(int n)
	{
		stack[top++] = n;
		size += 1;
	}
	int pop(int n)
	{	
		size -= 1;
		return stack[top--];
	}
	int getSize()
	{
		return size;
	}
	void display()
	{
		for (int i=0;i<size;i++)
		{
			cout<<stack[i]<<endl;
		}
	}
	bool search(int n)
	{
		for (int i = 0;i<size;i++)
		{
			if (stack[i] == n)
			{
				return true;
			}
		}
		return false;
	}

};