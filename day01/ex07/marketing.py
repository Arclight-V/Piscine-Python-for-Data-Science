import sys

def call_center(clients, recipients):
    return list(set(clients) - set(recipients))
def potential_clients(participants, clients):
    return list(set(participants) - set(clients))
def loyalty_program(clients, participants):
    return list(set(clients) - set(participants))

def marketing(command):
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    if (command == "call_center"):
        print(call_center(clients, recipients))
    elif (command == "potential_clients"):
        print(potential_clients(participants, clients))
    else:
        print(loyalty_program(clients, participants))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception('Error! There is no function as an argument')
    if  sys.argv[1] != 'call_center' and sys.argv[1] != 'potential_clients' and sys.argv[1] != 'loyalty_program' :
        raise Exception('Error! available functions: call_center, potential_clients, loyalty_program')
    marketing(sys.argv[1])
