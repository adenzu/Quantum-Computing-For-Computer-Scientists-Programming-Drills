from dataclasses import dataclass
import heapq


@dataclass
class Node:
    frequency: float
    symbol: str = None
    left: 'Node' = None
    right: 'Node' = None

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __str__(self) -> str:
        return f'{self.frequency} {self.symbol}\n{self.left}\n{self.right}'


def createHuffmanTree(symbols: list, frequencies: list[float]) -> Node:
    tree = []
    for symbol, frequency in zip(symbols, frequencies):
        heapq.heappush(tree, Node(frequency, symbol))
    while len(tree) > 1:
        node1 = heapq.heappop(tree)
        node2 = heapq.heappop(tree)
        heapq.heappush(tree, Node(node1.frequency +
                       node2.frequency, left=node1, right=node2))
    return tree[0]


def main():
    symbols = ['A', 'B', 'C', 'D', 'E']
    frequencies = [0.1, 0.2, 0.3, 0.25, 0.15]
    tree = createHuffmanTree(symbols, frequencies)
    print(str(tree).replace(' None\n', '\n').replace('None\n', ''))


if __name__ == '__main__':
    main()
