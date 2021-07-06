Implement Stack Using List


```python
stack = []
def push_element():
    element = input("enter the element: ")
    stack.append(element)
    print(stack)
    
def pop_element():
    if not stack:
        print("stack is empty")
    else:
        stack.pop()
        print(stack)
    
while True:
    print("select the operation 1.push 2.pop 3.quit")
    choice = int(input())
    if choice == 1:
        push_element()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("Enter the correct operation")
```

    select the operation 1.push 2.pop 3.quit
    1
    enter the element: 20
    ['20']
    select the operation 1.push 2.pop 3.quit
    1
    enter the element: 30
    ['20', '30']
    select the operation 1.push 2.pop 3.quit
    1
    enter the element: 40
    ['20', '30', '40']
    select the operation 1.push 2.pop 3.quit
    1
    enter the element: 50
    ['20', '30', '40', '50']
    select the operation 1.push 2.pop 3.quit
    3
    

Implement Stack Using List with stack length


```python
stack = []
def push_element():
    if len(stack) == number:
        print("list is full")
    else:
        element = input("enter the element: ")
        stack.append(element)
        print(stack)
        
def pop_element():
    if not stack:
        print("stack is empty")
    else:
        stack.pop()
        print(stack)
        

number = int(input("enter the length of stacK: "))    
while True:
    print("select the operation 1.push 2.pop 3.quit")
    choice = int(input())
    if choice == 1:
        push_element()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("Enter the correct operation")
```

    enter the length of stacK: 3
    select the operation 1.push 2.pop 3.quit
    1
    enter the element: 20
    ['20']
    select the operation 1.push 2.pop 3.quit
    1
    enter the element: 30
    ['20', '30']
    select the operation 1.push 2.pop 3.quit
    1
    enter the element: 30
    ['20', '30', '30']
    select the operation 1.push 2.pop 3.quit
    1
    list is full
    select the operation 1.push 2.pop 3.quit
    3
    


```python

```


```python

```


```python

```
