#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: node structure for a singly linked list
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/**
 * print_listint - prints all the elements of a linked list
 * @h: pointer to the head of the list
 *
 * Return: the number of nodes in the list
 */
size_t print_listint(const listint_t *h);

/**
 * add_nodeint - adds a new node at the beginning of a linked list
 * @head: pointer to the head of the list
 * @n: integer to be added to the new node
 *
 * Return: pointer to the newly added node
 */
listint_t *add_nodeint(listint_t **head, const int n);

/**
 * free_listint - frees a linked list
 * @head: pointer to the head of the list
 */
void free_listint(listint_t *head);

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: pointer to the head of the list
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list);

#endif /* LISTS_H */
