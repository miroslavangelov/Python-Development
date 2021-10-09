from collections import deque

pizzas_deque = deque(map(int, input().split(', ')))
employees_deque = deque(map(int, input().split(', ')))
employees_deque.reverse()
total_pizzas = 0
pizzas = list(pizzas_deque)
employees = list(employees_deque)

for i in range(0, len(employees)):
    employee = employees[i]

    for j in range(0, len(pizzas)):
        pizza = pizzas[j]

        if pizza > 10 or pizza <= 0:
            if pizza in pizzas_deque:
                pizzas_deque.remove(pizza)
            continue

        if pizza <= employee:
            if pizza in pizzas_deque:
                pizzas_deque.remove(pizza)
            if employee in employees_deque:
                employees_deque.remove(employee)
            total_pizzas += pizza
            pizzas[j] = 0
        else:
            pizzas[j] -= employee
            if employee in employees_deque:
                employees_deque.remove(employee)
            if pizza in pizzas_deque:
                pizzas_deque.popleft()
                pizzas_deque.appendleft(pizzas[j])
            total_pizzas += employee
        break

employees_deque.reverse()

if len(pizzas_deque) > 0:
    pizzas_as_string = ', '.join(map(str, pizzas_deque))
    print('Not all orders are completed.\n' +
          f'Orders left: {pizzas_as_string}')
else:
    employees_as_string = ', '.join(map(str, employees_deque))
    print('All orders are successfully completed!\n' +
          f'Total pizzas made: {total_pizzas}\n' +
          f'Employees: {employees_as_string}')
