#include <stdio.h>
#include <stdlib.h>

typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list)
{
    listint_t *slow = list;
    listint_t *fast = list;

    if (!list)
        return 0;

    while (slow && fast && fast->next)
    {
        slow = slow->next;
        fast = fast->next->next;

        if (slow == fast)
            return 1;
    }

    return 0;
}

int main(void)
{
    // Create a sample linked list
    listint_t *head = malloc(sizeof(listint_t));
    listint_t *second = malloc(sizeof(listint_t));
    listint_t *third = malloc(sizeof(listint_t));

    head->n = 1;
    head->next = second;

    second->n = 2;
    second->next = third;

    third->n = 3;
    third->next = NULL;

    // Create a cycle in the linked list
    third->next = second;

    // Check if the linked list contains a cycle
    int hasCycle = check_cycle(head);

    if (hasCycle)
        printf("The linked list contains a cycle.\n");
    else
        printf("The linked list does not contain a cycle.\n");

    // Free the memory allocated for the linked list
    free(head);
    free(second);
    free(third);

    return 0;
}
