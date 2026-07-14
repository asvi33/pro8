import numpy as np


class DataAnalytics:

    def __init__(self):
        self.array = None

    # -------------------- MAIN MENU --------------------

    def menu(self):
        while True:
            print("\nWelcome to the NumPy Analyzer!")
            print("=" * 40)
            print("Choose an option:\n")
            print("1. Create a Numpy Array")
            print("2. Perform Mathematical Operations")
            print("3. Combine or Split Arrays")
            print("4. Search, Sort, or Filter Arrays")
            print("5. Compute Aggregates and Statistics")
            print("6. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.create_array()

            elif choice == "2":
                self.math_menu()

            elif choice == "3":
                self.combine_split_menu()

            elif choice == "4":
                self.search_sort_filter_menu()

            elif choice == "5":
                self.statistics_menu()  # Displays all 5 metrics together

            elif choice == "6":
                print("\nThank you for using the NumPy Analyzer! Goodbye!")
                break

            else:
                print("Invalid Choice!")

    # -------------------- ARRAY CREATION --------------------

    def create_array(self):
        while True:
            print("\nArray Creation:")
            print("1. 1D Array")
            print("2. 2D Array")
            print("3. 3D Array")
            print("4. Go Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                n = int(input("Enter number of elements: "))
                data = list(
                    map(int, input(f"Enter {n} elements: ").split())
                )

                if len(data) != n:
                    print("Incorrect number of elements.")
                    continue

                self.array = np.array(data)
                print("\nArray Created Successfully:")
                print(self.array)
                self.index_slice_menu()

            elif choice == "2":
                rows = int(input("Enter number of rows: "))
                cols = int(input("Enter number of columns: "))
                total = rows * cols

                data = list(
                    map(
                        int,
                        input(f"Enter {total} elements: ").split(),
                    )
                )

                if len(data) != total:
                    print("Incorrect number of elements.")
                    continue

                self.array = np.array(data).reshape(rows, cols)
                print("\nArray Created Successfully:")
                print(self.array)
                self.index_slice_menu()

            elif choice == "3":
                x = int(input("Enter first dimension: "))
                y = int(input("Enter second dimension: "))
                z = int(input("Enter third dimension: "))
                total = x * y * z

                data = list(
                    map(
                        int,
                        input(f"Enter {total} elements: ").split(),
                    )
                )

                if len(data) != total:
                    print("Incorrect number of elements.")
                    continue

                self.array = np.array(data).reshape(x, y, z)
                print("\nArray Created Successfully:")
                print(self.array)
                self.index_slice_menu()

            elif choice == "4":
                break

            else:
                print("Invalid Choice!")

    # -------------------- INDEXING & SLICING --------------------

    def index_slice_menu(self):
        while True:
            print("\nChoose an operation:")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                if self.array.ndim == 1:
                    i = int(input("Enter index: "))
                    print("Element:", self.array[i])

                elif self.array.ndim == 2:
                    r = int(input("Enter row: "))
                    c = int(input("Enter column: "))
                    print("Element:", self.array[r, c])

                else:
                    a = int(input("First index: "))
                    b = int(input("Second index: "))
                    c = int(input("Third index: "))
                    print("Element:", self.array[a, b, c])

            elif choice == "2":
                if self.array.ndim == 1:
                    s = int(input("Start: "))
                    e = int(input("End: "))
                    print(self.array[s:e])

                elif self.array.ndim == 2:
                    row = input("Row range (start:end): ")
                    col = input("Column range (start:end): ")

                    r1, r2 = map(int, row.split(":"))
                    c1, c2 = map(int, col.split(":"))

                    print(self.array[r1:r2, c1:c2])

                else:
                    print("3D slicing not implemented.")

            elif choice == "3":
                break

            else:
                print("Invalid Choice!")

    # -------------------- MATHEMATICAL OPERATIONS --------------------

    def math_menu(self):
        if self.array is None:
            print("\nPlease create an array first.")
            return

        print("\nMathematical Operations")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Enter your choice: ")
        total = self.array.size

        elements = list(
            map(
                int,
                input(
                    f"\nEnter {total} elements separated by space: "
                ).split(),
            )
        )

        if len(elements) != total:
            print("Incorrect number of elements.")
            return

        second = np.array(elements).reshape(self.array.shape)

        print("\nOriginal Array:")
        print(self.array)

        print("\nSecond Array:")
        print(second)

        if choice == "1":
            print("\nResult of Addition:")
            print(self.array + second)

        elif choice == "2":
            print("\nResult of Subtraction:")
            print(self.array - second)

        elif choice == "3":
            print("\nResult of Multiplication:")
            print(self.array * second)

        elif choice == "4":
            if np.any(second == 0):
                print("\nDivision by zero is not allowed.")
            else:
                print("\nResult of Division:")
                print(self.array / second)

        else:
            print("Invalid Choice!")

    # -------------------- COMBINE & SPLIT --------------------

    def combine_split_menu(self):
        if self.array is None:
            print("\nPlease create a NumPy array first.")
            return

        while True:
            print("\nCombine or Split Arrays:")
            print("Choose an option:")
            print("1. Combine Arrays")
            print("2. Split Array")
            print("3. Go Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                total = self.array.size

                data = list(
                    map(
                        int,
                        input(
                            f"\nEnter the elements of another array to combine ({total} elements separated by space): "
                        ).split(),
                    )
                )

                if len(data) != total:
                    print("Incorrect number of elements.")
                    continue

                arr2 = np.array(data).reshape(self.array.shape)

                print("\nOriginal Array:")
                print(self.array)

                print("\nSecond Array:")
                print(arr2)

                print("\n1. Vertical Stack")
                print("2. Horizontal Stack")

                op = input("Enter your choice: ")

                if op == "1":
                    print("\nCombined Array (Vertical Stack):")
                    print(np.vstack((self.array, arr2)))

                elif op == "2":
                    print("\nCombined Array (Horizontal Stack):")
                    print(np.hstack((self.array, arr2)))

                else:
                    print("Invalid Choice!")

            elif choice == "2":
                print("\nOriginal Array:")
                print(self.array)

                if self.array.ndim == 1:
                    parts = np.array_split(self.array, 2)
                    print("\nFirst Part:")
                    print(parts[0])
                    print("\nSecond Part:")
                    print(parts[1])

                elif self.array.ndim == 2:
                    print("\n1. Split Rows")
                    print("2. Split Columns")

                    op = input("Enter your choice: ")

                    if op == "1":
                        rows = np.vsplit(self.array, self.array.shape[0])
                        for i, row in enumerate(rows, 1):
                            print(f"\nRow {i}:")
                            print(row)

                    elif op == "2":
                        cols = np.hsplit(self.array, self.array.shape[1])
                        for i, col in enumerate(cols, 1):
                            print(f"\nColumn {i}:")
                            print(col)

                    else:
                        print("Invalid Choice!")

                else:
                    parts = np.array_split(self.array, 2)
                    for i, part in enumerate(parts, 1):
                        print(f"\nPart {i}:")
                        print(part)

            elif choice == "3":
                break

            else:
                print("Invalid Choice!")

    # -------------------- SEARCH, SORT, FILTER --------------------

    def search_sort_filter_menu(self):
        if self.array is None:
            print("\nPlease create an array first.")
            return

        while True:
            print("\nSearch, Sort, and Filter:")
            print("Choose an option:")
            print("1. Search a value")
            print("2. Sort the array")
            print("3. Filter values")
            print("4. Go Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                val = int(input("Enter value to find: "))
                indices = np.where(self.array == val)
                print(f"Indices where value {val} is found: {indices}")

            elif choice == "2":
                print("\nOriginal Array:")
                print(self.array)

                print("\nSorted Array:")
                if self.array.ndim == 2:
                    print(np.sort(self.array, axis=1))
                    print("(Sorting applied row-wise.)")
                else:
                    print(np.sort(self.array, axis=None))

            elif choice == "3":
                threshold = int(input("Enter threshold (filter elements >): "))
                filtered = self.array[self.array > threshold]
                print(f"\nElements greater than {threshold}:")
                print(filtered)

            elif choice == "4":
                break
            else:
                print("Invalid Choice!")

    # -------------------- PART 5: ALL AGGREGATES & STATISTICS --------------------

    def statistics_menu(self):
        if self.array is None:
            print("\nPlease create an array first.")
            return

        print("\nAggregates and Statistics:")
        print("Original Array:")
        print(self.array)
        print("-" * 30)
        
        # Displays all 5 statistics concurrently
        print(f"1. Sum of Array: {np.sum(self.array)}")
        print(f"2. Mean of Array: {np.mean(self.array)}")
        print(f"3. Median of Array: {np.median(self.array)}")
        print(f"4. Standard Deviation of Array: {np.std(self.array)}")
        print(f"5. Variance of Array: {np.var(self.array)}")
        print("-" * 30)


# -------------------- DRIVER CODE --------------------

if __name__ == "__main__":
    obj = DataAnalytics()
    obj.menu()
