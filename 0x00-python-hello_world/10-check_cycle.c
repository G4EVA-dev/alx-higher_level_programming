#include "lists.h"

/**
 * check_cycle - This  checks if the linked list contains a cycle
 * @list: This is the linked list to be checke
 *
 * Return: 1 if cycle is present, 0 if absent 
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}

