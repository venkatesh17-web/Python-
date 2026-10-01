questions = [
        ["Q1. Which data structure follows the LIFO principle? ", "Queue", "Stack", "Array", "Linked List", 2],
        ["Q2. Which data structure follows the FIFO principle? ", "Stack", "Tree", "Queue", "Graph", 3],
        ["Q3. What is the time complexity of accessing an element in an array using its index? ", "O(n)", "O(log n)", "O(1)", "O(n²)", 3],
        ["Q4. Which data structure consists of nodes connected by pointers? ", "Array", "Linked List", "Stack", "Hash Table", 2],
        ["Q5. Which operation is used to add an element to a stack? ", "Enqueue", "Insert", "Push", "Pop", 3],
        ["Q6. Which operation removes an element from a stack? ", "Push", "Pop", "Enqueue", "Delete", 2],
        ["Q7. Which operation is used to add an element to a queue? ", "Push", "Pop", "Enqueue", "Delete", 3],
        ["Q8. Which operation removes an element from a queue? ", "Enqueue", "Push", "Insert", "Dequeue", 4],
        ["Q9. Which data structure is commonly used to implement recursion? ", "Queue", "Stack", "Graph", "Heap", 2],
        ["Q10. Which traversal visits the Root → Left → Right nodes in a binary tree? ", "Inorder", "Postorder", "Preorder", "Level Order", 3],
        ["Q11. Which traversal visits Left → Root → Right in a binary tree? ", "Preorder", "Inorder", "Postorder", "Level Order", 2],
        ["Q12. Which traversal visits Left → Right → Root in a binary tree? ", "Inorder", "Preorder", "Level Order", "Postorder", 4],
        ["13. Which data structure is used in Breadth-First Search (BFS)? ", "Stack", "Queue", "Heap", "Array", 2],
        ["Q14. Which data structure is commonly used in Depth-First Search (DFS)? ", "Queue", "Stack", "Hash Table", "Heap", 2],
        ["Q15. What is the worst-case time complexity of searching for an element in an unsorted array? ", "O(1)", "O(log n)", "O(n)", "O(n²)", 3],
        ["Q16. Which data structure is most suitable for representing hierarchical data? ", "Stack", "Queue", "Tree", "Array", 3]

]

levels = [5000, 10000, 15000, 20000, 25000, 50000, 100000, 200000, 300000, 500000, 750000, 1250000, 2500000, 5000000, 10000000, 70000000]
money = 0
for i in range(0, len(questions)):
    question = questions[i]

    print(f"\n{question[0]}")
    print(f"Question for Rs {levels[i]}")

    print(f"a. {question[1]}           b. {question[2]} ")
    print(f"c. {question[3]}           d. {question[4]}")

    reply = int(input("Enter Your Answer (1-4) or 0 to quit"))

    if reply == 0:
        print(f"You are taking home Rs {money}")
        break
    if(reply == question[-1]):
        print(f"Correct ansewer, you have won Rs. {levels[i]}")
        if(i == 4):
            money = 25000
        elif(i == 9):
            money = 500000
        elif(i == 15):
            money = 70000000
    else:
        print("Wrong answer")
        break

print(f"\nYou are takeing home Rs. {money}")