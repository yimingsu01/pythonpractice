from polynomial_adt.polynode import Polynode
import math
class Polynomial():
    degree = 0
    polyHead = None

    def __init__(self, degree = 0, coefficient = 0):
        self.polyHead = Polynode(degree, coefficient)

    def count_degree(self):
        if self.polyHead is None:
            return -1
        else:
            max = 0
            temp_node = self.polyHead
            while temp_node is not None and temp_node.coefficient != 0:
                if temp_node.degree > max:
                    max = temp_node.degree
                temp_node = temp_node.nextNode
            self.degree = max
            return max

    def getitem(self, degree):
        temp_node = self.polyHead
        temp_list = []
        coefficient = 0
        while temp_node is not None and temp_node.coefficient != 0:
            if temp_node.degree == degree:
                temp_list.append(temp_node)
            temp_node = temp_node.nextNode
        for nodes in temp_list:
            coefficient += nodes.coefficient
        return coefficient

    def evaluate(self, scalar):
        sum = 0
        temp_node = self.polyHead
        while temp_node is not None and temp_node.coefficient != 0:
            temp = math.pow(scalar, temp_node.degree)
            temp = temp * temp_node.coefficient
            sum += temp
            temp_node = temp_node.nextNode
        return sum

    def add(self, rhsPolynomial):
        if self.polyHead is None or rhsPolynomial.polyHead is None:
            return -1
        else:
            new_poly = 0
            temp_node = self.polyHead
            while temp_node.nextNode is not None and temp_node.nextNode.coefficient != 0:
                temp_node = temp_node.nextNode
            temp_node.nextNode = rhsPolynomial.polyHead
            max_degree = max(self.degree, rhsPolynomial.degree)
            i = 0
            while i <= max_degree:
                node_list = []
                traverse_node = self.polyHead
                while traverse_node is not None and traverse_node.coefficient != 0:
                    if traverse_node.degree == i:
                        node_list.append(traverse_node)
                    traverse_node = traverse_node.nextNode
                coefficient_sum = 0
                for nodes in node_list:
                    coefficient_sum += nodes.coefficient
                if i == 0:
                    new_poly = Polynomial(i, coefficient_sum)
                else:
                    temp_node2 = new_poly.polyHead
                    while temp_node2.nextNode is not None and temp_node2.nextNode.coefficient != 0:
                        temp_node2 = temp_node2.nextNode
                    temp_node2.nextNode = Polynode(i, coefficient_sum)
                i += 1
            return new_poly

    def subtract(self, rhsPolynomial):
        if self.polyHead is None or rhsPolynomial.polyHead is None:
            return -1
        else:
            new_poly = 0

            rhs_node = rhsPolynomial.polyHead
            while rhs_node is not None and rhs_node.coefficient != 0:
                rhs_node.coefficient = -rhs_node.coefficient
                rhs_node = rhs_node.nextNode

            temp_node = self.polyHead
            while temp_node.nextNode is not None and temp_node.nextNode.coefficient != 0:
                temp_node = temp_node.nextNode
            temp_node.nextNode = rhsPolynomial.polyHead

            max_degree = max(self.degree, rhsPolynomial.degree)
            i = 0
            while i <= max_degree:
                node_list = []
                traverse_node = self.polyHead
                while traverse_node is not None and traverse_node.coefficient != 0:
                    if traverse_node.degree == i:
                        node_list.append(traverse_node)
                    traverse_node = traverse_node.nextNode
                coefficient_sum = 0
                for nodes in node_list:
                    coefficient_sum += nodes.coefficient
                if i == 0:
                    new_poly = Polynomial(i, coefficient_sum)
                else:
                    temp_node2 = new_poly.polyHead
                    while temp_node2.nextNode is not None and temp_node2.nextNode.coefficient != 0:
                        temp_node2 = temp_node2.nextNode
                    temp_node2.nextNode = Polynode(i, coefficient_sum)
                i += 1
            return new_poly

    def multiply(self, rhsPolynomial):
        new_poly = 0
        node1 = self.polyHead
        i = True
        while node1 is not None and node1.coefficient != 0:
            node2 = rhsPolynomial.polyHead
            while node2 is not None and node2.coefficient != 0:
                coefficient = node1.coefficient * node2.coefficient
                degree = node1.degree + node2.degree
                if i:
                    new_poly = Polynomial(degree, coefficient)
                    i = False
                else:
                    temp_node = new_poly.polyHead
                    while temp_node.nextNode is not None and temp_node.nextNode.coefficient != 0:
                        temp_node = temp_node.nextNode
                    temp_node.nextNode = Polynode(degree, coefficient)
                node2 = node2.nextNode
            node1 = node1.nextNode
        return new_poly

    def uniteliketerms(self):
        new_poly = 0
        max_degree = self.degree
        i = 0
        while i <= max_degree:
            node_list = []
            traverse_node = self.polyHead

            while traverse_node is not None and traverse_node.coefficient != 0:
                if traverse_node.degree == i:
                    node_list.append(traverse_node)
                traverse_node = traverse_node.nextNode

            coefficient_sum = 0
            for nodes in node_list:
                coefficient_sum += nodes.coefficient

            if coefficient_sum != 0:
                if new_poly == 0:
                    new_poly = Polynomial(i, coefficient_sum)
                else:
                    temp_node2 = new_poly.polyHead
                    while temp_node2.nextNode is not None and temp_node2.nextNode.coefficient != 0:
                        temp_node2 = temp_node2.nextNode
                    temp_node2.nextNode = Polynode(i, coefficient_sum)
            i += 1
        return new_poly

a = Polynomial(1, 2) # 2x
b = Polynode(2, 3) # 3x^2
a.polyHead.nextNode = b
a.count_degree()

c = Polynomial(3, 5) # 5x^3
d = Polynode(2, 3) # 3x^2
c.polyHead.nextNode = d
c.count_degree()
e = a.multiply(c)
e.count_degree()
e = e.uniteliketerms()


temp_node = e.polyHead
while temp_node is not None and temp_node.coefficient != 0:
    print(str(temp_node.coefficient) + "x^" + str(temp_node.degree))
    print()
    temp_node = temp_node.nextNode

