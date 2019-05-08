#include "lists.h"
/**
 * palindrome - check if a array is a palindrome
 * @pal: the array to check
 * @len: the len of the array
 * Return: 1 if is true, 0 is false
 */
int palindrome(int *pal, size_t len)
{
	size_t i = 0;
	size_t j = 0;

	if (pal == NULL)
		return (1);
	j = len - 1;
	while (i < j)
	{
		if (pal[i] != pal[j])
		{
			return (0);
		}
		i++;
		j--;
	}
	return (1);
}
/**
 * is_palindrome - check if a data of a linked list of ints is palindrome
 * @head: the pointer to the list
 *
 * Return: 1 if is palindrom, 0 otherweise
 */
int is_palindrome(listint_t **head)
{
	int *pal = NULL;
	size_t len;
	listint_t *aux;
	int val;
	int i = 0;

	if (*head == NULL)
		return (1);
	aux = *head;
	len = listint_len(*head);
	pal = malloc(sizeof(int) * len);
	while (aux != NULL)
	{
		pal[i] = aux->n;
		aux = aux->next;
		i++;
	}
	val = palindrome(pal, len);
	free(pal);
	return (val);

}
/**
 * listint_len - count the amount of members in a list
 * @h: the pointer to the list
 *
 * Return: the number of elements of the list
 */
size_t listint_len(const listint_t *h)
{
	int n = 0;

	if (h != NULL)
	{
		if (h->next == NULL)
			return (++n);
		n = listint_len(h->next);
		return (++n);
	}
	return (n);
}
