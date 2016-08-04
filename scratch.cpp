/*
 *
 * Linked list of integers
 *
 * Private variables: 
 *  - Node *head;
 * 
 */

struct Node {
    int data;
    Node *next;
};


List::List()
{
}

void List::print()
{
    print(head);
}

void List::print(Node *node)
{
    if (node == NULL) /* Base Case */
        return;

    cout << node->data << '\n';
    print(node->next); /* Recursive Call */
}


void List::print_reverse(Node *node)
{
    if (node == NULL) /* Base Case */
        return;

    print(node->next); /* Recursive Call */
    cout << node->data << '\n';
}


