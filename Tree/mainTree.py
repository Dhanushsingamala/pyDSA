class Treenode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)   

    #for indentation --> get level function and add spaces
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level+=1
            p = p.parent

        return level

    #we are going through all element we are printing data one by one
    def print_tree(self):
        # print(self.data) -> modify using len spaces
            # spaces = ' ' * self.get_level()
            # print(spaces + self.data)
        #to make look like tree we add prefix like this
        spaces= ' '*self.get_level() *3
        prefix = spaces + '|__' if self.parent else ""
        print(f'{prefix}{self.data}')

        #to check that children is not empty at leaf nodes 
        if len(self.children)>0:
            for child in self.children:
                # print(child.data)  -> instead using recursion
                child.print_tree()    

    
def build_product_tree():
    root = Treenode("Electronics")

    laptop = Treenode("Laptop")
    laptop.add_child(Treenode("Macbook M1"))
    laptop.add_child(Treenode("windows Ideapad"))
    laptop.add_child(Treenode("linux Thinkpad"))

    cellphone = Treenode("cell phone")
    cellphone.add_child(Treenode("Iphone 15pro Max"))
    cellphone.add_child(Treenode("Google pixel"))
    cellphone.add_child(Treenode("vivo v7"))

    tv = Treenode("TV")
    tv.add_child(Treenode("Samsung s7 edge"))
    tv.add_child(Treenode("Vizio V40e"))
    tv.add_child(Treenode("Panasonic plasma TV"))
    tv.add_child(Treenode("lg"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    # print(tv.get_level()) -> 1
    # print(lg.get_level()) -> 2   we modify print based on this

    return root

if __name__ == "__main__":
    root = build_product_tree()
    # print(root.get_level)
    root.print_tree()