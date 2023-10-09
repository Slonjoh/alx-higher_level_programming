#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to a pointer to the head of the list.
 * Return: 1 if it is a palindrome, 0 if it is not.
 */

int is_palindrome(listint_t **head)
{
    listint_t *slow, *fast, *prev, *second_half, *temp;
    int is_palindrome = 1;

    if (head == NULL || *head == NULL)
        return (1);

    slow = *head;
    fast = *head;
    prev = NULL;

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    if (fast != NULL)
    {
        slow = slow->next;
    }

    second_half = slow;

    while (prev != NULL && second_half != NULL)
    {
        if (prev->n != second_half->n)
        {
            is_palindrome = 0;
            break;
        }
        prev = prev->next;
        second_half = second_half->next;
    }
    prev = NULL;
    while (slow != NULL)
    {
        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    return is_palindrome;
}
