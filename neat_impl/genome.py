from neat_impl.node_gene import NodeGene, NodeTypes
from neat_impl.connection_gene import ConnectionGene
import random


class Genome:
    def __init__(self, params):
        self.connection_genes = []  # connection of the node genes => phenotype
        self.nodes = []  # represents input/output node genes

        self.fitness = None

    def mutate(self):
        pass

    def crossover(self, other_parent):
        pass

    def _mutate_add_connection(self):
        in_node = self.nodes[random.randint(len(self.nodes))]
        out_node = self.nodes[random.randint(len(self.nodes))]
        weight = random.randrange(-1, 1)

        if in_node.node_type == NodeTypes.HIDDEN and \
                out_node.node_type == NodeTypes.INPUT:
            in_node, out_node = out_node, in_node

        if in_node.node_type == NodeTypes.OUTPUT and \
                out_node.node_type == NodeTypes.HIDDEN:
            in_node, out_node = out_node, in_node

        if in_node.node_type == NodeTypes.OUTPUT and \
                out_node.node_type == NodeTypes.INPUT:
            in_node, out_node = out_node, in_node

        self.connection_genes \
            .append(ConnectionGene(in_node, out_node, weight, 0))

    def _mutate_add_node(self):
        rand_con = random.randint(len(self.connection_genes))
        connection = self.connection_genes[rand_con]
        self.connection_genes[rand_con].disable()

        in_node = connection.in_node
        out_node = connection.out_node

        new_node = NodeGene(len(self.nodes), NodeTypes.HIDDEN)

        in_to_new = ConnectionGene(in_node, new_node, 1, 0)
        new_to_out = ConnectionGene(new_node, out_node, connection.weight, 0)

        self.nodes.append(new_node)
        self.connection_genes.append([in_to_new, new_to_out])
