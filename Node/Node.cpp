#include "Node.h"
#include <iostream>
using namespace std;

Node::Node(){
    this->data = -1;
    this->next = nullptr;
}

Node::Node(int data){
    this->data = data;
    this->next = nullptr;
}

int Node::getData(){
    return this->data;
}

Node *Node::getNext(){
    return this->next;
}
void Node::setData(int data){
    this->data = data;
}
void Node::setNext(Node *next){
    this->next = next;
}

int main(){
    Node node1(1);
    Node node2(2);
    Node node3(3);
    Node node4(4);
    node1.setNext(&node2);
    node2.setNext(&node3);
    node3.setNext(&node4);
    Node *tmp = &node1;
    while (tmp){
        cout << tmp->getData() << endl;
        tmp = tmp->getNext();
    }
    return 0;
}

