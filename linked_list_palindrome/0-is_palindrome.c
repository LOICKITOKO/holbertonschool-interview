#include "lists.h"
#include <stdlib.h>

/**
 * reverse_list - Reverses a linked list
 * @head: Pointer to the head of the list
 * Return: New head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
    listint_t *prev = NULL, *current = head, *next;

    while (current)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return (prev);
}

/**
 * compare_lists - Compares two linked lists
 * @head1: First list
 * @head2: Second list
 * Return: 1 if identical, 0 otherwise
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
    while (head1 && head2)
    {
        if (head1->n != head2->n)
            return (0);
        head1 = head1->next;
        head2 = head2->next;
    }
    return (1);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Double pointer to head of list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head;
    listint_t *second_half, *prev_slow = NULL;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    // Find midpoint using slow/fast pointers
    while (fast && fast->next)
    {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    // For odd-sized list, skip middle node
    if (fast)
        slow = slow->next;

    second_half = reverse_list(slow);
    prev_slow->next = NULL;

    if (!compare_lists(*head, second_half))
    {
        reverse_list(second_half); // optional: restore original list
        return (0);
    }

    reverse_list(second_half); // optional: restore original list
    return (1);
}
