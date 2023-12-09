from artificial_tree import ArtificialTree

def main():
    tree1 = ArtificialTree("Dongyi", 100, 2000, "plastic", True, "14.11.2020")
    tree2 = ArtificialTree("Sunwing ", 120, 1000, "metalic", False, "13.12.2222")
    tree3 = ArtificialTree("Nearly", 120, 3000, "wooden", True, "10.08.2024")

    print(tree1)
    print(tree2)
    print(tree3)

if __name__ == "__main__": 
    main()