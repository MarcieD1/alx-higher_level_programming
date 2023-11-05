#ifndef LISTS_H
#define LISTS_H

#include <stddef.h>

/* Structure for singly linked list */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/* Function prototypes */
size_t print_listint(const listint_t *h);
int element_at(const listint_t *head, unsigned int index);
listint_t *replace_in_list(listint_t *head, unsigned int index, int value);
void print_reversed_list_integer(const listint_t *head);
listint_t *new_in_list(const listint_t *head, int index, int value);
char *no_c(char *str);
void print_matrix_integer(const int (*matrix)[3]);
int *add_tuple(const int *tuple_a, const int *tuple_b);
int multiple_returns(char *sentence, int *length, char *first);
int max_integer(const int *array, int size);
int *divisible_by_2(const int *array, int size);
int *delete_at_index(int *array, unsigned int size, unsigned int index);
void switch_integers(int *a, int *b);
int is_palindrome(listint_t **head);

#endif /* LISTS_H */
