#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int aux_palind(listint_t **head, listint_t *end);

int is_palindrome(listint_t **head)
{
    if (head == NULL || *head == NULL)
        return (1);
    return (aux_palind(head, *head));
}

/**
 * aux_palind - checks if a sublist is a palindrome
 * @head: pointer to the head of the linked list.
 * @end: pointer to the end of the linked list.
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int aux_palind(listint_t **head, listint_t *end)
{
    if (end == NULL)
        return (1);

    if (aux_palind(head, end->next) && (*head)->n == end->n)
    {
        *head = (*head)->next;
        return (1);
    }

    return (0);
}
