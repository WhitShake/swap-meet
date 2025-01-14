

class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
        

    def vendor_has_inventory(self):
        if len(self.inventory) > 0:
            return self.inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item
        
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id ==id:
                return item
        return None
    

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)

        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)

        return True
    
    
    def swap_first_item(self, other_vendor):

        if not self.inventory or not other_vendor.inventory:
            return False
        
        my_item = self.inventory.pop(0)
        their_item = other_vendor.inventory.pop(0)

        self.inventory.append(their_item)
        other_vendor.inventory.append(my_item)

        return True


    def get_by_category(self,category):
        return [item for item in self.inventory if item.get_category()== category]

        
    def get_best_by_category(self, category):
        items_in_category = self.get_by_category(category)
        if not items_in_category:
            return None
        return max(items_in_category, key= lambda item: item.condition)


    def swap_best_by_category(self, other_vendor, my_priority, their_priority):

        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        if not my_best_item or not their_best_item:
            return False
        
        return self.swap_items(other_vendor, my_best_item, their_best_item)