"""  ----------------------------顯示包包內物品--------------------------------------- """
def DisplayInventory(Inventory):
    print("Inventory:")
    item_total = 0
    for k,v in Inventory.items():
        print(k ,end=' ')
        print(v)
        item_total = item_total + int(v)
    print("Total number of items: " + str(item_total))


Backpack = {'repe':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}
DisplayInventory(Backpack)


print ("------------------------------分隔線----------------------------------------")

""" ----------------------------增加包包內物品---------------------------------------"""
def AddToInventory(Inventory, AddedItems):
    for x in range(5):
        if AddedItems[x] in Inventory.keys():
            Inventory[AddedItems[x]]=Inventory[AddedItems[x]]+1
        else:
            AddedItems[x]={AddedItems[x]:1}
            Inventory.update(AddedItems[x])




inv = {'gold coin': 42, 'rope': 1}

DragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin','ruby']

ivn = AddToInventory(inv, DragonLoot)
DisplayInventory(inv)