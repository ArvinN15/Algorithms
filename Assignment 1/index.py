import time

class Product:
    def __init__(self, pid, name, price, category):
        self.pid = pid
        self.name = name
        self.price = price
        self.category = category

class ProductManager:
    def __init__(self):
        self.products = []

    def load_data(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                product = Product(data[0], data[1], float(data[2]), data[3])
                self.products.append(product)

    def insert_product(self, product):
        self.products.append(product)

    def update_product(self, pid, name=None, price=None, category=None):
        for p in self.products:
            if p.pid == pid:
                if name:
                    p.name = name
                if price:
                    p.price = price
                if category:
                    p.category = category
                break

    def delete_product(self, pid):
        self.products = [p for p in self.products if p.pid != pid]

    def search_product(self, key, value):
        results = []
        if key == 'ID':
            results = [p for p in self.products if value in p.pid]
        elif key == 'Name':
            results = [p for p in self.products if value in p.name]
        elif key == 'Price':
            results = [p for p in self.products if p.price == float(value)]
        elif key == 'Category':
            results = [p for p in self.products if value in p.category]

        if not results:
            return f"No products found for {key} '{value}'."
        else:
            return results

    def bubble_sort(self):
        n = len(self.products)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.products[j].price > self.products[j+1].price:
                    self.products[j], self.products[j+1] = self.products[j+1], self.products[j]

    def insertion_sort(self):
        for i in range(1, len(self.products)):
            key = self.products[i]
            j = i - 1
            while j >= 0 and key.price < self.products[j].price:
                self.products[j + 1] = self.products[j]
                j -= 1
            self.products[j + 1] = key

if __name__ == "__main__":
    manager = ProductManager()
    manager.load_data('product_data.txt')

    # Testing operations
    print("Initial Products:")
    for product in manager.products:
        print(f"ID: {product.pid}, Name: {product.name}, Price: {product.price}, Category: {product.category}")

    # Insert operation
    new_product = Product('101', 'New Product', 29.99, 'Electronics')
    manager.insert_product(new_product)
    print("\nAfter Insertion:")
    for product in manager.products:
        print(f"ID: {product.pid}, Name: {product.name}, Price: {product.price}, Category: {product.category}")

    # Update operation
    manager.update_product('101', name='Updated Product Name')
    print("\nAfter Update:")
    for product in manager.products:
        print(f"ID: {product.pid}, Name: {product.name}, Price: {product.price}, Category: {product.category}")

    # Delete operation
    manager.delete_product('101')
    print("\nAfter Deletion:")
    for product in manager.products:
        print(f"ID: {product.pid}, Name: {product.name}, Price: {product.price}, Category: {product.category}")

    # Search operation
    print("\nSearch Results:")
    search_results = manager.search_product('Name', 'Shirt')
    for product in search_results:
        print(f"ID: {product.pid}, Name: {product.name}, Price: {product.price}, Category: {product.category}")

    # Bubble sort
    start_time = time.time()
    manager.bubble_sort()
    end_time = time.time()
    print("\nAfter Bubble Sort:")
    for product in manager.products:
        print(f"ID: {product.pid}, Name: {product.name}, Price: {product.price}, Category: {product.category}")

    # Insertion sort
    start_time = time.time()
    manager.insertion_sort()
    end_time = time.time()
    print("\nAfter Insertion Sort:")
    for product in manager.products:
        print(f"ID: {product.pid}, Name: {product.name}, Price: {product.price}, Category: {product.category}")
    print(f"\nTime taken for Insertion Sort: {end_time - start_time:.6f} seconds")
    print(f"\nTime taken for Bubble Sort: {end_time - start_time:.6f} seconds")