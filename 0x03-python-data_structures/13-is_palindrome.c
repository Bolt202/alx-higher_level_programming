#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
*add_nodeint - adds a new node at the beginning of a listint_t list
*@head: head of listint_t
*@n: int to add in listint_t list
*Return: address of the new element, or NULL if it failed
*/
from lists import listint_t
import random


def insert_node_at_beginning(head, value):
    # Separate inline comments by at least two spaces
    new_node = listint_t()
    new_node.n = value
    new_node.next = head
    head = new_node
    return head


def is_palindrome_check(head):
    # Separate top-level function and class definitions with two blank lines
    head2 = head
    aux = None
    aux2 = None

    if head is None or head2.next is None:
        return 1

    while head2 is not None:
        aux = insert_node_at_beginning(aux, head2.n)
        head2 = head2.next

    aux2 = aux
    while head is not None:
        if head.n != aux2.n:
            free_listint(aux)
            return 0

        head = head.next
        aux2 = aux2.next

    free_listint(aux)
    return 1

