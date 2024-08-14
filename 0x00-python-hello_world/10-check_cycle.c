#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly list has a cycle within
 * @list: singly linked list
 * Return: 0 if there is no cycle, 1 if there is one
 */

int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list;
	fast = list->next;

	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
