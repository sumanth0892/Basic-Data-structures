#include <iostream>
#include <cstring>
#include <string>
using namespace std;

struct node {
	int data;
	node *next;
};

class linked_list{
private:
	int size = 0;
	node *head,*tail;
public:
	linked_list()
	{
		head = NULL;
		tail = NULL;
	}
	~linked_list()
	{}

	void add_node(int n)
	{
		node *temp = new node;
		temp->data = n;
		temp->next = NULL;
		if (head == NULL)
		{
			head = temp;
			tail = temp;
		}
		else
		{
			tail->next = temp;
			tail = tail->next;
		}
	}	size += 1;

	void before (int n)
	{
		node *temp = new node;
		temp->data = n;
		temp->next = head;
		head = temp;
		size += 1;
	}

	void insert(int n, node *a)
	{
		node *temp = new node;
		temp->data = n;
		temp->next = a->next;
		a->next = temp;
		size += 1;
	}

	void del_node(node *previous)
	{
		node *temp;
		temp = previous->next;
		previous->next = temp->next;
		size -= 1;
		delete temp;
	}

	static void concatenate(node *a,node *b)
	{
		if (a!=NULL && b!=NULL)
		{
			if (a->next == NULL)
			{
				a->next = b;
			}
			else
			{
				concatenate(a->next,b);
			}
		}
		else
		{
			cout<<"One or more of the lists is empty"<<endl;
		}
	}
};

int main()
{
	//Write the driver code to test this
	return 0;
}